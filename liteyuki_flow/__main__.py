import os
from contextvars import Context

# 插件编写者造成的错误需要raise
# 用户输入错误需要print提示并返回

if __name__ == '__main__':
    # ENV
    # TOKEN：API token   用于访问GitHub
    # ISSUE_ID：Issue number  用于访问指定Issue
    # REPO：Repository name  用于访问指定仓库
    TOKEN = os.getenv('TOKEN')
    ISSUE_ID = os.getenv('ISSUE_ID')
    REPO = os.getenv('REPO')

    if not all([TOKEN, ISSUE_ID, REPO]):
        raise ValueError('Please set TOKEN, ISSUE_ID and REPO environment variables.')
