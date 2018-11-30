import time,threading

def foo():
    print(time.ctime())
    threading.Timer(1,foo).start()

foo()
for i in range(10):
    print('hello')
    time.sleep(0.5)
