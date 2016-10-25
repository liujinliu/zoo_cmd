#coding=utf-8

from kazoo.client import KazooClient, KazooState
import os
from datetime import datetime
import time

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
            print('instance zk client (%s)' % hosts)
            self.prefix_path = '/'

    def close(self):
        try:
            self.zk.stop()
            self.zk.close()
        except Exception as e:
            logging.error(e)

    def stop(self):
        try:
            self.zk.stop()
        except Exception as e:
            logging.error(e)
            raise

    def listener(self, state):
        if state == KazooState.LOST:
            print("zk connect lost, stop this "
                   "connection and then start new one!")

        elif state == KazooState.SUSPENDED:
            print("zk connect suspended, stop this "
                   "connection and then start new one!")
        else:
            pass

    @fullpath
    def get_mtime(self, path):
        _, stat = self.zk.get(path)
        mtime = int(stat.mtime)/1000
        timeA = time.localtime(mtime)
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', timeA)
        return time_str

    @fullpath
    def ls(self, path=None, *args):
        return self.zk.get_children(path)

    def _relative_path_cd(self, path):
        _pathlist = self.prefix_path.split('/')
        list(map(lambda x: _pathlist.pop() if x == '..' \
            else _pathlist.append(x),
            list(filter(lambda x:x, path.split('/')))))
        prefix_path = '/'.join(_pathlist).replace('//','/')
        return prefix_path

    def cd(self, path=None):
        if not path:
            return
        _prefix_path = path if path.startswith('/') else \
                        self._relative_path_cd(path)
        if self.zk.exists(_prefix_path):
            self.prefix_path = _prefix_path
        else:
            print("unkown path")
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

    @fullpath
    def vi(self, path=None, *args):
        value, _ = self.zk.get(path)
        # create a tmp file to store the value, then use vi to
        # modify this file. At the end, save the file, get the
        # new value, and restore the value to the zookeeper node
        filename = '%s_%d.tmp' % (path.split('/')[-1],
                  time.mktime(datetime.now().timetuple()))
        tmpfile = open(filename, 'w')
        if value:
            tmpfile.write(value)
        tmpfile.close()
        try:
            os.system('vi %s' % filename)
        except:
            print("error occur in edit")
            return
        tmpfile = open(filename, 'r')
        lines = tmpfile.read().strip('\n')
        self.zk.set(path, lines)
        tmpfile.close()
        os.remove(filename)
        print("edit ok")
