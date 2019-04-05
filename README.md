## Context

You want to have a visual countdown for an upcoming crowdfunded project ?
Then search no more as this variation for Pimoroni's Scroll Bot (https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit) or Scroll pHAD HD (https://shop.pimoroni.com/products/scroll-phat-hd), allows you to set the deadline of the project, taking into account different timezones.

![Countdown](https://github.com/pierreyvesbaloche/countdown/blob/master/resources/scroll-countdown.png)

## Execute

You can then run the python code like this :

```bash
python project-countdown.py --deadline "Wed, 10 Apr 2019 10:00:00" --my_timezone "Europe/Paris" --target_timezone "US/Eastern" 
```
* deadline : The date and time when the project is due.
* my_timezone : The timezone details for the calculation of the countdown.
* target_timezone : The timezone in which the dedline is expressed.

## Display
The following elements are being presented when the deadline is not reached yet:
* Hours & Minutes remaining
* Visual progress bar for the seconds
* Visual indication of days remaining :
  * by 3x1 blocks at the bottom, for at least 4 days 
  * by spaced 1 pixel blocks, on the last day

![Animated Countdown](https://github.com/pierreyvesbaloche/countdown/blob/master/resources/scroll-countdown.gif)

Once reached, a proper animation is replacing the countdown.

## Service configuration
If you'd wish to have this countdown automatically started when you power on your Scroll Bot, you can use the provided service template, in the scripts directory.

```bash
sudo cp scripts/countdown.service.template scripts/countdown.service
sudo cp scripts/countdown.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/countdown.service 
sudo pip3 install -r requirements.txt 
sudo systemctl daemon-reload
sudo systemctl enable countdown.service
sudo systemctl start countdown.service
```

## Extension

![Power SHIM](https://github.com/pierreyvesbaloche/countdown/blob/master/resources/onoff_shim.jpg)

As the Scroll Bot should be controllable easily when it comes to turning it ON or OFF, I would recommend to complete the hardware setup with Pimoronit's OnOff SHIM (https://shop.pimoroni.com/products/onoff-shim).

![Easy Access](https://github.com/pierreyvesbaloche/countdown/blob/master/resources/onoff_easy.jpg)

By doing so, you also "move" to the side the required power connection for the Scroll Bot, which I find much more efficient.

![Portable Scroll Bot](https://github.com/pierreyvesbaloche/countdown/blob/master/resources/onoff_portable.jpg)

## Documentation & Support

* Pimoroni Guides and tutorials - https://learn.pimoroni.com/scroll-phat-hd
* Base code line for Clock functions - https://github.com/pimoroni/scroll-phat-hd/blob/master/examples/clock.py