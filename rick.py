import time
import thumby
import math
import time

# video = open("/Games/VideoPlayer/video.raw", 'rb')
video = open("/video.raw", 'rb')

while(1):
    for frameIndex in range(0, 71, 1):
        frame = video.read(360)
        thumby.display.fill(0)
        thumby.display.blit(bytearray(frame), 0, 0, 72, 40, 0, 0, 0)
        thumby.display.update()
        time.sleep_ms(17)
    video.seek(0)
