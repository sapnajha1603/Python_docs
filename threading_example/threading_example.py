import threading
import time
def execute_task(seconds):
    print(f"The function is sleeping for {seconds} seconds")
    time.sleep(seconds)
current_time = time.time()
# execute_task(4)
# execute_task(3)
# execute_task(2)
t1 = threading.Thread(target = execute_task, args = [4])
t2 = threading.Thread(target = execute_task, args = [3])
t3 = threading.Thread(target = execute_task, args = [2])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(f"The total time taken by normal operation is : {time.time() - current_time}")