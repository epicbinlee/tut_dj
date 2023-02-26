SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
# web端口监控
celery -A dj_cly.celery_app flower --port=5555