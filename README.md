# lg-remote
Control a LG-TV over RS232 by using a Web-App hosted on a Raspberry Pi

##Requirements

- Python 2
    - Debian/Ubuntu Linux: `sudo apt-get install python`
- Python 3
    - Debian/Ubuntu Linux: `sudo apt-get install python3`
- The pyserial module
    -    Windows: http://pypi.python.org/pypi/pyserial
    -    Debian/Ubuntu Linux: `sudo apt-get install python-serial`

##Before you start ...

###Dialing out
Be sure you can dial out. If your serial device is ttyuSB0 you can chmod it:
`sudo chmod 666 /dev/ttyUSB0`

You can check your connection i.e. with screen or minicom:
`minicom -D /dev/ttyUSB0`
or
`screen /dev/ttyUSB0 9600 8N`

###Set the correct path in the code
There are a few things to change/set in the code. My examples based on a OSMC-Mediacenter-Distribution for Raspberry Pi.
####STARTwebserver.sh
- correct the path to `webserver.py`

####webserver.py
- correct the path to the `webdir`
- You can also change the `port` of the webserver. You should user for security purposes individual ports such as `8000` or `8080`. If you want to use Port `80` you have to run the startscript as root (not recommended).

####RemoteControl.py
- set the correct serial device at `serial_port`
- to disable cgi-debug-output (i.e. when exceptions are thrown) comment out the line `cgitb.enable()`

###Run the tv-server at startup
- Simply use cron. Let the `STARTwebserver.sh` run at startup.
Edit the cron-file:
`sudo nano /etc/crontab`
In `crontab` insert:
`@reboot <user_who_runs_the_script> /path/to/tvserver/STARTwebserver.sh`

##User-Interface
![](https://github.com/Einstein2150/lg-remote/blob/master/images/Screenshot.png)
###Screenshot

###Making a Web-App at the mobile
*comming soon ...*
##Setting up the correct buttons to your individual conditions

*comming soon ...*