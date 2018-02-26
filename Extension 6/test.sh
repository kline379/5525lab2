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
echo "running python script..."
python fst_helper.py

#Compile and compose the FSTs

echo "compiling labeler fst..."
fstcompile --acceptor=true --isymbols=tags.voc ptgt.fst.txt ptgt.fst
fstcompile --osymbols=tags.voc --isymbols=words.voc pwgt.fst.txt pwgt.fst
fstarcsort --sort_type=olabel pwgt.fst > pwgt1.fst
fstarcsort --sort_type=ilabel ptgt.fst > ptgt1.fst
fstcompose pwgt1.fst ptgt1.fst labeler.fst
numfiles="$(find sents/. | wc -l)"
index=1
#Takes produced sentence files, compiles, composes, and finds shortest path.
ls sents $1 | while read x; 
  do 
    echo -en "\rfile $index of $numfiles test sentences being produced..."
    fstcompile --acceptor=true --isymbols=words.voc sents/$x compiledsents/$x;
    fstcompose compiledsents/$x labeler.fst composedsents/$x;
    fstshortestpath composedsents/$x composedsents/$x;
    fstprint -isymbols=words.voc -osymbols=tags.voc composedsents/$x > results/$x;
    index=$((index+1))
done

#Compiles to correct answers
#TODO: Automate comparisons with composedsents.
index=1
numfiles="$(find answers/. | wc -l)"
ls answers $1 | while read x;
  do
    echo -en "\rfile $index of $numfiles test answers being produced..."
    fstcompile --isymbols=words.voc --osymbols=tags.voc answers/$x compiledanswers/$x;
    index=$((index+1))
done

