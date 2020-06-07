try:
    import Image

except ImportError:
	from PIL import Image

import pyscreenshot as ImageGrab
import pytesseract
import pyttsx3
import time

engine = pyttsx3.init()

#up = (18711, (255, 255, 255)), (3, (253, 253, 253)),
#not up = [(21350, (32, 33, 36)), (1400, (17, 17, 17))]

oldMsg = ""
muted = False

while True:
	chatMessage = ImageGrab.grab(bbox = (1000, 630, 1325, 700))

	try:
		if chatMessage is not None and chatMessage.getcolors()[0][1][0] == 255 and chatMessage.getcolors()[0][1][1] == 255 and chatMessage.getcolors()[0][1][2] == 255:
			text = pytesseract.image_to_string(chatMessage)
			
			if "Turn on cantions Dracent now" not in text and text != "":
				if ("\n" in text):
					text = text[text.find("\n"):]
				
				print(text)
				
				if text == "MUTE":
					muted = True
				
				if text == "UNMUTE":
					muted = False
				
				if not muted and text != oldMsg:
					engine.say(text)			
					engine.runAndWait()

				oldMsg = text
				
	except:
		print("ERROR")

#chatMessage.save("file.jpg")



