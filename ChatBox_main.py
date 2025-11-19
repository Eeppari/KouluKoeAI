import tkinter, time, clipboard, win32clipboard, turtle, requests

API_URL = "https://koulu-koe-ai-api.eetupetteri2010.workers.dev/use"

showScreen = False
ChatBox = turtle.Screen() ## CHANGE TURTLE FOR TKINTER
ChatBox.setup(940, 150, starty=40)
token = None
if showScreen:
    turtle.penup()
    turtle.goto(-450, 50)
else:
    ChatBox.setup(30, 40, startx=-350, starty=650)
messages = [ {"role": "system", "content": 
              "This is a test."} ]

def submitCopy(usingToken):
    ChatBox.bgcolor("green")
    time.sleep(0.1)
    ChatBox.bgcolor("white")
    win32clipboard.OpenClipboard()
    msg = win32clipboard.GetClipboardData()
    if msg:
        response = requests.post(API_URL, json={"token": usingToken, "text": msg}).json()
    reply = response["result"]
    try:
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

def checkToken(checkingToken):
    response = requests.post(
        "https://koulu-koe-ai-api.eetupetteri2010.workers.dev/check",
        json={"token": checkingToken}
    ).json()

    if not response.get("valid"):
        reason = response.get("reason", "unknown")
        ChatBox.bgcolor("red")
        print("Token invalid:", reason)
        time.sleep(1)
        raise SystemExit("Invalid token: " + reason)
    
    print("Token valid!")

def StartChatBox():
    tkn = ChatBox.textinput(title="Chatbox Security", prompt="Enter token")
    if tkn != None:
        checkToken(tkn)
        return tkn
    else:
        raise

token = StartChatBox()
ChatBox.listen()
ChatBox.onkeyrelease(lambda: submitCopy(token), "Tab" and "c")
ChatBox.onkeyrelease(searchData, "Tab" and "s")
while True:
    ChatBox.update()
    ChatBox.listen()
    time.sleep(1)