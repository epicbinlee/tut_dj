import os
import compileall


def compile_project(_dir):
    """
    编译项目
    """
    # 删除目录
    for root, dirs, files in os.walk(_dir):
        for f in files:
            if str(root).__contains__('__pycache__') and str(f).endswith('pyc'):
                os.remove(os.path.join(root, f))
    # 编译
    compileall.compile_dir(_dir)
    # 遍历替换
    for root, dirs, files in os.walk(_dir):
        for f in files:
            if str(root).__contains__('__pycache__') and str(f).endswith('pyc'):
                fp1 = os.path.join(root, f)
                fp2 = os.path.join(root, str(f).replace(r'.cpython-36', ''))
                os.rename(fp1, fp2)


def freeze():
    os.system('pip3 freeze > ../requirements.txt')


def package_project():
    os.system('chmod +x pkg.sh && sh pkg.sh')


if __name__ == '__main__':
    compile_project(os.getcwd())
    freeze()
    package_project()
