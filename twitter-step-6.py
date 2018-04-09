import os,fnmatch,codecs


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


qury=str(input("Enter Search quary :"))
Or=set()
And=set()
for word in qury.split():
    if (word in dict):
        Or=(set(dict[word][1:]) | set(Or))
        if (len(And) > 0):
            And = set(And) & set(dict[word][1:])
        else:
            And=(dict[word][1:])

for a in And:
    f=open("nlp/step2/"+str(a),"r",encoding="utf-8")
    print(f.read() + "\n" + "-" * 100)
    f.close()

Or = set(Or).difference(set(And))

for a in Or:
    f=open("nlp/step2/"+str(a),"r",encoding="utf-8")
    print(f.read() + "\n" + "*" * 100)
    f.close()
