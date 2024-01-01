from PIL import Image
import math

def palette7Convert(image):
    palettedata = [0x00, 0x00, 0x00,
                   0xff, 0xff, 0xff,
                   0x00, 0xff, 0x00,
                   0x00, 0x00, 0xff,
                   0xff, 0x00, 0x00,
                   0xff, 0xff, 0x00,
                   0xff, 0x80, 0x00,
                  ]
    

    for i in range(0, 249 * 3):
        palettedata.append(0)

    p_img = Image.new('P', (600, 448))
    p_img.putpalette(palettedata)

    image = image.quantize(palette=p_img, dither=1)

    return image

def cutToSize(image, outLength, outHeight):
    
    length, height = image.size

    if length < height:
        image = image.rotate(90, expand=1)
    
    length, height = image.size

    ratio = length/outLength
    tempHeight = height/ratio

    image = image.resize((outLength, math.floor(tempHeight)))
    
    difference = tempHeight - outHeight
    
    partVal = abs(difference)/2

    bot = math.ceil(partVal)
    top = math.floor(partVal)
    
    if difference > 0:
        image = image.crop((0, top, outLength, tempHeight-bot))
        image = image.rotate(180, expand=1)

    elif difference < 0:
        tempImage = Image.new(image.mode, (outLength, outHeight), (255, 255, 255))
        tempImage.paste(image, (0, top))
        image = tempImage
    
    return image

def toBMP(input):

    image = Image.open(input).convert('RGB')

    return image

def saveImage(image, input, output=None):
    
    imgOut = output
    
    if output is None:
        slash = 0
        period = input.rindex(".")
        try:
            slash = input.rindex("/")+1
        except ValueError:
            pass

        imgOut = "output/"+input[slash:period]+".bmp"
    image.save(imgOut)

def convertFile(path):
    img = toBMP(path)
    img = cutToSize(img, 600, 448)
    img = palette7Convert(img)
    saveImage(img, path)

def main():
    path = ""
    convertFile(path)
    

    

if __name__ == "__main__":
    main()