import re

files = {
					 '1' : 'p1.txt',
           '2' : 'p2.txt',
           '3' : 'p3.txt',
}

print ("Enter file number (1,2,3):")
filenumber = input()

while (not(filenumber in files.keys())):
	print ("Enter file number (1,2,3):")
	filenumber = input()



words=re.findall("\w+", open(files[filenumber]).read().lower())
sentences=re.findall(r".*?\.", open(files[filenumber]).read().lower())

#print ("%s" % len(words))
#print ("%s" % words)
#print ("%s" % sentences)


wordcount = 0
totalletters = 0

for word in words:
	totalletters = totalletters + len(word)
	wordcount = wordcount + 1
	
averagewordlen = 	totalletters / wordcount

sentencecount = 0
totalwords = 0

for sentence in sentences:
	words2=re.findall("\w+", sentence.lower())
	totalwords = totalwords + (len(words2)-1)
	sentencecount = sentencecount + 1
	
averagesentence = 	totalwords / sentencecount


print ("Total words found: %s" % (len(words)-1))
print ("Average letters per word: %s" % round(averagewordlen,2))
print ("Total sentences found: %s" % (len(sentences)))
print ("Average word per sentence: %s" % round(averagesentence,2))