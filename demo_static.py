class Counter:

    i = 0

    @staticmethod
    def increment():
        Counter.i += 1

Counter.increment()
c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
print(c1.i, c2.i)