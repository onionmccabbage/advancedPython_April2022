from multiprocessing import Process, current_process
import os # this can tell us how many processors we have

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    def run(self): # we override the built in run method of Process
        print('Child process ID is {}'.format(current_process().pid)) # get the unique process ID

def main():
    print('Main process ID is {}'.format(current_process().pid))
    myProcess = MyProcess()
    myProcess.start()
    myProcess.join()
    # a bunch of child process
    processes = []
    for i in range(os.cpu_count()):
        proc = MyProcess()
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()