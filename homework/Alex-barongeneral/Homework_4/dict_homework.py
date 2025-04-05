my_dict = {
    'tuple': (10, 20, 30, 40, 50),
    'list': ['python1', 'python2', 'python3', 'python4', 'python5'],
    'dict': {
        'Imya': 'Alex',
        'Vozrast': 23,
        'Gorod': 'orlandoBlum',
        'Zanatie': 'python_codding',
        'Yazik': 'Python'
    },
    'set': {228, 229, 400, 500, 9001, 700}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('python6')
del my_dict['list'][1]

my_dict['dict'][('i am a tuple', )] = 'tuple key'
my_dict['dict'].pop('Imya')


my_dict['set'].add(600)
my_dict['set'].discard(200)

print(my_dict)
