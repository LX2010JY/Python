# import os
#
# #windows不能运行，这是unix的系统方法
# print('process (%s) start ....'% os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("I am child process(%s) and my parent is %s"%(os.getpid(),os.getpid()))
# else:
#     print("I (%s) just create a child process (%s)."%(os.getpid(),pid))

from multiprocessing import Process,Pool
import os,time,random

def long_time_task(name):
    print('Run task %s(%s)'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s Runs %2.f seconds"%(name,end-start))

def run_proc(name):
    print('Run child process %s(%s)...'%(name,os.getpid()))
if __name__ != '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print("child process will start.")
    p.start()
    #用于进程同步,join等待子进程结束，父进程才继续运行
    p.join()
    print('Child process stop')

if __name__ == '__main__':
    print("parent process %s."%os.getpid())
    #电脑四核，默认为四
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("waiting for all subprocess done...")
    #调用join之前，必须关闭close,关闭之后不能添加子进程
    p.close()
    p.join()
    print('All subprocess done')