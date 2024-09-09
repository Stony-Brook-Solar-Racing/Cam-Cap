import cv2

cam_port = 0
# https://docs.opencv.org/4.8.0/d8/dfe/classcv_1_1VideoCapture.html
cam = cv2.VideoCapture(cam_port)

def capture_frame():
    raise NotImplementedError()


if __name__ == "__main__":


# cv2.imwrite(os.path.join('caputres', time.strftime('%Y-%m-%d-%H-%M-%S-%z-capture.png')),
#         capture)
