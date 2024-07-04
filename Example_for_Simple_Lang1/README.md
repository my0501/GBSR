# Explanation of example_fin.pdf

## The `example_fin.pdf` file presents the procedural methods and coverage information, and detailed descriptions of mutation generation and killed relationships, as exemplified in Section 3 of the paper. 

## According to Tables 2 and 3, we obtained the statement coverage and killed information for part of Lang1, thereby constructing a Fault-oriented Interaction Graph. 

## Based on this Graph, we derived two matrices (associated with passed tests and failed tests, respectively), performed PageRank calculations on both matrices, and obtained a list of PageRank values. 

## By extracting the top three values from the list, we obtained the corresponding values of method entities in the two matrices. 

## Using the weight calculation formula and setting α to 1, we calculated the weight of each method entity, refining the suspicion scores of traditional fault localization techniques and obtaining more effective suspicion scores.
