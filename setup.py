# -*- coding: utf-8 -*-
import sys
import os
import setuptools
from version import __VERSION__

def _setup():
    setuptools.setup(
        name='zoo_cmd',
        version=__VERSION__,
        description='zookeeper client',
        author='liujinliu',
        author_email='',
        url='',
        install_requires=['kazoo'],
        packages=['zoo_cmd', 'zoo_cmd.zk'],
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': [
                'zk_cmd=zoo_cmd.main:main',
                ]
            },
        classifiers=[
            'Development Status :: 4 - Beta Development Status',
            'Environment :: Console',
            'Topic :: Utilities',
        ],
    )

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'publish':
            os.system('make publish')
            sys.exit()
        elif sys.argv[1] == 'release':
            if len(sys.argv) < 3:
                type_ = 'patch'
            else:
                type_ = sys.argv[2]
            assert type_ in ('major', 'minor', 'patch')

            os.system('bumpversion --current-version {} {}'
                      .format(__VERSION__, type_))
            sys.exit()

    _setup()


if __name__ == '__main__':
    main()
