import time
def func():
    time.sleep(100)
    with open('/v3io/users/shapira/Varonish/archive/test.txt','r') as f:
        print(f.readlines())
