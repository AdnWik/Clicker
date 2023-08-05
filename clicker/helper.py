"""Read mouse position every two seconds"""
from pynput.mouse import Controller
from time import sleep

mouse = Controller()


while True:
    # Read pointer position
    print('The current pointer position is {0}'.format(mouse.position))
    sleep(2)
