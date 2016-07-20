import httplib 
import RPi.GPIO as GPIO
conn = httplib.HTTPConnection("45.79.151.162:8080")  
conn.request("GET", "/get.jsp") 
r1 = conn.getresponse()  
data = r1.read()
if (data.strip() is "1"):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12,0)
else:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12,1)
