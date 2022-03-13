# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check, never_crash)


@CmdRegister(func_name='set')
class CmdSet(BaseCmd):

    @never_crash
    @client_check
    def do(self, line=None):
        path, value = line.split()
        print(self.zoo.set('/' + path, value))
