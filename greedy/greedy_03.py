import time
start_time = time.time()

# Program source code
# input data with split space n, m, k
n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# Time check
end_time = time.time()
print("time: ", end_time - start_time)