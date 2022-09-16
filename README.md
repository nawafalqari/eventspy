# EventsPy
Events in Python

Example:
```python
from threading import Thread
import eventspy

events = eventspy.EventsHandler()

@events.on('message')
def messageEvent(data):
   print(f"{data['name']}> {data['message']}")

@events.on("quit")
def quitEvent(data):
   print(f"{data['name']}> quit!")
   exit()

def terminal():
   while True:
      cmd = input("> ")
      if cmd == "quit":
         events.send("quit", {"name": "Nawaf"})
      else:
         events.send("message", {"name":"Nawaf", "message": cmd})

thread = Thread(target=terminal, daemon=True)
thread.start()

events.listen()
```