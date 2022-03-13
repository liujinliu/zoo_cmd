# -*- coding: utf-8 -*-
import types
import sys
import traceback
from cmd import Cmd
from zoo_cmd.zk import zk_opers


class _ZooCmd(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.zoo = None
        self.prompt = 'zoo#>'

    def help_conn(self):
        print("conn {host:port}")

    def do_conn(self, line):
        if len(line) == 0:
            line = '127.0.0.1:2181'
        if not self.zoo:
            self.zoo = zk_opers.ZkOpers(hosts=line)
            self.prompt = 'zoo@%s#> ' %line
        else:
            print("client already connected")

    def do_exit(self, line):
        print("Bye")
        sys.exit()

    def emptyline(self):
        return


class BaseCmd:

    ZOO_CMD = _ZooCmd()

    REG_FUNC = dict()

    @property
    def zoo(self):
        return self.ZOO_CMD.zoo

    def do(self, line):
        print('unknown command')

    def help(self):
        print('there is no help message here')


def client_check(func):
    def wrapper(self, line, *args):
        if BaseCmd.zoo:
            return func(self, line, *args)
    return wrapper


def never_crash(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except Exception as e:
            print(traceback.format_exc())
    return wrapper


class CmdRegister:

    def __init__(self, func_name):
        self.__func_name = func_name

    def __call__(self, cls: BaseCmd):
        cmd_do = 'do_%s' % self.__func_name
        cmd_help = 'help_%s' % self.__func_name
        setattr(BaseCmd.ZOO_CMD, cmd_do,
                types.MethodType(cls.do, BaseCmd.ZOO_CMD))
        setattr(BaseCmd.ZOO_CMD, cmd_help,
                types.MethodType(cls.help, BaseCmd.ZOO_CMD))
        return cls
