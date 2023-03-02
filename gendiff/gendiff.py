def generate_diff(data1, data2, level=1):
    diffs = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        node = {'name': key}
        if key not in data1:
            node['status'] = 'added'
            node['data'] = data2[key]
            node['level'] = level
        elif key not in data2:
            node['status'] = 'removed'
            node['data'] = data1[key]
            node['level'] = level
        elif type(data1[key]) is dict and type(data2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = generate_diff(data1[key], data2[key], level + 1)
            node['level'] = level
        elif data1[key] == data2[key]:
            node['status'] = 'not updated'
            node['data'] = data1[key]
            node['level'] = level
        else:
            node['status'] = 'updated'
            node['old data'] = data1[key]
            node['new data'] = data2[key]
            node['level'] = level
        diffs.append(node)
    return diffs
