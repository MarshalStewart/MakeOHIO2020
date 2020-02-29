import RPi.GPIO as GPIO
from SerLCD import SerLCD

class LCD:
	def __init__(self):
		# Declare Variables
		self.RXPIN = 2
		self.SerLCD = SerLCD()

		# Set Pin Names
		GPIO.setmode(GPIO.BOARD)
		
		# Set Pin IDs
		GPIO.setup(self.RXPIN, GPIO.OUT)
		return

	def sendString(self, message):
		self.SerLCD.write(message)


# Testing
if __name__ == "__main__":
	lcd = LCD()
	lcd.sendString("Hello, World")





