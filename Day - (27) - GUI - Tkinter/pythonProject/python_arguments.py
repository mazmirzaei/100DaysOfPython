#### Python Argumens *


def foo(a, b=4, c=6):
    print(a, b, c)


foo(1)


################### Unlimited positional Argumnets   *args  ######################
# * means the function can accept any number of arguments


def add(*args):
    for n in args:
        print(n)


add(2, 4, 6, 8, 10)


#################################################################

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 2, 1, 7, 4, 3))


##################################################################

def test(*args):
    print(args)


test(1, 2, 3, 5)


######################################################################3##
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)


##################################### **kwargs  ###########################
# many key worded arguments


def cal(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)


# creates a dic
cal(add=3, multiply=4)


################ class example #####################3


class Car():

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')


my_car = Car(make='BMW')

print(my_car.model)
print(my_car.make)

