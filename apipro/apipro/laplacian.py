import cv2


def variance_of_laplacian(img, threshold):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    # return cv2.Laplacian(image, cv2.CV_64F).var()
    # construct the argument parse and parse the arguments

    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    image = cv2.imread(cv2.samples.findFile(img), cv2.IMREAD_COLOR)
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    # image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    text = "Not Blurry"
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < threshold:
        text = "Blurry"
    # show the image
    # cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    # cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Image", image)
    key = cv2.waitKey(0)
    return text
# variance_of_laplacian(r'C:\Users\Mahdi\Desktop\blurImages\3.jpg',100)