def f(x):
    return x * 2

print(f(2))
len("Monty")
len("Python")
str(100)
int("1")
float(100)


def f(x):
    return x ** 2

def printString(x):
    print(x)

def multipleParameters(x, y = 1, z = 2):
    print(x)
    print(y)
    print(z)

fruit = list()
fruit

fruit = []
fruit

fruit = ["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print(fruit)

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

print(fruit[0])
print(fruit[1])
print(fruit[2])
popped = fruit.pop()
print(fruit)
print(popped)
empty_list = list()
#popped = empty_list.pop()
fruit += random
print(fruit)
truth_var = "Apple" in fruit
print(truth_var)
truth_var = "Bondonoo" in fruit
print(truth_var)
print(len(fruit))