# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check)


@CmdRegister(func_name='pwd')
class CmdPwd(BaseCmd):

    @client_check
    def do(self, line=None):
        print(self.zoo.pwd())
