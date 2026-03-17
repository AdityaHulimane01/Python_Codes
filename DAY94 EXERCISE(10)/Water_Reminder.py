import time
from plyer import notification

# Infinite loop -> reminder will keep running until you stop the program
while True:

    # Wait 1 hour (3600 seconds)
    time.sleep(3600)

    # Send desktop notification
    notification.notify(
        title="💧 Water Reminder",
        message="Time to drink water bro!",
        timeout=10  # notification will stay for 10 seconds
    )