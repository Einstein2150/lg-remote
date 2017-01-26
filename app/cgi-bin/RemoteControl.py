#!/usr/bin/env python

import cgi
import cgitb

import sys

########Code aus dem ehemaligen LGTV.py#######################################
from libLGTV_serial import LGTV
 
model = '42LK450'                    # Change this to your TV's model
#serial_port = "/dev/ttyS0"
serial_port = "/dev/ttyUSB0"

tv = LGTV(model, serial_port)

# Example of adding a custom toggle command. Passing in '--toggleinput'
# will toggle between 'inputrgbpc' and 'inputdigitalcable'
tv.add_toggle('input', 'inputrgbpc', 'inputdigitalcable')

# Sometimes a single remote button press is detected as many. By debouncing a
# command, we make sure its only called once per button press.
tv.debounce('togglepower')

# Finally, send the command
# .send() Returns nothing on failure, 2-digit bytecode for status commands,
# and True for other commands

########Code aus dem ehemaligen LGTV.py-Ende#################################

cgitb.enable()
form=cgi.FieldStorage()

print('''
<!DOCTYPE html>
<html>
<head>
<br>
<title>Fernbedienung LG-TV</title>
<meta name="viewport" content="width=350"/>
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<link rel="apple-touch-icon" sizes="180x180" href="../icon/apple-touch-icon.png">
<link rel="icon" type="image/png" href="../icon/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="../icon/favicon-16x16.png" sizes="16x16">
<link rel="manifest" href="../icon/manifest.json">
<link rel="mask-icon" href="../icon/safari-pinned-tab.svg" color="#5bbad5">
<meta name="theme-color" content="#ffffff">
</head>
<body bgcolor="#1C1C1C">
<center>

<h1 style="font-family:verdana; font-size:80%; color: #A4A4A4">Fernbedienung LG-TV</h1>

<table style="width:90%; font-family:verdana; font-size:50%"; bgcolor="#A4A4A4">
<tr>
<td>
''')

#Statustabelle mit Ausfuehrung der Befehle

#initialisieren
commandkey = ""
returncode = ""

print("<b>Console: </b>")

#Befehl aus POST bearbeiten
if   "Submit_Power" in form:
    commandkey = "togglepower"
elif   "Submit_1" in form:
    commandkey = "key1"
elif "Submit_2" in form:
    commandkey = "key2"
elif "Submit_3" in form:
    commandkey = "key3"
elif "Submit_4" in form:
    commandkey = "key4"
elif "Submit_5" in form:
    commandkey = "key5"
elif "Submit_6" in form:
    commandkey = "key6"
elif "Submit_7" in form:
    commandkey = "key7"
elif "Submit_8" in form:
    commandkey = "key8"
elif "Submit_9" in form:
    commandkey = "key9"
elif "Submit_0" in form:
    commandkey = "key0"
elif "Submit_UP" in form:
    commandkey = "keyUP"
elif "Submit_PM" in form:
    commandkey = "keyPM"
elif "Submit_L" in form:
    commandkey = "keyL"
elif "Submit_OK" in form:
    commandkey = "keyOK"
elif "Submit_R" in form:
    commandkey = "keyR"
elif "Submit_PP" in form:
    commandkey = "keyPP"
elif "Submit_DOWN" in form:
    commandkey = "keyDOWN"
elif "Submit_Kabel" in form:
    commandkey = "inputdigitalantenna"
elif "Submit_HDMI" in form:
    commandkey = "inputhdmi3"
elif "Submit_BACK" in form:
    commandkey = "keyBACK"
elif "Submit_FAV" in form:
    commandkey = "keyFAV"
elif "Submit_Menu" in form:
    commandkey = "keyMenu"
elif "Submit_VM" in form:
    commandkey = "volumedown"
elif "Submit_VP" in form:
    commandkey = "volumeup"
elif "Submit_MUTE" in form:
    commandkey = "keyMUTE"
elif "Submit_KIKA" in form:
    commandkey = "KIKA"
elif "Submit_SRTL" in form:
    commandkey = "SRTL"
elif "Submit_DISNEY" in form:
    commandkey = "DISNEY"
elif "Submit_PRO7" in form:
    commandkey = "PRO7"
elif "Submit_RTL" in form:
    commandkey = "RTL"
elif "Submit_VOX" in form:
    commandkey = "VOX"
elif "Submit_ARDHD" in form:
    commandkey = "ARDHD"
elif "Submit_ZDFHD" in form:
    commandkey = "ZDFHD"
elif "Submit_ARTEHD" in form:
    commandkey = "ARTEHD"
elif "Submit_STATUS" in form:
    commandkey = ""

    #Power-Zustand Fernseher
    Status1 = str(tv.send("powerstatus"))

    #Umwandlung in lesbaren Wert
    Status1_codes = {
    '00'      : "aus",
    '01'      : "ein"
    }
    if Status1 in Status1_codes:
        Status1 = Status1_codes[Status1]

    #Lautstaerke ermitteln
    tv2 = LGTV(model, serial_port)
    Status2 = str(tv2.send("volumelevel"))

    #aktuellen Eingangskanal ermitteln
    tv3 = LGTV(model, serial_port)
    Status3 = str(tv3.send("inputstatus"))

    #Umwandlung in lesbaren Wert
    Status3_codes = {
    '00'      : "Antenne (Digital)",
    '01'      : "Kabel (Digital)",
    '10'      : "Antenne (Analog)",
    '11'      : "Kabel (Analog)",
    '20'      : "AV1",
    '21'      : "AV2",
    '40'      : "Component1",
    '41'      : "Component2",
    '42'      : "Component3",
    '60'      : "RGB-PC",
    '90'      : "HDMI1",
    '91'      : "HDMI2",
    '92'      : "HDMI3",
    '93'      : "HDMI4"
    }       
    if Status3 in Status3_codes:
        Status3 = Status3_codes[Status3]

    print("Power: " + Status1 + " - Volume: " + Status2 + " - Input: " + Status3)

#Beim ersten Aufruf ist kein Komando vorhanden. Sobald eine Taste gedrueckt wurde wird commandkey
#mit dem entsprechenden Befehl gefuellt und die Anwort in returncode geschrieben:
if commandkey != "":
    returncode = str(tv.send(commandkey))
    #Ausgabe vom Befehl gefolgt von der Geraeteantwort:
    print("Befehl: " + commandkey + " - Antwort: " + returncode)

#Schliessen der Statustabelle
print('''
</td>
</tr>
</table>
<br>
''')

#Beginn des Fernbedienungsformulars
print(''' 	
<form action="/cgi-bin/RemoteControl.py" method="POST">
                <input type="submit" value="TV" name="Submit_Kabel" style="height:25px; width:50px; background-color: #FE9A2E" />
		<input type="submit" value="Power" name="Submit_Power" style="height:35px; width:60px; background-color: #F78181" />
                <input type="submit" value="Media" name="Submit_HDMI" style="height:25px; width:50px; background-color: #FE9A2E" />
	<br> 
	<br>
		<input type="submit" value="P-" name="Submit_PM" style="height:40px; width:40px" />
		<input type="submit" value="&uarr;" name="Submit_UP" style="height:40px; width:80px; background-color: #A4A4A4" />
		<input type="submit" value="P+" name="Submit_PP" style="height:40px; width:40px" />
	<br>
		
                <input type="submit" value="&larr;" name="Submit_L" style="height:80px; width:40px; background-color: #A4A4A4" />
                <input type="submit" value="OK" name="Submit_OK" style="height:80px; width:80px; background-color: #A4A4A4" />	
                <input type="submit" value="&rarr;" name="Submit_R" style="height:80px; width:40px; background-color: #A4A4A4" />
	<br>
		<input type="submit" value="V-" name="Submit_VM" style="height:40px; width:40px" />
		<input type="submit" value="&darr;" name="Submit_DOWN" style="height:40px; width:80px; background-color: #A4A4A4" />
		<input type="submit" value="V+" name="Submit_VP" style="height:40px; width:40px" />
	<br>
                <input type="submit" value="Stumm" name="Submit_MUTE" style="height:25px; width:160px" />
        <br>
        <br>
                <input type="submit" value="KIKA" name="Submit_KIKA" style="height:25px; width:100px" />
                <input type="submit" value="SuperRTL" name="Submit_SRTL" style="height:25px; width:100px" />
                <input type="submit" value="Disney Ch." name="Submit_DISNEY" style="height:25px; width:100px" />
	<br>
                <input type="submit" value="Pro7" name="Submit_PRO7" style="height:25px; width:100px" />
                <input type="submit" value="RTL" name="Submit_RTL" style="height:25px; width:100px" />
                <input type="submit" value="VOX" name="Submit_VOX" style="height:25px; width:100px" />
	<br>
                <input type="submit" value="ARD HD" name="Submit_ARDHD" style="height:25px; width:100px" />
                <input type="submit" value="ZDF HD" name="Submit_ZDFHD" style="height:25px; width:100px" />
                <input type="submit" value="ARTE HD" name="Submit_ARTEHD" style="height:25px; width:100px" />
	<br>
	<br>
		<input type="submit" value="1" name="Submit_1" style="height:40px; width:40px" />
		<input type="submit" value="2" name="Submit_2" style="height:40px; width:40px" />
		<input type="submit" value="3" name="Submit_3" style="height:40px; width:40px" />
	<br> 
		<input type="submit" value="4" name="Submit_4" style="height:40px; width:40px" />
                <input type="submit" value="5" name="Submit_5" style="height:40px; width:40px" />
                <input type="submit" value="6" name="Submit_6" style="height:40px; width:40px" />
	<br> 
		<input type="submit" value="7" name="Submit_7" style="height:40px; width:40px" />
                <input type="submit" value="8" name="Submit_8" style="height:40px; width:40px" />
                <input type="submit" value="9" name="Submit_9" style="height:40px; width:40px" />
	<br> 
		<input type="submit" value="0" name="Submit_0" style="height:40px; width:40px" />
	<br>
        <br> 
                <input type="submit" value="back" name="Submit_BACK" style="height:25px; width:80px" />
                <input type="submit" value="FAV" name="Submit_FAV" style="height:25px; width:80px" />
                <input type="submit" value="Menu" name="Submit_Menu" style="height:25px; width:80px" />
        <br> 
                <input type="submit" value="Status" name="Submit_STATUS" style="height:25px; width:80px; background-color: #FE9A2E" />
        <br> 
</form>

<p style="font-family:verdana; font-size:60%; color: #A4A4A4">program and design<br>&copy; by Raik Schneider<br><a href="../Changelog.html" target="_blank">Version 2.2</a></p>
</center>
 
</body>
</html> 
''')
