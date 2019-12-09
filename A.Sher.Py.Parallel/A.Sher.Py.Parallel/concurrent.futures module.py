from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
    sleep(5)
    return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_5_secs, ("hello"))
print("Роботу закінчено?:", future.done())
sleep(5)
print("Роботу закінчено?:", future.done())
print("Результат:", future.result())
print("Роботу закінчено?:", future.done())