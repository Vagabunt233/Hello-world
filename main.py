def print_bot(text):
    print("bot:", text)

message = input("user: ").lower()
while message != "выход":
    if message == "привет":
        print_bot("Привет!")
    elif message == "как дела":
        print_bot("Прекрасно а у тебя как?")
    elif message == "нормально" or message == "хорошо" or message == "прекрасно": 
        print_bot("я рад за тебя!")
    elif message == "плохо":
        print_bot("печально, давай я тебя развеселю")
    elif "зовут" in message:
        print_bot("меня зовут Крута бот")
    else:
        print_bot("извини я тебя не понимаю")
    message = input("user: ").lower()
