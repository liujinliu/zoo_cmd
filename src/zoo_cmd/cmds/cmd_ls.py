# -*- coding: utf-8 -*-

from zoo_cmd.cmd_register import (
    BaseCmd, CmdRegister, client_check, never_crash)


@CmdRegister(func_name='ls')
class CmdLs(BaseCmd):

    @never_crash
    @client_check
    def do(self, line=None):
        max_pname_len = 38
        for pname in self.zoo.ls(line):
            max_pname_len = max(max_pname_len, len(pname))

        for pname in sorted(self.zoo.ls(line)):
            time_str = self.zoo.get_extra_info('%s/%s' % (line, pname))
            prefix = '+'
            if not len(self.zoo.ls('%s/%s' % (line, pname))):
                prefix = '-'
            _pname = ('%s %-*s  %s' % (prefix, max_pname_len, pname, time_str))
            print(_pname)
