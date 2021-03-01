# This is the MySQL Test Client with Java Connector

1. To compile
Setup classpath correctly

```shell
THISCLASSPATH=.
for i in `ls -1 lib`
do
THISCLASSPATH=$THISCLASSPATH:./lib/$i
done
export CLASSPATH=$THISCLASSPATH
```

Comiling the JavaClient.java
```shell
javac -classpath $THISCLASSPATH JavaClient.java
```

2. To run
```
java -classpath $THISCLASSPATH JavaClient -h<mds host>:<port -u<user> -p<password> -t<thread> -l<loop>
```

