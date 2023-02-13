# %% Hàm nói tiếng anh giọng nữ [1]. Nếu giọng nam là [0]
def speaking(text):

    import pyttsx3

    engine = pyttsx3.init() #Khởi tạo biến engine có thể nói được

    voices = engine.getProperty('voices') #Khởi tạo voices có thể chỉnh sửa 
    engine.setProperty("voice", voices[1].id) #Chỉnh sửa  thành giọng nữ [1]

    engine.say(text) #Chuyền biết văn bản text vào hàm say()
    engine.runAndWait() #Chạy biến engine khi đã được chỉnh sửa và truyền văn bản cần đọc

# %%
import pyttsx3
text = "How are you"
engine = pyttsx3.init() #Tạo nên engine( động cơ ) có thể nói

voices = engine.getProperty('voices')

for voice in voices: #In ra thông tin id các giọng đọc có thể chọn
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

voices = engine.getProperty("voices")#Chỉnh sửa
engine.setProperty("voice",voices[1].id)

engine.say(text) #Đưa văn bản vào để nói
engine.runAndWait() #Chạy