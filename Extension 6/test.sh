#Make the required folders
mkdir -p compiledsents
mkdir -p composedsents
mkdir -p results
mkdir -p sents
mkdir -p answers
mkdir -p compiledanswers

#The bulk of the work happens here. First, weights are determined from pos_train.txt
#Then FSTs are produced with the probabilities from that data.
#Then test FSAs and FSTs are produced from pos_test.txt.
python fst_helper.py

#Compile and compose the FSTs

fstcompile --acceptor=true --isymbols=tags.voc ptgt.fsa.txt ptgt.fsa
fstcompile --osymbols=tags.voc --isymbols=words.voc pwgt.fst.txt pwgt.fst
fstarcsort --sort_type=olabel pwgt.fst > pwgt1.fst
fstarcsort --sort_type=ilabel ptgt.fsa > ptgt1.fsa
fstcompose pwgt1.fst ptgt1.fsa labler.fst
numfiles="$(find sents/. | wc -l)"
index=1
#Takes produced sentence files, compiles, composes, and finds shortest path.
ls sents $1 | while read x; 
  do 
    echo -en "\rfile $index of $numfiles being processed."
    fstcompile --acceptor=true --isymbols=words.voc sents/$x compiledsents/$x;
    fstcompose compiledsents/$x labler.fst composedsents/$x;
    fstshortestpath composedsents/$x composedsents/$x;
    #fstprint -isymbols=words.voc -osymbols=tags.voc composedsents/$x > results/$x;
    index=$((index+1))
done

ls answers $1 | while read x;
  do
    fstcompile --isymbols=words.voc --osymbols=tags.voc answers/$x compiledanswers/$x;
    fstisomorphic composedsents/$x answers/$name;
done
