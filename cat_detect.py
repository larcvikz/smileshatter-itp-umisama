import cv2

def detect(cascadePath):

	ESC_KEY = 27
	INTERVAL = 33
	FRAME_RATE = 30

	ORG_WINDOW_NAME = "org"
	GAUSSIAN_WINDOW_NAME = "gaussian"

	DEVICE_ID = 0

	white = (0, 0, 255)

	# image = cv2.imread(imagePath)
	# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cap = cv2.VideoCapture(DEVICE_ID)

	end_flag, c_frame = cap.read()
	height, width, channels = c_frame.shape

	cv2.namedWindow(ORG_WINDOW_NAME)

	cascade = cv2.CascadeClassifier(cascadePath)

	while end_flag == True:

		image = c_frame
		image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		face_list = cascade.detectMultiScale(image_gray, minSize=(100, 100))

		for (x,y,w,h) in face_list:
			color = (0, 0, 255)
			pen_w = 3
			cv2.rectangle(c_frame, (x, y), (x + w, y + h), color, thickness = pen_w)

		cv2.imshow(ORG_WINDOW_NAME, c_frame)

		key = cv2.waitKey(INTERVAL)
		if key == ESC_KEY:
			break

		end_flag, c_frame = cap.read()

	cv2.destroyAllWindow()
	cap.release()


detect("cascade.xml")