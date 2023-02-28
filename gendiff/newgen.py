import json

def generate_diff(data1, data2, level=1):
    result = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        node = {'name': key}
        if key not in data1:
            node ['level'] = level
            node['status'] = 'added'
            node['data'] = data2[key]
        elif key not in data2:
            node ['level'] = level
            node['status'] = 'deleted'
            node['data'] = data1[key]
        elif type(data1[key]) is dict and type(data2[key]) is dict:
            node ['level'] = level
            node['status'] = 'nested'
            node['children'] = generate_diff(data1[key], data2[key], level + 1)
        elif data1[key] == data2[key]:
            node ['level'] = level
            node['status'] = 'not changed'
            node['data'] = data1[key]
        else:
            node ['level'] = level
            node['status'] = 'changed'
            node['data before'] = data1[key]
            node['data after'] = data2[key]
        result.append(node)
    return result

'''for key_data1, value_data1 in data1.items():
    if key_data1 in data2:
        if data2[key_data1] == value_data1:
            result.append(f'  {key_data1}: {value_data1}')
        else:
            result.append(f'- {key_data1}: {value_data1}')
            result.append(f'+ {key_data1}: {data2[key_data1]}')
    else:
        result.append(f'- {key_data1}: {value_data1}')
for key_data2, value_data2 in data2.items():
    if key_data2 not in data1:
        result.append(f'+ {key_data2}: {value_data2}')
result = sorted(result, key=lambda i: i[2])
return '{\n  ' + '\n  '.join(result) + '\n}'''


with open('file3.json') as f:
    data1 = json.load(f)
with open('file4.json') as f:
    data2 = json.load(f)
print(generate_diff(data1, data2))