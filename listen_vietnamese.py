def listening():	
	import speech_recognition # Nên để trên phần đầu chương trình

	robot_ear = speech_recognition.Recognizer() # Tạo ra robot_ear có thể nghe được
	with speech_recognition.Microphone() as mic: # Nghe được với việc sử dụng mic
		audio = robot_ear.listen(mic, phrase_time_limit=5) # audio = robot_ear nghe được bằng mic, với giới hạn thời gian là 5s

	try:
		audio_text = robot_ear.recognize_google(audio,language="vi VN") # Nhận dạng âm thanh nghe được ở trên .recognize_google() với ngôn ngữ là tiếng Việt
	except:
		audio_text = ""
	return audio_text