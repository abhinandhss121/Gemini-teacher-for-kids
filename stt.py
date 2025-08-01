import speech_recognition as sr
import pyttsx3
# initializing the recognizer
r = sr.Recognizer() 

def record_text():
    while(1):
        try:
            #Using microphone named source1
            with sr.Microphone() as source1:
                #adjusting ambient noise for better accuracy
                r.adjust_for_ambient_noise(source1,duration=0.2)
                #recording audio from source1(mic)
                audio1= r.listen(source1)
                #using recognize_google() to generate text
                myText = r.recognize_google(audio1)
                print(myText)
                return myText
            
        except sr.RequestError as e:
            print("could not request results:{0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured!")
    return
def output_text(text):
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return
while(1):
    recorded_text=record_text()
    output_text(recorded_text)
    print("wrote text")
    