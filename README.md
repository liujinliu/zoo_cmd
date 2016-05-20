# zoo_cmd
I hope I can operate zookeeper path like localfile system

## DEPLOY METHOD
    make install
    make uninstall ---UNDEPLOY METHOD

## USEAGE
```
[liujinliu@liujinliu zoo_cmd]$ zk_cmd
(Cmd) conn
instance zk client (127.0.0.1:2181)
(Cmd) ls
[u'letv', u'zookeeper']
(Cmd) ls letv
[u'docker']
(Cmd) ls letv/docker
[u'acb896d8-078c']
```

## TODO LIST
* Need to add some decorator to check if the conn is alive and anything others
