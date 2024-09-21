from .model import Resource

tokens = {
    "名称": "NAME",
    "描述": "DESCRIPTION",
    "作者": "AUTHOR",
    "下载链接": "LINK",
    "主页": "HOMEPAGE",
    "标签": "TAGS",
    "标签们": "TAGS",

    "Name": "NAME",
    "Description": "DESCRIPTION",
    "Author": "AUTHOR",
    "Download": "LINK",
    "Homepage": "HOMEPAGE",
    "Tags": "TAGS",

}


def parse_resource_publish(content: str) -> Resource:
    """
    解析资源发布issue体
    Args:
        content: str
    Returns:
        dict[str, str]
    """
    result = {}
    current_key = None

    for line in content.splitlines():
        if line.startswith("###"):
            current_key = tokens.get(line[4:].strip(), None)
            if current_key is None:
                raise ValueError(f"Invalid key: {line[4:].strip()}")
        elif current_key:
            result[current_key] = line.strip()
            current_key = None
    return Resource(
        name=result.get("NAME"),
        description=result.get("DESCRIPTION"),
        link=result.get("LINK"),
        homepage=result.get("HOMEPAGE"),
        tags=result.get("TAGS"),
    )
