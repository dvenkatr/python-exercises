kv = {
    'black' : 0,
    'brown' : 1,
    'red'   : 2,
    'orange': 3,
    'yellow': 4,
    'green' : 5,
    'blue'  : 6,
    'violet': 7,
    'grey'  : 8,
    'white' : 9
}
    
def color_code(color):
    return kv[color]

def colors():
    return list(kv.keys())

# print(kv.keys) 
# <built-in method keys of dict object at 0x100e10100>

# print(kv.keys()) 
# dict_keys(['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'])

# print(list(kv.keys())) 
# ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

# print(list(kv.values())) 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(kv.items())) 
# [('black', 0), ('brown', 1), ('red', 2), ('orange', 3), ('yellow', 4), ('green', 5), ('blue', 6), ('violet', 7), ('grey', 8), ('white', 9)]
