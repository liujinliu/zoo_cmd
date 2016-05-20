#coding=utf-8
from cmd import Cmd
import sys
from zoo_cmd.zk import zk_opers

def client_check(func):
    def wrapper(self, line):
        if self.zoo:
            return func(self, line)
    return wrapper


class ZooCmd(Cmd):
    
    def __init__(self):
        Cmd.__init__(self)
        self.zoo = None
    
    def help_conn(self):
        print ("conn {host:port}")

    def do_conn(self, line):
        if len(line) == 0:
            line = '127.0.0.1:2181'
        if not self.zoo:
            self.zoo = zk_opers.ZkOpers(hosts=line)
        else:
            print "client already connected"

    def do_exit(self, line):
        print "Bye"
        sys.exit()

    @client_check
    def do_ls(self,line=None):
        print self.zoo.ls(line)

    @client_check
    def do_cd(self,line=None):
        print self.zoo.cd(line)

    @client_check
    def do_pwd(self,line=None):
        print self.zoo.pwd()

def main():
    cmd = ZooCmd()
    cmd.cmdloop()

