import time

class Timer:
    
    def __init__(self, delay_interval, sleep_duration, working_hours_start=7.5, working_hours_end=17.5, off_hours_multiplier=2):
        self.delay_interval = delay_interval
        self.sleep_duration = sleep_duration
        self.working_hours_start = working_hours_start
        self.working_hours_end = working_hours_end
        self.off_hours_multiplier = off_hours_multiplier
        self.count = 0
        
    def pause(self):
        self.count += 1
        if self.count % self.delay_interval == 0:
            if self.is_working_hours():
                time.sleep(self.sleep_duration)
            else:
                time.sleep(self.sleep_duration * self.off_hours_multiplier)
    
    def is_working_hours(self):
        current_time = time.localtime(time.time()).tm_hour + time.localtime(time.time()).tm_min / 60
        return self.working_hours_start <= current_time <= self.working_hours_end
    
'''    
timer_instance = Timer(delay_interval=10, sleep_duration=2)

while True:
    print("Executing query...")
    timer_instance.pause()
'''
