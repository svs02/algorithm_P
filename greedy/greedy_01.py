import time
start_time = time.time()

# Program source code

n = 1260

a = 0
b = 0
c = 0
d = 0

a = n // 500
n = n % 500

b = n // 100
n = n % 100

c = n // 50
n = n % 50

d = n // 10
n = n % 10

print("500원 {}개".format(a))
print("100원 {}개".format(b))
print("50원 {}개".format(c))
print("10원 {}개".format(d))

print("동전의 갯수는 {}개".format(a+b+c+d))

# Time check
end_time = time.time()
print("time: ", end_time - start_time)
