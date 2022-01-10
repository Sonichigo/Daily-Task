from plyer import notification
import time

def reminder():
    notification.notify(title = "Submission reminder", message="Time is near please submit the hackathon Project",timeout = 1)

while True:
    reminder()
    time.sleep(345600)
