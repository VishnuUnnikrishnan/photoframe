# Open Source Digital Eink Photo Frame

Digital Photo Frames are traditionally made of LCD panels and the software is closed source. With the advent of colour e-ink displays, this gives us the oppotunity to build our own photoframe with E-Ink Displays and Open Source software and teh Raspberry Pi 0w.

## Installation
1. Install Pillow:
   - pip install Pillow
  
2. Download the waveshare eink libraries for python from this location. Just copy it into the folder where the application will sit.
   - https://github.com/waveshareteam/e-Paper/tree/master/RaspberryPi_JetsonNano/python/lib/waveshare_epd

3. Copy all of the files to a local directory on your Raspberry Pi 0w. We recommend that you use the one below, otherwise change every : 
   - "/home/pi/PhotoFrame"

4. Make the bash scripts executable
   - chmod +x photoframe.sh
   - chmod +x eink_shutdown.sh
  
5. Create the cronjob to run the script every hour.
   - 0 * * * * /home/pi/PhotoFrame/photoframe.sh
  
Your final directory structure should look like this:

![directory](https://github.com/VishnuUnnikrishnan/photoframe/assets/14148289/69c497ee-85d8-4b7c-9772-d459c66eaec8)

  
## Convert a Photo for display

Converting a photo to be displayed is easy. Upload the file to the rspberry pi and then run the following command.

- python converter.py "PATH TO FILE"

This will modify the file to be able to be displayed on the eink screen. If the format it incorrect the file will not be displayed and the program will crash.

For More Information: [Blog](https://blog.v1shnu.com/build-a-better-digital-photo-frame)




