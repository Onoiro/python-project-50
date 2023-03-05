def get_plain(diff_list):
    plain_result = get_plain_diff(diff_list)
    return '\n'.join(plain_result)


def get_plain_diff(diff_list, path=''):
    formatted_diff = []
    for node in diff_list:
        if node['status'] == 'nested':
            path_to_diff = path + node['name'] + '.'
            diff = get_plain_diff(node['children'], path_to_diff)
            formatted_diff.extend(diff)
        if node['status'] == 'added':
            path_to_diff = path + node['name']
            change = format_data(node['data'])
            diff = (
                f"Property '{path_to_diff}' was added "
                f"with value: {change}"
            )
            formatted_diff.append(diff)
        if node['status'] == 'removed':
            path_to_diff = path + node['name']
            change = format_data(node['data'])
            diff = f"Property '{path_to_diff}' was removed"
            formatted_diff.append(diff)
        if node['status'] == 'updated':
            path_to_diff = path + node['name']
            change_before = format_data(node['old data'])
            change_after = format_data(node['new data'])
            diff = (
                f"Property '{path_to_diff}' was updated. "
                f"From {change_before} to {change_after}"
            )
            formatted_diff.append(diff)
    return formatted_diff


def format_data(data):
    if type(data) is dict or type(data) is list:
        formatted_data = '[complex value]'
    elif data is False:
        formatted_data = 'false'
    elif data is True:
        formatted_data = 'true'
    elif data is None:
        formatted_data = 'null'
    elif type(data) is str:
        formatted_data = f"'{data}'"
    else:
        formatted_data = f'{data}'
    return formatted_data
