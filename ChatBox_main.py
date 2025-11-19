import openai
import turtle
import time
import clipboard
import win32clipboard


openai.api_key = 'ENTER API KEY'

showScreen = False
ChatBox = turtle.Screen()
ChatBox.setup(940, 150, starty=40)
Questions = False
if showScreen:
    turtle.penup()
    turtle.goto(-450, 50)
else:
    ChatBox.setup(30, 40, startx=-350, starty=650)
messages = [ {"role": "system", "content": 
              "This is a test."} ]

def submitCopy():
    ChatBox.bgcolor("green")
    time.sleep(0.1)
    ChatBox.bgcolor("white")
    win32clipboard.OpenClipboard()
    msg = win32clipboard.GetClipboardData()
    if msg:
        messages.append(
            {"role": "user", "content": msg},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-5.1", messages=messages
        )
    reply = chat.choices[0].message.content
    try:
        messages.append({"role": "assistant", "content": reply})
        win32clipboard.CloseClipboard()
        print(reply)
        clipboard.copy(reply)
        ChatBox.bgcolor("green")
        time.sleep(0.1)
        ChatBox.bgcolor("white")
    except:
        win32clipboard.CloseClipboard()
        print(reply if reply else "ERROR GETTING REPLY")
        ChatBox.bgcolor("red")
        time.sleep(0.1)
        ChatBox.bgcolor("white")

def searchData():
    tiedot = {
        "kansalaisen perusoikeudet": "1.Yhdenvertaisuus 2.oikeus elämään ja vapaus ja koskemattomuus 3.liikkumisvapaus 4.yksityiselämän suoja 5 ja 6. uskonnon ja sananvapaus 7.kokoontumisvapaus 8.vaalioikudet",
        "perinteinen rasismi": "Alistaminen/orjuus, Ylittämättömän biologiset erot",
        "uusrasismi" : "Poissulkeminen(Suomi suomalaisille), Ylittämättömän kulttuuriset erot, Ihmisarvon loukkaus tai sen kiistäminen"
    }
    win32clipboard.OpenClipboard()
    search = win32clipboard.GetClipboardData()
    if search in tiedot:
        print(tiedot[search])
        clipboard.copy(tiedot[search])
    else:
        clipboard.copy("Ei ole. Vaihtoehdot ovat: kansalaisen perusoikeudet, perinteinen rasismi")
    ChatBox.bgcolor("green")
    time.sleep(0.1)
    ChatBox.bgcolor("white")
    win32clipboard.CloseClipboard()

def StartChatBox():
    ChatBox.numinput(title="Chatbox Security", prompt="Enter token")

StartChatBox()
ChatBox.listen()
ChatBox.onkeyrelease(submitCopy, "Tab" and "c")
ChatBox.onkeyrelease(searchData, "Tab" and "s")
while True:
    ChatBox.update()
    ChatBox.listen()
    time.sleep(1)