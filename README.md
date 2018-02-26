# Lab 2

In this lab we implemented an HMM utilizing a viterbi algorithm. In addition to the required part 0, we implemented extension 6 and answered extension 3.  Part 0 and extension 6 can be found in their respective folder.  Extension 3 can be found below.

## Instructions
Part 0 can be run by opening the python notebook and then simply running each cell in order. The user must ensure that the folder with training and test data is in the current directory under the "pos" folder or otherwise fix the file addresses acordingly.

## Extension 3:
Changing the HMM to be case-insensitive slightly increased the error rate from 5% to 6%. The only words that would be impacted by this are proper nouns that are more commonly used as common nouns, for which there would now be ambiguity and a higher probability for the word being a common noun (and thus being misclassified as such). This may effect performance on the word following the misclassified proper noun, but the effect would be less pronounced. The results suggest, however, that this decision does not significantly impact performance, likely because these cases are only a small subset of the observations.
