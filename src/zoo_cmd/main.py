#coding=utf-8
from cmd import Cmd
import sys
from zoo_cmd.zk import zk_opers

def client_check(func):
    def wrapper(self, line, *args):
        if self.zoo:
            return func(self, line, *args)
    return wrapper

def never_crash(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except Exception as e:
            print("exception accur:%s" % str(e))
    return wrapper

class ZooCmd(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.zoo = None

    def help_conn(self):
        print("conn {host:port}")

    def do_conn(self, line):
        if len(line) == 0:
            line = '127.0.0.1:2181'
        if not self.zoo:
            self.zoo = zk_opers.ZkOpers(hosts=line)
        else:
            print("client already connected")

    def do_exit(self, line):
        print("Bye")
        sys.exit()

    @never_crash
    @client_check
    def do_ls(self,line=None, *args):
        for pname in sorted(self.zoo.ls(line)):
            time_str = self.zoo.get_mtime('%s/%s' % (line,pname))
            _pname = ('+ %-40s%s' % (pname, time_str) if \
                     len(self.zoo.ls('%s/%s' % (line,pname))) \
                     else ('- %-40s%s' % (pname, time_str)))
            print(_pname)

    @never_crash
    @client_check
    def do_wc(self,line=None, *args):
        print(len(self.zoo.ls(line)))

    @never_crash
    @client_check
    def do_cd(self,line=None):
        print(self.zoo.cd(line))

    @client_check
    def do_pwd(self,line=None):
        print(self.zoo.pwd())

    @never_crash
    @client_check
    def do_cat(self,line=None, *args):
        print(self.zoo.cat('/'+line))

    @never_crash
    @client_check
    def do_set(self,line, *args):
        path, value = line.split()
        print(self.zoo.set('/'+path, value))

    @never_crash
    @client_check
    def do_touch(self,line=None, *args):
        print(self.zoo.touch('/'+line))

    @never_crash
    @client_check
    def do_rm(self,line=None, *args):
        print(self.zoo.rm('/'+line))

    @never_crash
    @client_check
    def do_vi(self,line=None, *args):
        self.zoo.vi('/'+line)

def main():
    cmd = ZooCmd()
    cmd.cmdloop()

