import re
import os

txt_files = os.listdir("samples/stories/test2/")
corpus = set([])
for txt_file in txt_files:
    with open("samples/stories/test2/"+txt_file, "r", encoding='utf-8') as f:
        for line in f:
            w_list = line.split()
            for i, w in enumerate(w_list):
                w = re.sub(r"[^a-zA-Z]", "", w)
                if len(w) > 0:
                    corpus.add(w.lower()) 
corpus2 = set([])
num_unk = 0
with open("result0630_8.full", "r", encoding='utf-8') as f:
    for line in f:
        w_list = line.split()
        for i, w in enumerate(w_list):
            w = re.sub(r"[^a-zA-Z]", "", w)
            if len(w) > 0:
                if w == "UNK":
                    num_unk += 1
                corpus2.add(w.lower())
# corpusとcorpus2の共通部分の数を数える
print(num_unk)
print(len(corpus))
print(len(corpus2))
print(len(corpus & corpus2))
print(len(corpus & corpus2)/len(corpus))