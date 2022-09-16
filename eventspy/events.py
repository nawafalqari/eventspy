from threading import Event, Thread
from time import sleep
from typing import Any

class EventsHandler:
   def __init__(self):
      self.listeners = {}

   def on(self, name:str):
      def decorator(func):
         self._registerEvent(name, func)
         return func
      
      return decorator

   def _registerEvent(self, name:str, func):
      self.listeners[name] = {
         "func": func,
         "event": Event()
      }

   def send(self, eventName:str, data:Any=None):
      listener = self.listeners.get(eventName)
      if not listener:
         raise Exception("Invalid event name")

      event = listener["event"]

      event.set()
      event.data = data or None

   def listen(self, threaded:bool=False, daemonThread:bool=False, tickDelay:float=0.1):
      if threaded:
         def job():
            while True:
               for listener in self.listeners:
                  event:Event = listener["event"]
                  func = listener["func"]
                  if event.is_set():
                     func(None if not hasattr(event, "data") else event.data)
                     event.clear()

               sleep(tickDelay)
               
         thread = Thread(target=job, name="EventsPy", daemon=daemonThread)
         thread.start()

      else:
         while True:
            for listenerName, listener in self.listeners.items():
               event:Event = listener["event"]
               func = listener["func"]
               if event.is_set():
                  func(None if not hasattr(event, "data") else event.data)
                  event.clear()
            sleep(tickDelay)