import random
import time
import sys

countdown_duration = 50

initial_interval = 0.01 

final_interval = 0.2  

interval_step = (initial_interval - final_interval) / countdown_duration

print("Rolling the dice..")

for i in range(countdown_duration, 0, -1):
    
    dice_roll = random.randint(1, 6)
    
    sys.stdout.write("\r" + "Rolling... " + str(dice_roll))
    sys.stdout.flush()

    initial_interval -= interval_step

    time.sleep(initial_interval)

print("\r" + "The dice rolls to: " + str(dice_roll))
