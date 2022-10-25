print("Hello World")

potato = 'This is my variable'
print (potato)

def peel_potato(num1, num2):
    return num1 + num2

def floor_potato(num1, num2):
    return num1 // num2
def divide_potato(num1, num2):
    return num1 / num2
print(divide_potato(15, 2))
print(floor_potato(15, 2)) # Should print 7

print(peel_potato(3 , 10))

def double_potato(num):
    return num**2
print(double_potato(5))

list_of_numbers = range(0, 10, 2)
print(list_of_numbers)
print(list_of_numbers[2])

print(range(5)[2])

print(range(0, 10)[4])

i = 5
while(i):
    print(i)
    i -= 1

print('mod')
print(3 % 2)

class Car:
    def __init__(self, input_model):
        self.model = input_model
        self.mileage = 0
        self.oilLevel = 6000

    def vroom(self, distance):
        self.mileage += distance
        self.oilLevel = self.oilLevel - distance

    def oilChange(self):
        self.oilLevel = 6000

    def __str__(self):
        return f"Hello, I am a {self.model} and I have traveled {self.mileage} miles and I need an oil change in {self.oilLevel} miles"

myCar = Car('Buick')
print('Obj' , myCar)
print('Model', myCar.model)
print('Mileage', myCar.mileage)
print('Oil', myCar.oilLevel)
myCar.vroom(25232)
print(myCar)
print('Oil', myCar.oilLevel)
print('Mileage', myCar.mileage)
myCar.oilChange()
print('Oil', myCar.oilLevel)
print(myCar)

naodCar = Car('Tayota')
print(naodCar.mileage)
print(naodCar.model)

class prompt:
    def __init__(self):
        self.text = input('Text: ')
        self.name = input('Name: ')
    def __str__(self):
        return f"{self.name} is doing {self.text}"

fun = prompt()
print(fun)

new_one = prompt()
print(new_one)