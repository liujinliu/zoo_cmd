#coding=utf-8
from cmd import Cmd
import sys
from zoo_cmd.zk import zk_opers
class ZooCmd(Cmd):
    
    def __init__(self):
        Cmd.__init__(self)
        self.zoo = None 

    def help_conn(self):
        print ("conn {host:port}")

    def do_conn(self, line='127.0.0.1:2181'):
        if not self.zoo:
            self.zoo = zk_opers.ZkOpers()
        else:
            print "client already connected"

    def do_exit(self, line):
        if self.zoo:
            child = self.zoo.zk.get_children('/')
            print child
        print "Bye"
        sys.exit()

def main():
    cmd = ZooCmd()
    cmd.cmdloop()

