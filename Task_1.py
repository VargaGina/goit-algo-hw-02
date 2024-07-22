from queue import Queue
import random
import time
 
queue = Queue()

def generate_request():
    id = random.randint(1, 1000)
    queue.put(id)
    print(f" {id} added ")

def process_request():
    if not queue.empty():
        id = queue.get()
        print(f"Processing  {id}")
    else:
        print("The queue is empty.")

def main():
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(3) 
    except KeyboardInterrupt:
        print("Exit")

if __name__ == "__main__":
    main()
