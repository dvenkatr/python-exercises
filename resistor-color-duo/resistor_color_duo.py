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

def value(colors):
    print(colors[0], colors[1])
    print(kv[colors[0]], kv[colors[1]])
    print(str(kv[colors[0]]), str(kv[colors[1]]))
    print(str(kv[colors[0]]) + str(kv[colors[1]]))
    print (int(str(kv[colors[0]]) + str(kv[colors[1]])))
    
    return int((str(kv[colors[0]]) + str(kv[colors[1]])))
