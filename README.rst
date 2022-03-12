zoo_cmd
===========
I hope I can operate zookeeper path like localfile system

INSTALL
~~~~~~~~~~~~~~~
install from pypi:

::

    pip install zoo_cmd

install from source:

::

    git clone git@github.com:liujinliu/zoo_cmd.git
    cd zoo_cmd
    make install
    make uninstall ---UNDEPLOY METHOD

USEAGE
~~~~~~~~~~~~~

::

    [liujinliu@liujinliu zoo_cmd]$ zk_cmd
    zoo#> conn 127.0.0.1 
    zoo@127.0.0.1:2181#> help
    Documented commands (type help <topic>):
    ========================================
    conn  help
    
    Undocumented commands:
    ======================
    cat  cd  cdcd  exit  ls  pwd  rm  set  touch  vi  wc
    zoo@127.0.0.1:2181#> ls           ----查看当前节点下的子节点
    + zookeeper           2016-02-03 16:25:12
    + test                2016-02-03 16:25:12
    zoo@127.0.0.1:2181#> wc           ----查看当前节点下的子节点个数
    2 
    zoo@127.0.0.1:2181#> cd test      ----进入子节点路径(支持跟绝对路径参数，类似"/test/docker"这种)
    /test
    zoo@127.0.0.1:2181#> ls           ----查看当前节点下的子节点
    + docker              2016-02-03 16:25:12
    zoo@127.0.0.1:2181#> cd docker    ----if only there is only one child, you can also use cdcd
    /test/docker
    zoo@127.0.0.1:2181#> ls
    + acb896d8            2016-02-03 16:25:12
    zoo@127.0.0.1:2181#> touch tmp_ljl   ----创建新节点
    /test/docker/tmp_ljl
    zoo@127.0.0.1:2181#> set tmp_ljl csdn0   ----向节点写入内容(会覆盖原有内容)
    ZnodeStat(czxid=313532612647, ...... pzxid=313532612647)
    zoo@127.0.0.1:2181#> cat tmp_ljl    ----查看节点内容
    csdn0
    zoo@127.0.0.1:2181#> pwd             ----查看当前所处的绝对路径
    /test/docker
    zoo@127.0.0.1:2181#> ls
    - tmp_ljl             2016-02-03 16:25:12
    acb896d8
    zoo@127.0.0.1:2181#> rm tmp_ljl  ----删除节点
    None
    zoo@127.0.0.1:2181#> cd ..      ----回退(同时支持类似于"../.."这样的回退多层路径)
    /test
    zoo@127.0.0.1:2181#> ls
    + gary                               2016-11-06 10:40:04
    + zookeeper                               1970-01-01 08:00:00
    zoo@127.0.0.1:2181#> cat gar*/tmp*
    --gary/tmp0:
    gary,1
    --gary/tmp1:
    gary,2

use vi to edit the node:
::

    zoo@127.0.0.1:2181#> vi tmp_ljl

