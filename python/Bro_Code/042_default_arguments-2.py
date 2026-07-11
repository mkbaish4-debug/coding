import time

def timer(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(0.1)
    print("Done!")

timer(10)
