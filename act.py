from pygame import mixer
from time import sleep
import random
import os

mixer.init()

# mixer.music.load("sounds/test.mp3")
# mixer.music.play()
# number = random.randint(6, 12)

sound_list = os.listdir("sounds")

while True:

    print("============GO===========")
    random_sound = random.choice(sound_list)
    print(f"random sound is {random_sound}")
    mixer.music.load(f"sounds/{random_sound}")
    print("playing sound...")
    mixer.music.play()
    wait_time = random.randint(3,10)
    print(f"waiting {wait_time} seconds...")
    sleep(wait_time)
    print("===========DONE==========")

