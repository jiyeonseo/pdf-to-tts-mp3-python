import sys
import pyttsx3
import PyPDF2

# python main.py ./test.pdf 인자로 읽을 파일 받기
file_path = sys.argv[1]

if len(sys.argv) != 2:
	print("Insufficient arguments")
	sys.exit()

# binary mode로 파일 읽기
pdf_file = open(file_path, 'rb')

# PdfFileReader로 파일 읽을 Reader Object 생성
pdfReader = PyPDF2.PdfReader(pdf_file)

# 읽은 총 페이지 수 
pages = len(pdfReader.pages)

# pyttsx3.Engine 초기화 해주기
speaker = pyttsx3.init()

# 페이지 돌며 text 읽어오기 
for num in range(pages):
	# 해당 페이지 읽기
	page = pdfReader.pages[num] # pdfReader.getPage(num)
	# 해당 페이지 내 text 뽑아내기 
	text = page.extract_text() 
	# 뽑아낸 text 읽기 
	speaker.say(text)
	speaker.runAndWait() 

# mp3로 저장하려면 아래와 같이 하면 된다.
# speaker.save_to_file(text, 'audio.mp3')
# speaker.runAndWait()