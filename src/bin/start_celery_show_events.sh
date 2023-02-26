SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
# linux界面监控
celery -A dj_cly.celery_app events