SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
celery -A dj_cly.celery_app worker -P eventlet -c 1000 -l INFO -E