# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check, never_crash)


@CmdRegister(func_name='touch')
class CmdTouch(BaseCmd):

    @never_crash
    @client_check
    def do(self, line=None):
        print(self.zoo.touch('/'+line))
