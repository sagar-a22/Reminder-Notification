import time
from plyer import notification

if __name__ == "__main__":  
    while True:
        print("Sending notification...")
        notification.notify(
            title="Please drink water!!",
            message="Water is very necessary for the body since 60 percent of the body is made up of water.",
            app_icon="icon.ico",
            timeout=10
        )
        print("Notification sent.")
        time.sleep(5*5)