from client import Client
from threading import Thread
import time

c1 = Client("Aaditi")
time.sleep(3)
c2 = Client("Jane")
time.sleep(3)


def update_messages():
    msgs = []
    run = True
    while True:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break

Thread(target=update_messages).start()

c1.send_messages("Hello..")
time.sleep(3)
c2.send_messages("Hey")
time.sleep(3)  
c1.send_messages("What's up?")
time.sleep(3)  
c2.send_messages("Nothing much...")
time.sleep(3)

c1.disconnect()
time.sleep(3)
c2.disconnect()


