#coding=utf-8

from kazoo.client import KazooClient, KazooState
import logging

class ZkOpers(object):
    
    def __init__(self, hosts='127.0.0.1:2181'):
            self.zk = KazooClient(hosts=hosts, timeout=20)
            self.zk.add_listener(self.listener)
            self.zk.start()
            logging.info("instance zk client (%s)" % hosts)


    def close(self):
        try:
            self.zk.stop()
            self.zk.close()
        except Exception, e:
            logging.error(e)
   
    def stop(self):
        try:
            self.zk.stop()
        except Exception, e:
            logging.error(e)
            raise

    def listener(self, state):
        if state == KazooState.LOST:
            logging.info("zk connect lost, stop this connection and then start new one!")
            
        elif state == KazooState.SUSPENDED:
            logging.info("zk connect suspended, stop this connection and then start new one!")
        else:
            pass

