import threading
import time


class Filozof(threading.Thread):
    def init(self, id, widelce):
        threading.Thread.init(self)
        self.id = id
        self.widelce = widelce

    def run(self):
        while True:
            time.sleep(1)
            print("Filozof", self.id, "myśli")
            self.widelce[self.id].acquire()
            self.widelce[(self.id + 1) % 5].acquire()
            print("Filozof", self.id, "je")

            self.widelce[self.id].release()
            self.widelce[(self.id + 1) % 5].release()

            if name == "main":
                widelce = [threading.Lock() for i in range(5)]
                filozofowie = [Filozof(i, widelce) for i in range(5)]
                for f in filozofowie:
                    f.start()