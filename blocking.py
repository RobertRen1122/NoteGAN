# initialization
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
from PIL import Image
import cv2

def find_word(directory):
    resDict = pytesseract.image_to_boxes(Image.open(directory), lang='eng')
    return resDict

if __name__ == '__main__':
    # import the picture directory
    directory = "test.jpg"
    dict = find_word(directory).splitlines()
    #x, y, w, h
    # draw_rect(directory)
    image = cv2.imread(directory)
    hImg, wImg, _ = image.shape
    for x in range(len(dict)):
        dict[x] = dict[x].split(" ")
        start_point = (int(dict[x][1]), hImg - int(dict[x][2]))
        end_point = (int(dict[x][3]), hImg - int(dict[x][4]))
        thickness = 2
        color = (255, 0, 0)
        image = cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.imshow("hi", image)
    cv2.waitKey(0)
    cv2.destroyWindow("hi")
