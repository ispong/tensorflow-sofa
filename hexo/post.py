##
# 更加快速创建hexo文件模板
##
import sys
import os

# 博客的位置
blogs_path = 'D:\\isxcode\\blogs-galaxy'

# 检查是否存在文件名
if len(sys.argv) == 1:
    print('post_name is null')
    sys.exit()

# 文章的名称
param_name = sys.argv[1]

# post "Sublime 创建新的文件夹"
post_split = param_name.split(' ', 1)

# 获取模板名
template_name = post_split[0].lower()

# hexo new xx - post = xx / "" ""
hexo_command = 'hexo new ' + template_name + ' -post=' + template_name + '/"' + param_name + '" "' + param_name + '"'
print("execute ==> " + hexo_command)

# 执行创建命令
execute_command = 'D: && cd ' + blogs_path + ' && ' + hexo_command
os.system(execute_command)
