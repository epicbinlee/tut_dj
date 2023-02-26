SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
# cly_tasks.celery_app
celery -A cly_tasks.celery worker -l INFO