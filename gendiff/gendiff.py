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
    return '{\n  ' + '\n  '.join(result) + '\n}'


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