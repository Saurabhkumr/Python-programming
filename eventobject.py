import threading
import time

# Create an event object
event = threading.Event()

def task_with_timeout():
    print("Waiting for the event to be set.")
    # Wait for the event to be set, with a timeout of 3 seconds
    # event_set = event.wait(timeout=3)
    event_set = event.wait()
    if event_set:
        print("Event was set!")
    else:
        print("Timeout occurred, event was not set.")

# Create and start a thread
thread = threading.Thread(target=task_with_timeout)
thread.start()

# Sleep for 5 seconds (simulate delay)
time.sleep(5)

# Set the event after the delay
print("Setting the event now.")
event.set()

# Wait for the thread to finish
thread.join()
