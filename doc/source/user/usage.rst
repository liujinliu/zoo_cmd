USEAGE
=======

::

    [liujinliu@liujinliu zoo_cmd]$ zk_cmd
    zoo#> conn 127.0.0.1:2181    ---连接zookeeper
    zoo@127.0..01:2181#> addauth digest zkljl 123456  ----acl策略设置(如果目标zk设置了acl的话)
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
    + zookeeper