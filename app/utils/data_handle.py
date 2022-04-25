import re


def replace_str(data: str, pattern: str, replace_value):
    """检索目标字符串中的标签，并进行替换"""
    var_list = re.findall(pattern, data, flags=0)
    for i in var_list:
        _old = i
        _new = str(replace_value)
        data = data.replace(_old, _new)
    return data
