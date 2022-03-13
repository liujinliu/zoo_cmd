# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check)


@CmdRegister(func_name='addauth')
class CmdAddAuth(BaseCmd):

    def help(self):
        print('addauth <schema> <name> <passwd>')

    @client_check
    def do(self, args=None):
        if not args:
            print('参数错误')
        paras = args.split()
        schema, username, passwd = paras[0], paras[1], paras[2]
        self.zoo.zk.add_auth(schema, username + ':' + passwd)
