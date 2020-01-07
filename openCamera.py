import cv2


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (imgHeight, imgWidth) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(imgHeight)
        dim = (int(imgWidth * r), height)
    else:
        r = width / float(imgWidth)
        dim = (width, int(imgHeight * r))

    return cv2.resize(image, dim, interpolation=inter)


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('test.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
resize = ResizeWithAspectRatio(img, height=1024)
cv2.imshow('Face Detection', resize)
cv2.waitKey()
