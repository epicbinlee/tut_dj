SHELL_PATH=$(cd $(dirname $0);pwd)
cd $SHELL_PATH/../../..
echo `pwd`
if [[ -a tut_celery.tar.gz ]];then
  echo '压缩包文件存在.'
  rm -rf tut_celery.tar.gz
fi;
tar -zcvf tut_celery.tar.gz tut_celery

