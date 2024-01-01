# Name:  Picture Frame Code
# Version: 0.2
# Description: This script will pull images from a folder 
#              and display it on the eink screen. 

#from waveshare_epd import epd5in65f
from waveshare_epd import epd5in65f
from PIL import Image
from os import listdir

try:
    imagefiles = [f for f in listdir("photos")]
    print(imagefiles)

    with open("currimage.txt","r") as f:
        line = f.readline()
        displayImage = ""
        if line:
            index = imagefiles.index(line)
            if index == len(imagefiles)-1:
                index = 0
            else:
                index = index + 1
            displayImage = imagefiles[index]
        else:
            displayImage = imagefiles[0]
        
    with open("currimage.txt","w") as f:
        f.write(displayImage)

    #Clear and set the WaveShare Display
    epd = epd5in65f.EPD()
    epd.init()
    epd.Clear()

    Himage = Image.open("photos/"+displayImage)
    epd.display(epd.getbuffer(Himage))
    epd5in65f.epdconfig.module_exit()


except IOError as e:
    pass