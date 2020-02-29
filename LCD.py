import RPi.GPIO as GPIO


class LCD:
	def __init__(self):
		
		# Declare Variables
		self.RXPIN = 2

		# Set Pin Names
		GPIO.setmode(GPIO.BOARD)
		
		# Set Pin IDs
		GPIO.setup(self.RXPIN, GPIO.OUT)		
 
		return

	
# Testing
if __name__ == "__main__":
	lcd = LCD()

	



