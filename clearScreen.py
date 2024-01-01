from waveshare_epd import epd5in65f

try:
    epd = epd5in65f.EPD()
    epd.init()
    epd.Clear()
    epd5in65f.epdconfig.module_exit()

except IOError as e:
    pass