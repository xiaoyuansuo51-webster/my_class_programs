from cImage import *
GREEN_RANGE_MIN_HSV = (100, 80, 70)
GREEN_RANGE_MAX_HSV = (185, 255, 255)

#1.) Convert green pixels to transparency.
# Basically uses a filtering rule in the HSV color space.
def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v

def cleargreen(oldPixel):
    min_h, min_s, min_v = GREEN_RANGE_MIN_HSV
    max_h, max_s, max_v = GREEN_RANGE_MAX_HSV
    r = oldPixel.getRed()
    g = oldPixel.getGreen()
    b = oldPixel.getBlue()
    h_ratio, s_ratio, v_ratio = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    h, s, v = (h_ratio * 360, s_ratio * 255, v_ratio * 255)
    if min_h <= h <= max_h and \
        min_s <= s <= max_s and min_v <= v <= max_v:
    # if oldPixel.getGreen() > 150 and oldPixel.getRed() < 30\
    #         and oldPixel.getBlue() < 30:
        newgreen = 255
        newred = 255
        newblue = 255
    else:
        newgreen = oldPixel.getGreen()
        newred = oldPixel.getRed()
        newblue = oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel

def change(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("change Image", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)
    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col, row)
            #newPixel = clearRed(oldPixel)
            newPixel = cleargreen(oldPixel)
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

def clearRed(oldPixel):
    if oldPixel.getRed() > 250:
        newred = 0
    else:
        newred = oldPixel.getRed()
    newgreen = oldPixel.getGreen()
    newblue = oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel
    # for row in range(height):
    #     for col in range(width):
    #         oldPixel = oldImage.getPixel(col, row)
    #         newPixel = changePixel(oldPixel)
    #         newIm.setPixel(col, row, newPixel)



if __name__ == '__main__':
    change("green.jpeg")