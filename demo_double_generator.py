import time


def generator1(nb):
    i = 0
    while i < nb:
        yield i
        i+= 1
        time.sleep(1)

def generator2(nb):
    i = 0
    while i < nb:
        yield i / 10
        i+= 1
        time.sleep(1.1)

res1 = generator1(100)
res2 = generator2(50)
for tuple in zip(res1, res2):
    print(tuple)