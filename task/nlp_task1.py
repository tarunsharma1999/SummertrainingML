import pytesseract
from pytesseract import image_to_string
from PIL import Image
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
img=Image.open('news.jpeg')
#config=('-1 eng --oem 1 --psm 3')
text=image_to_string(img)
#print(text)

#storing text into file

f= open('text','r+')
f.write(text)
f.close()

#Removing stopwords

token_text=word_tokenize(text)
final_text=[]
for i in token_text:
	if i.lower() not in stopwords.words('english'):
		final_text.append(i)		
		#print(i)

#print(final_text)
text_count=nltk.FreqDist(final_text)
print("5 Most Frequent Words Used:")
print(text_count.most_common(5))


