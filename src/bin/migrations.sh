SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/..
python3 manage.py makemigrations
python3 manage.py migrate django_celery_results