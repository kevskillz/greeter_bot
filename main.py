from camera import Camera
#
import cv2

from AudioToText import AudioToText
import threading
import os
import CONSTANTS
import pyttsx3
from Motor import StepMotor
import time

cam = Camera()

print(CONSTANTS.WIDTH)
print(CONSTANTS.HEIGHT)

print(CONSTANTS.MIDDLE_WIDTH - CONSTANTS.THRESHOLD_X)
print(CONSTANTS.MIDDLE_WIDTH + CONSTANTS.THRESHOLD_X)

motor = StepMotor()


def get_center(coords):
    x = coords[0]
    w = coords[2]

    return x + (w / 2)


def get_img():
    if cv2.waitKey(1) & 0xFF == ord('q'):
        os._exit(1)

    coords, image = cam.get_img()

    cv2.imshow("face detection", image)
    if len(coords) > 0:
        x = get_center(coords)
        print("Center: ", x)
        if not (CONSTANTS.MIDDLE_WIDTH - CONSTANTS.THRESHOLD_X < x < CONSTANTS.MIDDLE_WIDTH + CONSTANTS.THRESHOLD_X):  # if x not in between threshold values
            move_dist_pixels = CONSTANTS.MIDDLE_WIDTH - x
            print("MOVE: ", move_dist_pixels)
            return move_dist_pixels

    return 0





def move_motor():
    motor.start_motor()
    while True:
        print(motor.step(get_img()))




def get_audio():
    while True:
        tts = pyttsx3.init()

        speak = AudioToText()

        resp = speak.get_text()

        if resp != "":
            def onEnd(name, completed):
                tts.stop()
                del tts

            tts.connect("finished-utterance", onEnd)
            tts.say(resp)
            tts.runAndWait()

        print("done speaking")


def main():
    t1 = threading.Thread(target=get_audio, name='t1')
    t2 = threading.Thread(target=move_motor, name='t2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()


main()
