class Counter:

    i = 0 # Static = Shared

    @staticmethod
    def increment():
        Counter.i+=1

Counter.increment()
Counter.increment()
print(Counter.i)