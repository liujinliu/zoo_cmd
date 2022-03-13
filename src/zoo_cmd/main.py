# -*- coding: utf-8 -*-
import pkgutil
from importlib import import_module
from zoo_cmd.cmd_register import BaseCmd
from zoo_cmd import cmds

for _, name, _ in pkgutil.iter_modules(cmds.__path__):
    # print('loading cmd %s ...' % (name, ))
    import_module('.cmds.%s' % (name, ), package=__package__)


def main():
    cmd = BaseCmd.ZOO_CMD
    cmd.cmdloop()

