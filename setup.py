# -*- coding: utf-8 -*-
import sys
import os
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

def readme():
    with open(os.path.join(HERE, 'README.rst')) as f:
            return f.read()

def _setup():
    setuptools.setup(
        name='zoo_cmd',
        version='1.0.1',
        description='zookeeper cli client',
        long_description=readme(),
        author='liujinliu',
        author_email='liujinliu@le.com',
        url='https://github.com/liujinliu/zoo_cmd',
        license='Apache',
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
        ],
    )

def main():
    _setup()


if __name__ == '__main__':
    main()
