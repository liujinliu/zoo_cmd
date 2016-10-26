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
    (Cmd) help
    
    Documented commands (type help <topic>):
    ========================================
    conn  help
    
    Undocumented commands:
    ======================
    cat  cd  exit  ls  pwd  rm  set  touch  vi
    (Cmd) ls           ----查看当前节点下的子节点
    + zookeeper           2016-02-03 16:25:12
    + test                2016-02-03 16:25:12
    (Cmd) wc           ----查看当前节点下的子节点个数
    2 
    (Cmd) cd test      ----进入子节点路径(支持跟绝对路径参数，类似"/test/docker"这种)
    /test
    (Cmd) ls           ----查看当前节点下的子节点
    + docker              2016-02-03 16:25:12
    (Cmd) cd docker
    /test/docker
    (Cmd) ls
    + acb896d8            2016-02-03 16:25:12
    (Cmd) touch tmp_ljl   ----创建新节点
    /test/docker/tmp_ljl
    (Cmd) set tmp_ljl csdn0   ----向节点写入内容(会覆盖原有内容)
    ZnodeStat(czxid=313532612647, ...... pzxid=313532612647)
    (Cmd) cat tmp_ljl    ----查看节点内容
    csdn0
    (Cmd) pwd             ----查看当前所处的绝对路径
    /test/docker
    (Cmd) ls
    - tmp_ljl             2016-02-03 16:25:12
    acb896d8
    (Cmd) rm tmp_ljl  ----删除节点
    None
    (Cmd) cd ..      ----回退(同时支持类似于"../.."这样的回退多层路径)
    /test
    (Cmd)

use vi to edit the node:
::

    (Cmd) vi tmp_ljl

