# Extension 6
The extension implements our trained tagger as an FST. To do this we first run the python code to calculate the probabilities of each labeling.  From there, we create an FST to transform from words to tags using P(W|T) and then we compose that with an FSA that utilizes the P(T|T).  
The FST was successful at labeling most of the words correctly, however handling edge cases (like unseen words/tags) proved to be another step in translating our HMM to openFST.  It also takes a long time for the code to run since the "test" file is hundreds of lines and therefore we produce hundreds of FSTs in the process of testing.

To test the program, simply run `bash test.sh`.  All of the work is done in `test.sh` and `fst_helper.py`.  Both are reasonably well documented to answer any questions you may have.
