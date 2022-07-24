import speech_recognition as sr
import os

r = sr.Recognizer()

msg = "Enter para hablar..."

while True:
	if input("IA: " + msg) != "0":
		with sr.Microphone() as source:
			audio = r.listen(source)

		#traducir de audio a texto con Google
		try:
			out_text = r.recognize_google(audio, language="es-ES")
			print("\nTu: "+ out_text + "\n")
		except sr.UnknownValueError:
		    print("No te entendí")
		except sr.RequestError as e:
		    print("Google no respondió")

		if "cómo estás" in out_text.lower():
			msg = "Bien y tu? "
		elif "abre" in out_text.lower():
			agregar = False
			msg = "Abriendo "
			for x in out_text.split():
				msg+=x if agregar else ""
				if x.lower() == "abre":
					agregar = True
					pass
				pass

			os.system("start www." + msg[9:]+".com")
		else:
			msg = ""

		msg += "(enter)"
	else:
		break


