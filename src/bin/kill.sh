SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
kill -9 `ps -ef | grep 8000 | grep -v grep | awk '{print $2}'`
ps -ef | grep 8000 | grep -v grep