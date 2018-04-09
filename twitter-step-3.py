import os,fnmatch,codecs


wordcount={}

for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:

            for word in file.read().split():

                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

step3 = open('nlp/step3/word-frequency.txt','w',encoding="utf-8")
for k,v, in sorted(wordcount.items(), key=lambda words: words[1], reverse = True):
    step3.write(k+":"+str(v)+"\n")