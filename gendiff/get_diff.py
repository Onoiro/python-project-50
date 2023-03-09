def get_diffs(data1, data2, level=1):
    diffs = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        node = {'name': key}
        if key not in data1:
            node['status'] = 'added'
            node['level'] = level
            node['data'] = data2[key]
        elif key not in data2:
            node['status'] = 'removed'
            node['level'] = level
            node['data'] = data1[key]
        elif type(data1[key]) is dict and type(data2[key]) is dict:
            node['status'] = 'nested'
            node['level'] = level
            node['children'] = get_diffs(data1[key], data2[key], level + 1)
        elif data1[key] == data2[key]:
            node['status'] = 'not updated'
            node['level'] = level
            node['data'] = data1[key]
        else:
            node['status'] = 'updated'
            node['level'] = level
            node['old data'] = data1[key]
            node['new data'] = data2[key]
        diffs.append(node)
    return diffs
