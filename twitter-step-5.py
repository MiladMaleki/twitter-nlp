import os,fnmatch,codecs
import re

dict={}
counter = 0
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8")as f:
            for word in f.read().split():
                if word not in dict:
                    dict[word]=["1"]
                    dict[word].append(filename)
                else:
                    dict[word][0]=str(int(dict[word][0])+1)
                    dict[word].append(filename)

op = open('nlp/step5/inverted-index.txt','w',encoding="utf-8")
for word in dict:
    op.write(word)
    for a in dict[word]:
        op.write(","+a)
    op.write("\n")