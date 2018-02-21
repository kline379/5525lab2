# Lab 2
The code can be run on the command line using 'python main.py'. The default is to run using pos_train.txt for training data and pos_test.txt for testing data. Differant training data can be input using the following format:
'python main.py -train [train data path] -test [test data path.]'
The epsilon value used for convergence can be set using the '-ep'  tag. An example using all three using the default behavior would be:
'python main.py -train pos_train.txt -test post_test.txt -ep .001'

Running main.py will output the results of part 0 and extension 1 with a comparison of the results to see which is better.

## hmms.py
The code implementing the vitirbi and the forward-backward algorithm can be found here.

## helpers.py
Extracts the needed data from the given input files.
