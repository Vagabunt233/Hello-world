reference = {
    "hello":{"ru":"Привет!", "en": "Hello"},
   "fine": {"ru":"Прекрасно а у тебя как?","en": "Im fine, and you?"},
   "glad":{"ru":"я рад за тебя!", "en": "Its wonderfull"},
   "sad": {"ru":"печально, давай я тебя развеселю", "en": "Its sadness.can i make you funny?"},
   "name":{"ru":"меня зовут Крута бот", "en": "My name is Kruta Bot"},
   "none":{"ru":"извини я тебя не понимаю", "en": "Excuse me i dont understand you "},

}
question = {
    "hello":{"ru":"привет", "en":"hello",},
    "how":{"ru":"как дела","en":"how are you"},
    "norm":{"ru":"нормально","en":"normal"},
    "fine":{"ru":"хорошо","en":"fine"},
    "wonderfull":{"ru":"прекрасно", "en":"wonderfull"},
    "sad":{"ru":"плохо", "en":"sad"},
    "name":{"ru":"зовут", "en":"name"},
    "exit":{"ru":"выход", "en":"exit"},
}
LANG = "en"
def print_bot(text):
    print("bot:", text)

message = input("user: ").lower()
while message != question["exit"][LANG]:
    if message == question["hello"][LANG]:
        print_bot(reference["hello"][LANG])
    elif message == question["how"][LANG]:
        print_bot(reference["fine"][LANG])
    elif message ==  question["norm"][LANG] or message == question["fine"][LANG]  or message == question["wonderfull"][LANG]: 
        print_bot(reference["glad"][LANG])
    elif message == question["sad"][LANG]:
        print_bot(reference["sad"][LANG])
    elif  question["name"][LANG] in message:
        print_bot(reference["name"][LANG])
    else:
        print_bot(reference["none"][LANG])
    message = input("user: ").lower()
