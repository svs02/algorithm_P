from dis import code_info
import time
start_time = time.time()

# Program source code



n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)

# Time check
end_time = time.time()
print("time: ", end_time - start_time)
