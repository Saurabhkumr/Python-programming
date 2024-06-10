# import threading
# import time

# # Semaphore with 3 permits
# semaphore = threading.Semaphore(3)

# def access_resource(thread_id):
#     with semaphore:
#         print(f"Thread {thread_id} accessing resource")
#         time.sleep(1)

# # Create multiple threads
# threads = []
# for i in range(10):
#     thread = threading.Thread(target=access_resource, args=(i,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()




import threading
import time

# Shared resource
counter = 0

# Lock object
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(5):
        # Acquire the lock
        lock.acquire()
        try:
            # Critical section
            print(f"{threading.current_thread().name} incrementing counter")
            counter += 1
            time.sleep(1)
        finally:
            # Release the lock
            lock.release()

# Create multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=increment_counter, name=f"Thread-{i}")
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
