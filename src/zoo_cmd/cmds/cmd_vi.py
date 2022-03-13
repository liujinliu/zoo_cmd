# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check, never_crash)


@CmdRegister(func_name='vi')
class CmdVi(BaseCmd):

    @never_crash
    @client_check
    def do(self, line=None):
        self.zoo.vi('/'+line)
