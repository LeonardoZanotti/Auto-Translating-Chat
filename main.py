from googletrans import Translator

translator = Translator()

text = "Hallo Welt"
translation = translator.translate(text, src="de", dest="en")

print(translation.text)