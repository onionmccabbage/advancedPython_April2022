from multiprocessing import Process

def myProcFn():
    print('Executing a child process (with its own GIL)')

def main():
    print('Executing the main process')
    myProc2 = Process( target=myProcFn() )
    myProc2.start()
    myProc2.join()
    myProc3 = Process( target=myProcFn() )
    myProc3.start()
    myProc3.join()
    print('child process has terminated')

if __name__ == '__main__':
    main()