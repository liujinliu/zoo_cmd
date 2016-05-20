# zoo_cmd
I hope I can operate zookeeper path like localfile system

## DEPLOY METHOD
    make install
    make uninstall ---UNDEPLOY METHOD

## USEAGE
```
[liujinliu@liujinliu zoo_cmd]$ zk_cmd
(Cmd) conn 127.0.0.1:2181
instance zk client (127.0.0.1:2181)
(Cmd) ls
[u'liujinliu', u'zookeeper']
(Cmd) ls liujinliu
[u'doc']
(Cmd) ls liujinliu/doc
[u'acb896d8-078c']
```

## TODO LIST
* Need to add some decorator to check if the conn is alive and anything others
