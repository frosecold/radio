import schedule
import time
import os
from datetime import datetime

def run_script():
    os.system('python recorder.py')
    print(f"Recording started at {datetime.now()}")

# Schedule the `run_script` to run 1 minute before each hour from 10:00 to 17:00
hours = ['09:59', '10:59', '11:59', '12:59', '13:59', '14:59', '15:59', '16:59']
for hour in hours:
    schedule.every().monday.at(hour).do(run_script)
    schedule.every().tuesday.at(hour).do(run_script)
    schedule.every().wednesday.at(hour).do(run_script)
    schedule.every().thursday.at(hour).do(run_script)
    schedule.every().friday.at(hour).do(run_script)

print("Scheduler started. Waiting for scheduled times to record audio.")
while True:
    schedule.run_pending()
    time.sleep(1)
