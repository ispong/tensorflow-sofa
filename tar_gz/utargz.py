##
# 解压tar.gz文件
##

import tarfile
import sys

unzip_path = 'C:/Users/ispon/Desktop/unzip'

# 检查是否传递压缩文件参数
if len(sys.argv) == 1:
    print('file_path is null')
    sys.exit()

# 获取压缩文件路径
tar_path = sys.argv[1]

# 解压文件到执行文件夹
tar = tarfile.open(tar_path, mode="r:gz")
tar.extractall(path=unzip_path)
tar.close()
