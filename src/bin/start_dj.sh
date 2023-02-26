SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
python3 manage.py runserver 0.0.0.0:8005