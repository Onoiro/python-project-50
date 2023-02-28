import json

def generate_diff(data1, data2):
    result = []
    for key_data1, value_data1 in data1.items():
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
    return '{\n  ' + '\n  '.join(result) + '\n}'


with open('file3.json') as f:
    data1 = json.load(f)
with open('file4.json') as f:
    data2 = json.load(f)
print(generate_diff(data1, data2))

'''print(generate_diff({
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  },
  {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }))'''
