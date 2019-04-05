
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import datetime
import pytz
import math
import time
import signal
import scrollphathd
from scrollphathd.fonts import font3x5

# Handle the argument passing
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--deadline", required=True, help="The project's deadline full date")
ap.add_argument("-mt", "--my_timezone", required=True, help="My own timezone")
ap.add_argument("-tt", "--target_timezone", required=True, help="The project's timezone")
args = vars(ap.parse_args())

# Required as the Pimoroni Scroll Bot display is upside down
scrollphathd.rotate(degrees=180)

# Brightness of the seconds bar and text
BRIGHTNESS = 0.3

ROW_DAYS = 6
DAYS_MAX = 4
DAY_1 = [0,1,2]
DAY_2 = [4,5,6]
DAY_3 = [10,11,12]
DAY_4 = [14,15,16]
DAYS = [DAY_1, DAY_2, DAY_3, DAY_4]

# Calculate the proper date with TimeZone
MY_ZONE = args["my_timezone"]       # "Europe/Paris"                    # <------- CHANGE HERE FOR YOUR OWN TIMEZONE
KS_ZONE = args["target_timezone"]   # "US/Eastern"                      # <------- PROJECT TIMEZONE
KS_START = args["deadline"]         # "Wed, 10 Apr 2019 10:00:00"       # <------- OPENING TIME

my_timez = pytz.timezone(MY_ZONE)
target_timez = pytz.timezone(KS_ZONE)
target = KS_START
date_start = datetime.datetime.strptime(target, '%a, %d %b %Y %H:%M:%S')
date_project = target_timez.localize(date_start)
date_my = date_project.astimezone(my_timez)

print("-------------------------")
print("- COUNTDOWN TO KS START -")
print("-------------------------")
print("{} Deadline: {}".format(KS_ZONE, date_project))
print("{} Deadline: {}".format(MY_ZONE, date_my))
print("-------------------------")

try:
    while True:
        date_now = datetime.datetime.now()

        # The deadline is still to come ...
        # =================================
        if date_start > date_now:
            # Calculate the remaining time before the KS opening
            pyis_target = date_start - date_now
            pyis_countdown = str(pyis_target).split(".")[0]
            # print("{}".format(pyis_countdown))                        # <------- UNCOMMENT TO SEE COUNTDOWN
            timeframe = pyis_countdown.split(" ")
            if len(timeframe) > 1:
                pyis_countdown_days = int(timeframe[0])
                pyis_countdown_time = timeframe[2]
            else:
                pyis_countdown_days = 0
                pyis_countdown_time = timeframe[0]

            scrollphathd.set_brightness(0.5)
            scrollphathd.clear()

            # Display the time (HH:MM) in a 3x5 pixel font
            hours = pyis_target.seconds // 3600
            minutes = (pyis_target.seconds % 3600) // 60
            seconds = pyis_target.seconds % 60
            scrollphathd.write_string(
                "{:02d}:{:02d}".format(hours, minutes), # Display the countdown
                x=0,                                    # Align to the left of the buffer
                y=0,                                    # Align to the top of the buffer
                font=font3x5,                           # Use the font5x5 font we imported above
                brightness=BRIGHTNESS                   # Use our global brightness value
            )

            # Display the seconds reamining as a timeline under
            float_sec = seconds / 59.0
            seconds_progress = float_sec * 15
            for y in range(15):
                # For each pixel, we figure out its brightness by
                # seeing how much of "seconds_progress" is left to draw
                # If it's greater than 1 (full brightness) then we just display 1.
                current_pixel = min(seconds_progress, 1)
                # Multiply the pixel brightness (0.0 to 1.0) by our global brightness value
                scrollphathd.set_pixel(y + 1, 5, current_pixel * BRIGHTNESS)
                # Subtract 1 now we've drawn that pixel
                seconds_progress -= 1
                # If we reach or pass 0, there are no more pixels left to draw
                if seconds_progress <= 0:
                    break

            # Show the number of days until the Start with...
            for day in range(DAYS_MAX):
                # Blocks of 3 pixels by full day remaining (max. 4 days)
                if pyis_countdown_days > 0:
                    if day < pyis_countdown_days:
                        for pixels in DAYS[day]:
                            scrollphathd.set_pixel(pixels, ROW_DAYS, BRIGHTNESS)
                    else:
                        for pixels in DAYS[day]:
                            scrollphathd.set_pixel(pixels, ROW_DAYS, 0)
                else:
                # Single alternated pixel line on the last day
                    for pixel in range(17):
                        if pixel % 2 == 0:
                            scrollphathd.set_pixel(pixel, ROW_DAYS, BRIGHTNESS)
                        else:
                            scrollphathd.set_pixel(pixel, ROW_DAYS, 0)

            # Do the 'Clock' Ticking 
            if int(pyis_target.seconds) % 2 == 0:
                scrollphathd.clear_rect(8, 0, 1, 5)

        # The deadline has passed !! Let's show it !!
        # ===========================================
        else:
            t = time.time() * 10
            for x in range(17):
                for y in range(7):
                    b = math.sin(x + y + t) + math.cos(x + y + t)
                    b = (b + 2) / 4
                    scrollphathd.set_pixel(x, y, b)

        # Set the screen
        scrollphathd.show()
        time.sleep(0.05)

except (KeyboardInterrupt, SystemExit):
    print("Bye Bye ...")
except:
    raise