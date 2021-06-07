from tkinter import *
import googletrans
import speech_recognition as sr
import gtts
import playsound
import os

root=Tk()

# ........function defining......
def click():
    global scvalue
    global selected_lang2
    global selected_lang1
    recognizer=sr.Recognizer()
    translator=googletrans.Translator()
    try:
        with sr.Microphone() as source:
            scvalue3.set("speak now.....")
            scr.update()
            scvalue3.set("listening....")
            scr.update()
        
            voice=recognizer.listen(source)
            text=recognizer.recognize_google(voice,language=selected_lang1.get())
            scvalue.set(text)
            screen.update()
            scvalue3.set("")
            scr.update()


    except:
        scvalue3.set("!!communication error!! ")
        scr.update()

    translated=translator.translate(text,dest=selected_lang2.get())
    scvalue2.set(translated.text)
    screen2.update()
    converted_audio=gtts.gTTS(translated.text,lang="es")
    converted_audio.save("recording.mp3")
    playsound.playsound("recording.mp3",True)
    os.remove("recording.mp3")
    
   







def refresh():
    scvalue.set("")
    screen.update()
    scvalue2.set("")
    screen2.update()




# .......window geometry.....
root.geometry("560x300")
root.title("translator application")



# ....................label...................
l1=Label(root,text="LANGUAGE TRANSLATOR",font="lucida 15 bold")
l1.grid(row=0,column=3)



# ............input language...........
inp1=Label(root,text="Input Language")
inp1.grid(row=2,column=2)
inp2=Label(root,text="output language")
inp2.grid(row=4,column=2)

dict1={'afrikaans': 'af', 'albanian': 'sq',
 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
  'azerbaijani': 'az', 'basque': 'eu', 
  'belarusian': 'be', 'bengali': 'bn', 
  'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
   'cebuano': 'ceb', 'chichewa': 'ny',
    'chinese (simplified)': 
'zh-cn', 'chinese (traditional)': 'zh-tw',
 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs',
  'danish': 'da', 'dutch': 'nl', 'english': 'en',
   'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl','finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 
    'galician': 'gl', 'georgian': 'ka', 'german': 'de', 
    'greek': 'el', 'gujarati': 'gu', 
    'haitian creole': 'ht', 'hausa': 'ha',
     'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi',
      'hmong': 'hmn', 'hungarian': 'hu', 
      'icelandic': 'is', 'igbo': 
'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn',
 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 
 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky',
  'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
   'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
    'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
     'marathi': 'mr', 'mongolian': 'mn', 
     'myanmar (burmese)': 'my', 'nepali': 'ne', 
     'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 
     'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt',
     'punjabi': 'pa', 'romanian': 'ro', 'russian':'ru',
      'samoan': 'sm', 'scots gaelic': 'gd',
       'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
        'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk',
        'slovenian': 'sl', 'somali': 'so', 
        'spanish': 'es', 'sundanese': 
'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg',
 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 
 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur',
  'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
   'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 
   'yoruba': 'yo', 'zulu': 'zu'}

selected_lang1=StringVar(root)
selected_lang1.set("select")


lang=OptionMenu(root,selected_lang1,*dict1)
lang.grid(row=2,column=3)


scvalue=StringVar(root)
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 15 bold",width=35,bd=2)
screen.grid(row=3,column=3,ipady=15)


selected_lang2=StringVar(root)
selected_lang2.set("select")

lang=OptionMenu(root,selected_lang2,*dict1)
lang.grid(row=4,column=3)




# .............screen.......................
scvalue2=StringVar(root)
scvalue2.set("")
screen2=Entry(root,textvar=scvalue2,font="lucida 15 bold",width=35,bd=2)
screen2.grid(row=6,column=3,ipady=15)


b1=Button(root,text="refresh",command=refresh,width=7,bd=5)
b1.grid(row=8,column=2,ipady=5)

scvalue3=StringVar(root)
scvalue3.set("")
scr=Entry(root,textvar=scvalue3,font="lucida 10 bold",width=15,bg="yellow")
scr.grid(row=8,column=3,ipady=7)

b2=Button(root,text="translate",command=click,width=7,bd=5)
b2.grid(row=8,column=4,ipady=5)


root.mainloop()