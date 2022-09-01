import speech_recognition
import keyboard
import math
from gtts import gTTS
from playsound import playsound


def hear_microphone():
    micro = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        micro.adjust_for_ambient_noise(source)
        print("Speak something!")
        try:
            audio = micro.listen(source)
            line = micro.recognize_google(audio, language="pt-BR")
            print("You spoke: " + line)
        except:
            print("Não entendi...")

        return line


def create_audio(line):
    tts = gTTS(line, lang="pt-br")
    tts.save("track.mp3")
    print("Preparing speech...")
    playsound("track.mp3")


line = hear_microphone()
line = line.split()
if line[0] == "somar":
    soma = ....str(float(line[1]) + float(line[3]))
    create_audio("a soma de "+line[1]+" com "+line[3]+" é "+soma)

elif line[0] == "subtrair":
    soma = str(float(line[1]) - float(line[3]))
    create_audio("a subtração de " + line[1] + " com " + line[3] + " é " + soma)

elif line[0] == "multiplicar":
    soma = str(float(line[1]) * float(line[3]))
    create_audio("a multiplicação de " + line[1] + " com " + line[3] + " é " + soma)

elif line[0] == "dividir":
    soma = str(float(line[1]) / float(line[3]))
    create_audio("a divisão de " + line[1] + " com " + line[3] + " é " + soma)

elif line[0] == "hipotenusa":
    soma = str("{:.2f}".format(math.sqrt((float(line[1])**2) + (float(line[3])**2))))
    create_audio("a hipotenusa dos catetos " + line[1] + " e " + line[3] + " é " + soma)

elif line[0] == "teste":
    line_mod = []
    for t in line:
        try:
            line_mod.append(float(t))
        except ValueError:
            pass

    soma = str(float(line_mod[0]) + float(line_mod[1]))
    create_audio("a soma de " + str(line_mod[0]) + " com " + str(line_mod[1]) + " é " + soma)
