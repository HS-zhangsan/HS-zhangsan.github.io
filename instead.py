import os
import re

# 需要替换的图床链接
old_url = 'C:/Files/markdown-images'

# 本地图片文件夹路径
local_path = 'C:/Files/markdown-images/'

# 替换后的本地图片链接前缀
new_url = 'C:/Files/markdown-images/'

# 遍历当前目录下的所有Markdown文档
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            # 读取Markdown文档内容
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # 使用正则表达式查找并替换图床链接
            pattern = re.compile(f'{old_url}(.*?)\)')
            content = pattern.sub(f'{new_url}\\1)', content)
            # 将替换后的内容写入原Markdown文档
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
