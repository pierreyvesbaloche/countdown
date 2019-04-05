## Context

You want to have a visual countdown for an upcoming crowdfunded project ?
Then search no more as this variation for Pimoroni's Scroll Bot (https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit) or Scroll pHAD HD (https://shop.pimoroni.com/products/scroll-phat-hd), allows you to set the deadline of the project, taking into account different timezones.

![Countdown](http://get.pimoroni.com/resources/github-repo-terminal.png)

You can then execute the python code like this :

```bash
python project-countdown.py --deadline "Wed, 10 Apr 2019 10:00:00" --my_timezone "Europe/Paris" --target_timezone "US/Eastern" 
```

## Documentation & Support

* Pimoroni Guides and tutorials - https://learn.pimoroni.com/scroll-phat-hd
* Base code line for Clock functions - https://github.com/pimoroni/scroll-phat-hd/blob/master/examples/clock.py