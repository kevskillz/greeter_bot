import cv2
import CONSTANTS





class Camera:



    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color):
        # Converting image to gray-scale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # detecting features in gray-scale image, returns coordinates, width and height of features
        features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        coords = []
        # drawing rectangle around the feature and labeling it
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            coords = [x, y, w, h]

        cv2.line(img, (int(CONSTANTS.MIDDLE_WIDTH + CONSTANTS.THRESHOLD_X), 0),
                 (int(CONSTANTS.MIDDLE_WIDTH + CONSTANTS.THRESHOLD_X), int(CONSTANTS.HEIGHT)), (0, 255, 0), 9)

        cv2.line(img, (int(CONSTANTS.MIDDLE_WIDTH - CONSTANTS.THRESHOLD_X), 0),
                 (int(CONSTANTS.MIDDLE_WIDTH - CONSTANTS.THRESHOLD_X), int(CONSTANTS.HEIGHT)), (0, 255, 0), 9)

        return coords

    def detect(self, img, faceCascade, mouthCascade):
        color = {"blue": (255, 0, 0), "white": (255, 255, 255)}
        coords = self.draw_boundary(img, faceCascade, 1.1, 10, color['blue'])
        # If feature is detected, the draw_boundary method will return the x,y coordinates and width and height of rectangle else the length of coords will be 0


        if len(coords) == 4:
            # Updating region of interest by cropping image
            roi_img = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
            # Passing roi, classifier, scaling factor, Minimum neighbours, color, label text


        return coords, img

    def __init__(self):
        # Loading classifiers
        self.faceCascade = cv2.CascadeClassifier('face_data.xml')
        self.mouthCascade = cv2.CascadeClassifier('mouth_data.xml')

        # Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
        self.video_capture = cv2.VideoCapture(0)

        # sets camera constants
        CONSTANTS.WIDTH = self.video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        CONSTANTS.HEIGHT = self.video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        CONSTANTS.MIDDLE_HEIGHT = CONSTANTS.HEIGHT / 2
        CONSTANTS.MIDDLE_WIDTH = CONSTANTS.WIDTH / 2
        CONSTANTS.THRESHOLD_X = CONSTANTS.WIDTH * CONSTANTS.OFFSET_MAX_PERCENT  # offset before off


    def get_img(self):
        return self.detect(self.video_capture.read()[1], self.faceCascade, self.mouthCascade)

    def __del__(self):
        # releasing web-cam
        self.video_capture.release()
        # Destroying output window
        cv2.destroyAllWindows()
