def get_diffs(data1, data2):
    diffs = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        node = {'name': key}
        if key not in data1:
            node['status'] = 'added'
            node['data'] = data2[key]
        elif key not in data2:
            node['status'] = 'removed'
            node['data'] = data1[key]
        elif type(data1[key]) is dict and type(data2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = get_diffs(data1[key], data2[key])
        elif data1[key] == data2[key]:
            node['status'] = 'not updated'
            node['data'] = data1[key]
        else:
            node['status'] = 'updated'
            node['old data'] = data1[key]
            node['new data'] = data2[key]
        diffs.append(node)
    return diffs
