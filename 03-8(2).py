import random

n = random.randint(0, 100)
a = [random.randint(0, 100) for _ in range(n)]

a.sort(reverse=True)

for i in a:
    print(i)
