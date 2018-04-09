

import os, fnmatch, codecs

counter = 0
inverted_indext = {}
count=1
word_Array=[]
stop_words = open('nlp/step4/stop words.txt','w',encoding="utf-8")
for line in open("nlp/step3/word-frequency.txt",encoding="utf-8"):
    stop_words.write(line[:line.find(":")]+"\n")
    word_Array.append(line[:line.find(":")])
    if (count >= 20):
        break
    count+=1





for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        stop_words = open('nlp/step4/' + filename + ".txt", 'w', encoding="utf-8")
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8")as f:
            for word in f.read().split():
                if word not in word_Array:
                    stop_words.write(word+" ")
        stop_words.close()

