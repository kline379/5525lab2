from collections import Counter as Counter
import copy
import math

#First we simply calculate the probabilities from the train text.
Pwgt = dict()
Ptgt = dict()
#Accounts for unknown words or tags.
unknown = "<UKN>"
with open('data/pos_train.txt', 'r') as infile:
    for line in infile:
        prev_tag = 'START'
        for wst in line.strip().split(' '):
            wt = wst.split('/')
            tag = wt.pop()
            word = '/'.join(wt)
            if tag not in Pwgt:
                Pwgt[tag] = Counter()
            Pwgt[tag][word] += 1
            if prev_tag not in Ptgt:
                Ptgt[prev_tag] = Counter()
            Ptgt[prev_tag][tag] += 1
            prev_tag = copy.deepcopy(tag)
        tag = 'END'
        if prev_tag not in Ptgt:
            Ptgt[prev_tag] = Counter()
        Ptgt[prev_tag][tag] += 1
tags = Pwgt.keys()
n = 0;
for tag in Pwgt:
	Pwgt[tag][unknown]=.1
for tag in tags:
    if sum(Pwgt[tag].values()) > n:
        mfreq_tag = tag
        n = sum(Pwgt[tag].values())
n = 0;
for tag in tags:
    if sum(Ptgt[tag].values()) > n:
        mfreq_taggt = tag
        n = sum(Pwgt[tag].values())
for tag in Pwgt:
    obs = sum(Pwgt[tag].values())
    for word in Pwgt[tag]:
        Pwgt[tag][word] = math.log(Pwgt[tag][word])-math.log(obs)
for ptag in Ptgt:
    obs = sum(Ptgt[ptag].values())
    for ctag in Ptgt[ptag]:
        Ptgt[ptag][ctag] = math.log(Ptgt[ptag][ctag])-math.log(obs)
start = "START"
end = "END"
keys = list(Ptgt.keys())
keys.remove(start)
keys.append(end)

#First, we make an FSA that utilizes P(T|T)
f = open("ptgt.fsa.txt","w")

for tag in Ptgt[start]:
	f.write("{} {} {} {}\n".format(0, keys.index(tag)+1, tag, -Ptgt[start][tag]))

for prev_tag in Ptgt:
	if prev_tag != start:
		for tag in Ptgt[prev_tag]:
			f.write("{} {} {} {}\n".format(keys.index(prev_tag)+1, keys.index(tag)+1, tag, -Ptgt[prev_tag][tag]))
		f.write("{}\n".format(keys.index(prev_tag)+1))
f.close()

#Then an FST that utilizes P(W|T)
f = open("pwgt.fst.txt","w")
keys = list(Pwgt.keys())
for tag in Pwgt:
	for word in Pwgt[tag]:
		if word is "":
			word = "-"
		f.write("{} {} {} {} {}\n".format(0, 0, word, tag, -Pwgt[tag][word]))
f.write("0\n")
f.close()

#Produces the tag vocabulary
f = open("tags.voc","w")
index=0
tagset = set()
for tag in Ptgt:
	f.write("{} {}\n".format(tag, index))
	index = index + 1
	tagset.add(tag)
f.write("END {}\n".format(index))
f.write("{} {}\n".format(unknown, index+1))
f.close()

#Produces the word vocabulary
f = open("words.voc","w")
wordset = set()
wordset.add(unknown)
for tag in Pwgt:
	for word in Pwgt[tag]:
		if word == "":
			word = "-"
		wordset.add(word)
index = 0
for word in wordset:
	f.write("{} {}\n".format(word, index))
	index = index + 1
f.close()

#Translates the test data into one FSA and one FST for each line.
#The FSA is input for our labeler FST.
#The FST is a labeled and used to compare results later on.
with open('data/pos_test.txt', 'r') as infile:
    index = 1
    for line in infile:
        f = open('sents/sent{}.fsa.txt'.format(index), 'w')
        answer = open('answers/sent{}.fst.txt'.format(index),'w')
        i = 0
        for wst in line.strip().split(' '):
            wt = wst.split('/')
            tag = wt.pop()
            word = '/'.join(wt)
            if word not in wordset:
		word = unknown
            if tag not in tagset:
                tag = unknown
            f.write("{} {} {}\n".format(i, i+1, word))
            answer.write("{} {} {} {}\n".format(i, i+1, word, tag))
            i = i + 1
        f.write("{}".format(i))
        answer.write("{}".format(i))
        index = index + 1
        f.close()
        answer.close()

tags = Pwgt.keys()



