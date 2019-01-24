x = 5

if x < 0:
	print("X is smaller than 0.")
elif x > 10:
	print("X is bigger than 10.")
else:
	print("X is between 0 and 10.")


########
#y = int(input("enter value of y:"))

y=10
if y < 0:
	print("y is small.")
elif y >= 0:
	print("y is big.")
else:
	print("error")

######

animals  = ['cat','dog', 'turtle','bird']

print(animals)

for x in animals:
	print(x)
	print(len(x))

#numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = range(1,11)
#numbers = range(10)+1


for i in numbers:
	print((i+1)**2)

def complicated_function():
	pass

### In R
# complicated_function <- function() {
	
# }


def fib(n):
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    
         a, b = b, a+b
     return result

print(fib(2000))


print("\n")
print("\n")
print("\n")

a = 10/3
b = 3.3333333


if (a == b):
	print("hahaha")


stack = [ 1, 2, 3]

stack.append(5)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)


results = []
for i in range(10):
	results.append(i**2)

print(results)

results = list(map(lambda i:i**2, range(10)))
# def square(i):
# 	return i**2
print(results)

results = [i**2 for i in range(10)]

print(results)


fruit = {'apple','blackberry','banana','pear','pineapple','apple','peach','orange'}

print(fruit)

tech = {'apple','blackberry'}

print(fruit - tech)

#dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])














































