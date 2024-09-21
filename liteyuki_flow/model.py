from typing import Optional

from pydantic import BaseModel


class Tag(BaseModel):
    label: str
    color: str


class Resource(BaseModel):
    name: str
    description: str
    link: str
    homepage: Optional[str] = None
    tags: list[Tag]


class Plugin(BaseModel):
    name: str  # 插件名，可读名
    description: str  # 插件描述
    pypi_name: str  # 模块名,pypi项目名
    module_name: str  # 模块名，import时使用

    homepage: str  # 主页地址
    author: str  # 作者，默认使用提交者的GitHub用户名填充
    tags: list[Tag]  # 标签
