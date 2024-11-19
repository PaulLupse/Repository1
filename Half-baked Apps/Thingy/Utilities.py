import threading as thrd
import time

class CDTimer:
    def __init__(self, period):
        self.running = False
        self.period = period
        self.__pperiod = period
        self.__pause = False
        self.__stop = False

    def __timing(self):
        while self.__pperiod > 0 and self.__stop is not True:
            if self.__pause is not True:
                self.__pperiod -= 0.01
                time.sleep(0.01)

        self.running = False
        self.__stop = False
        return

    def start_timer(self):
        thrd.Thread(target = self.__timing).start()
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

class Timer:
    def __init__(self):
        self.time_passed = 0
        self.running = False
        self.__stop = False
        self.__run = False

    def __timing(self):
        self.running = True
        while True:
            if self.__stop is True:
                break
            if self.__run is True:
                self.time_passed += 0.01
                time.sleep(0.01)
        return

    def start_timer(self):
        self.__run = True
        thrd.Thread(target = self.__timing).start()

    def pause_timer(self):
        self.__run = False
        self.running = False

    def resume_timer(self):
        self.__run = True
        self.running = True

    def stop_timer(self):
        self.__stop = True
        self.running = False

class StopWatch:
    def __init__(self):
        self.__start_time = 0
        self.__stop_time = 0
        self.time_passed = 0

    def start_timer(self):
        self.__start_time = time.time()

    def pause_timer(self):
        self.__stop_time = time.time()
        self.time_passed = self.__stop_time - self.__start_time

    def resume_timer(self):
        self.__start_time = time.time()

    def stop_timer(self):
        self.__stop_time = time.time()
        self.time_passed += self.__stop_time - self.__start_time

if __name__ == "__main__":
    Timer1 = StopWatch()
    Timer1.start_timer()
    time.sleep(1.234)
    Timer1.pause_timer()
    time.sleep(2)
    Timer1.resume_timer()
    time.sleep(3.141)
    Timer1.stop_timer()
    print(Timer1.time_passed)


