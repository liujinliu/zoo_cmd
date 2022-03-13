# -*- coding: utf-8 -*-
import os
import setuptools
from setuptools import find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(HERE, 'README.rst'), 'r', encoding='utf-8') as f:
        return f.read()


def _setup():
    setuptools.setup(
        name='zoo_cmd',
        version='1.1.0',
        description='zookeeper cli client',
        long_description=readme(),
        author='liujinliu',
        url='https://github.com/liujinliu/zoo_cmd',
        license='Apache',
        install_requires=['kazoo'],
        packages=find_packages('src'),
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
