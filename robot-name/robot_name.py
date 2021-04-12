import random
import string

all_robot_names = []

def generate_2_letters():
    # l = ""
    # for i in (0,1):
    #     l = l + random.choice(string.ascii_uppercase)
    # return l

    # return numpy.random.choice(string.ascii_uppercase, size=2, replace=False) #using numpy
    # return ''.join(random.choices(string.ascii_uppercase, k=2))
    return ''.join(random.choice(string.ascii_uppercase) for i in range(2)) # using join and range

def generate_3_numbers():
    # n = ""
    # for i in range(0,3):
    #     n = n + random.choice(string.digits)
    # return n

    # return ''.join(random.choices(string.digits, k=3))

    return ''.join(random.choice(string.digits) for i in range(3))

def is_unique(name):
    global all_robot_names
    if name in all_robot_names:
        return False
    else:
        return True

class Robot:

    def __init__(self):
        global all_robot_names
        self.name = generate_2_letters() + generate_3_numbers()
        while is_unique(self.name) == False:
            self.name = generate_2_letters() + generate_3_numbers()
        all_robot_names.append(self.name)
        
    def reset(self):
        global all_robot_names
        new_name = generate_2_letters() + generate_3_numbers()
        while is_unique(new_name) == False:
            new_name = generate_2_letters() + generate_3_numbers()
        all_robot_names.append(new_name)
        all_robot_names.remove(self.name)
        self.name = new_name

        

        