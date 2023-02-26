SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
redis-server /etc/redis.conf > /dev/null 2>&1 &
sleep 3
tailf /var/log/redis/redis.log
#netstat -nltp | grep redis