import time
def func():
    time.sleep(100)
    with open('/tmp/test_func.txt','w') as f:
        print(f.write("5"))
