import time

import Utilities.Utilities as Utils

<<<<<<< Updated upstream
import Utilities as Utils

Timer1 = Utils.Timer()

=======
Timer1 = Utils.StopWatch()
Timer1.pause_timer()
Timer1.start_timer()
Timer1.resume_timer()
while Timer1.running is not True:
    pass
time.sleep(5.5)
Timer1.stop_timer()
print(round(Timer1.time_passed, 3))
>>>>>>> Stashed changes
