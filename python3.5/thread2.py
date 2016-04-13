import time,threading

#多线程锁定执行完一个方法才能被打断
lock = threading.Lock()
balance = 0
def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n
def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)