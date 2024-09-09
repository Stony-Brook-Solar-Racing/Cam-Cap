import cv2
import time
import datetime
from imutils import grab_contours
import json 
import os

fp = open("config.json")
config = json.load(fp)

# load in constants from json
CAP_FOLDER = config["capture_folder"]
REC_FOLDER = config["recordings_folder"]
FPS = config["fps"]
FRAME_SIZE = config["frame_size"]
MIN_AREA = config["min_area"]

class Capture:

    # 0 is the default camera port
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)

    def __init__(self) -> None:
        frame_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.camera.get(cv2.CAP_PROP_FPS)

        print(f'Camera Info ---------')
        print(f"Frame Width: {frame_width}")
        print(f"Frame Height: {frame_height}")
        print(f"FPS: {fps}")

# if ran as a python file
if __name__ == '__main__':
    cap = Capture()
    cap.record_motion()
