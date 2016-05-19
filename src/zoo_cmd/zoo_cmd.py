#coding=utf-8
from cmd import Cmd
import sys

class ZooCmd(Cmd):
    
    def __init__(self):
        Cmd.__init__(self)
        self.name = 'name0'

    def help_help(self):
        print self.name
        self.name = 'name1'
        print ("This is a zookeeper client cmd tool, "
               "you can operate zookeeper like operate "
               "a common file system")

    def do_exit(self, line):
        print "Bye"
        print self.name
        sys.exit()

def main():
    cmd = ZooCmd()
    cmd.cmdloop()

