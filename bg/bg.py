# 备份将windows的桌面图片保存到指定文件夹

import shutil
import os

# 文件源路径
src_path = 'C:/Users/ispon/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/'

# 文件目标路径
target_path = 'C:/Users/ispon/OneDrive/Pictures/latest/'

for file in os.listdir(src_path):
    print('==> ' + file + '.png')
    shutil.copyfile(src_path + file, target_path + file + '.png')
