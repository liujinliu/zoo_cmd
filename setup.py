# -*- coding: utf-8 -*-
import sys
import os
import setuptools

def _setup():
    setuptools.setup(
        name='zoo_cmd',
        version='0.0.1',
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
            'Environment :: Console',
            'Topic :: Utilities',
        ],
    )

def main():
    _setup()


if __name__ == '__main__':
    main()
