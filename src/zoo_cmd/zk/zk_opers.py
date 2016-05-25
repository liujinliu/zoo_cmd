#coding=utf-8

from kazoo.client import KazooClient, KazooState

def fullpath(func):
    def wrapper(self, path, *args):
        fullpath =  self.prefix_path + path \
                   if path else self.prefix_path
        return func(self, fullpath, *args)
    return wrapper



class ZkOpers(object):
    
    def __init__(self, hosts='127.0.0.1:2181'):
            self.zk = KazooClient(hosts=hosts, timeout=20)
            self.zk.add_listener(self.listener)
            self.zk.start()
            print 'instance zk client (%s)' % hosts
            self.prefix_path = '/'

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
            print ("zk connect lost, stop this "
                   "connection and then start new one!")
            
        elif state == KazooState.SUSPENDED:
            print ("zk connect suspended, stop this "
                   "connection and then start new one!")
        else:
            pass

    @fullpath
    def ls(self, path=None, *args):
        return self.zk.get_children(path)

    def cd(self, path=None):
        if not path:
            return
        _pathlist = self.prefix_path.split('/')
        if path == '..' and len(_pathlist) > 0:
            _pathlist.pop()
        else:
           _pathlist.append(path)
        _prefix_path = '/'.join(_pathlist).replace('//','/')
        if self.zk.exists(_prefix_path):
            self.prefix_path = _prefix_path
        else:
            print "unkown path"
        return  self.prefix_path

    def pwd(self):
        return self.prefix_path

    @fullpath
    def cat(self, path=None, *args):
        value, _ = self.zk.get(path)
        return value 

    @fullpath
    def set(self, path, value, *args):
        return self.zk.set(path, value)

    @fullpath
    def touch(self, filename, *args):
        return self.zk.create(filename)

    @fullpath
    def rm(self, filename, *args):
        return self.zk.delete(filename, recursive=True)
