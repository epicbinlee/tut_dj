SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
echo `pwd`
gunicorn -c bin/gunicorn.conf.py  dj.wsgi:application