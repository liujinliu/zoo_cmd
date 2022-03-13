# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check, never_crash)


@CmdRegister(func_name='cdcd')
class CmdCdCd(BaseCmd):

    @never_crash
    @client_check
    def do(self, line=None):
        lines = self.zoo.ls(line)
        if len(lines) == 1:
            print(self.zoo.cd(lines[0]))
        else:
            print('no default path')

