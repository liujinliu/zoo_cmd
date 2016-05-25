# zoo_cmd
I hope I can operate zookeeper path like localfile system

## DEPLOY METHOD
### install from pypi
    pip install zoo_cmd
### install from source
    make install
    make uninstall ---UNDEPLOY METHOD

## USEAGE
```
[liujinliu@liujinliu zoo_cmd]$ zk_cmd
(Cmd) help

Documented commands (type help <topic>):
========================================
conn  help

Undocumented commands:
======================
cat  cd  exit  ls  pwd  rm  set  touch  vi
(Cmd) ls           ----查看当前节点下的子节点
zookeeper
test
(Cmd) cd test      ----进入子节点路径
/test
(Cmd) ls           ----查看当前节点下的子节点
docker
(Cmd) cd docker
/test/docker
(Cmd) ls
acb896d8
(Cmd) touch tmp_ljl   ----创建新节点
/test/docker/tmp_ljl
(Cmd) set tmp_ljl csdn0   ----向节点写入内容(会覆盖原有内容)
ZnodeStat(czxid=313532612647, ...... pzxid=313532612647)
(Cmd) cat tmp_ljl    ----查看节点内容
csdn0
(Cmd) pwd             ----查看当前所处的绝对路径
/test/docker
(Cmd) ls
tmp_ljl
acb896d8
(Cmd) rm tmp_ljl  ----删除节点
None
(Cmd) cd ..      ----回退到上一层节点(目前每次只能回退一层，可以回退多次)
/test
(Cmd)
```

## use vi to edit the node
```
(Cmd) vi tmp_ljl
```
## TODO LIST
* Need to publish the module to pypi 
