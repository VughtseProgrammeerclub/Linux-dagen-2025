import time
import sys
import random
width = 40
height = 20
screen = [" " * width for _ in range(height)]
def clear():
    sys.stdout.write("\033[H\033[J")
while True:
    new_line = "".join("|" if random.random() < 0.05 else " " for _ in range(width))
    screen.insert(0, new_line)
    screen.pop()
    clear()
    for line in screen:
        print(line)
        time.sleep(0.05)