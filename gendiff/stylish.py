def format_diff(diff_list, level=0):
    formatted_diff = '{\n'
    indent = '  '
    indent += '    ' * level
    for node in diff_list:
        if node['status'] == 'nested':
            level = node['level']
            data = format_diff(node['children'], level)
            formatted_diff += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'not updated':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'removed':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'updated':
            data = format_data(node['old data'], indent)
            formatted_diff += f"{indent}- {node['name']}: {data}\n"
            data = format_data(node['new data'], indent)
            formatted_diff += f"{indent}+ {node['name']}: {data}\n"
    formatted_diff += indent[:-2] + '}'
    return formatted_diff


def format_data(data, indent):
    if type(data) is dict:
        indent += '    '
        formatted_data = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            formatted_data += indent + '  ' + key + ': ' + value + '\n'
        formatted_data += indent[:-2] + '}'
    elif data is True:
        formatted_data = 'true'
    elif data is False:
        formatted_data = 'false'
    elif data is None:
        formatted_data = 'null'
    else:
        formatted_data = str(data)
    return formatted_data


def format_diff(diff_list, level=0):
    formatted_diff = '{\n'
    indent = '  '
    indent += '    ' * level
    for node in diff_list:
        if node['status'] == 'nested':
            level = node['level']
            data = format_diff(node['children'], level)
            formatted_diff += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'not updated':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}  {node['name']}: {data}\n"
        if node['status'] == 'added':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}+ {node['name']}: {data}\n"
        if node['status'] == 'removed':
            data = format_data(node['data'], indent)
            formatted_diff += f"{indent}- {node['name']}: {data}\n"
        if node['status'] == 'updated':
            data = format_data(node['old data'], indent)
            formatted_diff += f"{indent}- {node['name']}: {data}\n"
            data = format_data(node['new data'], indent)
            formatted_diff += f"{indent}+ {node['name']}: {data}\n"
    formatted_diff += indent[:-2] + '}'
    return formatted_diff


def format_data(data, indent):
    if type(data) is dict:
        indent += '    '
        formatted_data = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            formatted_data += indent + '  ' + key + ': ' + value + '\n'
        formatted_data += indent[:-2] + '}'
    elif data is True:
        formatted_data = 'true'
    elif data is False:
        formatted_data = 'false'
    elif data is None:
        formatted_data = 'null'
    else:
        formatted_data = str(data)
    return formatted_data
