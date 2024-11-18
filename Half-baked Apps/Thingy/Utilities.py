import threading as thrd
import time

class Timer:
    def __init__(self, period):
        self.running = False
        self.period = period
        self.__timer_thread = thrd.Thread(target = self.__timing)
        self.__pperiod = period
        self.__pause = False
        self.__stop = False

    def __timing(self):
        while self.__pperiod > 0:

            print(f"Timer is at second: {self.__pperiod}")
            if self.__pause is not True:
                self.__pperiod -= 1
            time.sleep(1)
            if self.__pperiod == 0:
                print("Ended!")
                self.running = False
                return
            if self.__stop is True:
                self.__stop = False
                return
        return

    def start_timer(self):
        self.__timer_thread.start()
        self.running = True

    def pause_timer(self):
        self.__pause = True
        self.running = False

    def resume_timer(self):
        self.__pause = False
        self.running = True

    def stop_timer(self):
        self.__stop = True
        self.running = False

if __name__ == "__main__":
    Timer1 = Timer(10)
    Timer1.start_timer()
    for i in range (1, 3):
        time.sleep(1)

    Timer1.pause_timer()

    for i in range (1, 3):
        time.sleep(1)

    Timer1.resume_timer()
    for i in range (1, 3):
        time.sleep(1)
    print(Timer1.running)
