import numpy as np
import re
import nltk


## To complete Part 2 (Viterbi):

## (1) Locate the places where I have written 
##             "YOUR CODE GOES HERE".
## In those places, you will insert your code.

## (2) To test your code, locate where I have written
##             "BEGIN UNCOMMENT CODE".
## Uncomment that code to start testing your code.


## The final program should print out the accuracy of
## 1. The nltk.pos_tag() method.
## 2. Your Viterbi implementation.


######################################
### READ IN EMISSION PROBABILITIES ###
######################################

## For a given POS, how likely is each word?
## Stored in a dict where the keys are POS
## and the value is a dictionary of word:prob pairs.
## These are *not* log probabilities.

emits = {}  ## dict that stores the emission probs

f = open('emissProbs.txt')
for line in f:
    parts = line.rstrip().split()
    pos = parts[0]
    word = parts[1]
    eprob = float(parts[2])
    if pos in emits.keys():
        emits[pos][word] = eprob
    else:
        emits[pos] = {word:eprob}
f.close()

########################################
### READ IN TRANSITION PROBABILITIES ###
########################################

## How likely is one POS to follow another POS?
## Stored in a dict where keys are tuples of POS sequences 
## and the values are the probabilities of those sequences.
## These are *not* log probabilities.

biprobs = {}  ## dictr that stores transition probs

f = open('transitProbs.txt')
for line in f:
    parts = line.rstrip().split()
    pos1 = parts[0]
    pos2 = parts[1]
    prob = float(parts[2])
    biprobs[(pos1, pos2)] = prob
f.close()


######################
## LIST OF POS TAGS ##
######################
## You'll store your Viterbi trellis as a 2D numpy array.
## One dimension will be the number of POS tags, and the 
## other  will be the number of tokens in the input sentence.
## We want to be able to map columns in the array to 
## POS tags. Here's how we can do that.

pos2int = list(emits.keys())

#####################
### NLTK.POS_TAG  ###
#####################

# this just calls nltk.pos_tag() on
# each word individually to get the most
# frequent POS for each word.

def run_nltkpos(insent):
    posseq = "BOS"
    for t in insent:
        posseq = posseq + " " + (nltk.pos_tag([t])[0][1])
    return(posseq + " EOS")


########################
### VITERBI FUNCTION ###
########################

def run_viterbi(insent):

    ## NOTE:
    ## You need to be able to fill in some value for every state.
    ## But sometimes the emission probability will be 0 (e.g., 
    ## the probability that you see "the" when the tag is NN).
    ## You can account for this possibility *and* for the 
    ## possibility of an OOV, by assigning this default prob
    ## when you emission probability is 0.
    defaultprob =  0.00000000001

    ## Create the trellis and backpointer itself as a 2D np array
    stateprobs = np.zeros(shape=(len(insent), len(pos2int)))
    backpointers = np.zeros(shape=(len(insent), len(pos2int)))

    ## Initialize state 0, which must be BOS with probability 1
    stateprobs[0,pos2int.index("BOS")] = 1.0

    ## Fill in the rest of the trellis, starting with state 1
    ## Populate both stateprobs *and* backpointers!

    for i in range(1, len(insent)):

        # this line allows the program to run and you can
        # delete it once you've written your code below.
        dummyvar = 1

        #########################
        ## YOUR CODE GOES HERE ##
        #########################


    ## Store the string of POS tags in a variable called posseq
    ## You know that the last POS tag has to be EOS.
    posseq = "EOS"

    ## After populating the full trellis and backpointer trellis,
    ## print out the proposed POS tag sequence by traversing
    ## the backpointers from the backpointer in the last 
    ## column that corresponds to "EOS" (end of sentence tag).

    ## Getting you started on backtrace...
    maxprob = stateprobs[len(insent)-1,pos2int.index("EOS")]
    maxprobid = backpointers[len(insent)-1,pos2int.index("EOS")]

    for i in range(len(insent)-2, 0, -1):

        # this line allows the program to run
        dummyvar = 1

        #########################
        ## YOUR CODE GOES HERE ##
        #########################

    return posseq


##########################
### COUNT CORRECT TAGS ###
##########################

## Function to find incorrect tags
def countcorrecttags(sq1, sq2):
    numcorrect = 0
    numwrong = 0
    if len(sq1) == len(sq2):
        for idx in range(len(sq1)):
            if sq1[idx] == sq2[idx]:
                numcorrect += 1
            else:
                numwrong += 1
    return [numcorrect, numwrong]
                


######################
### TEST SENTENCES ###
######################

## Read in a list of 100 sentences and the correct 
## POS tags. Use your functions function to
## generate POS tags for each sentence, then 
## compare the output against the correct POS tags.


## Use these to keep track of how many tags you got right.

# viterbi
V_numcorrect = 0
V_numwrong = 0

# most frequent (with nltk)
M_numcorrect = 0
M_numwrong = 0


## Read in the test file of sentences to tag.
f = open("test-ps2.txt")
for line in f:
    
    ## Break each sentence into POS tags and word tokens
    line = re.sub(r'\(', "", line.rstrip())
    line = re.sub(r'\)', "", line.rstrip())
    parts = line.split()

    ## Create strings with words and POS tags
    testin = "BOS "
    testout = "BOS "
    for i in range(1, len(parts), 2):
        testout = testout + parts[i] + " "
        testin = testin + parts[i-1] + " "
    testout = testout + "EOS"
    testin = testin + "EOS"

    # print out the sentence, correct POS tags.
    print(testin)
    print(testout)

    ## Run the nltk.pos_tag() method on each word individually.
    ## Test the accuracy of this method.
    mostfreqpos_guess = run_nltkpos(testin.split()[1:-1])
    print(mostfreqpos_guess + "\n")

    sq1 = testout.split()
    sq2 = mostfreqpos_guess.split()
    (c, w) = countcorrecttags(sq1, sq2)
    M_numcorrect += c
    M_numwrong += w


    ##########################
    ## BEGIN UNCOMMENT CODE ##
    ##########################

    ## Call the viterbi algorithm which returns a string of POS tags
    #viterbiguess = run_viterbi(testin.split())

    # Print out the predicted sequence of POS tags.
    #print(viterbiguess + "\n")

    ## Count correct and incorrect tags for this sentence
    #sq1 = testout.split()
    #sq2 = viterbiguess.split()
    #(c, w) = countcorrecttags(sq1, sq2)
    #V_numcorrect += c
    #V_numwrong += w

f.close()


## Print out overall tagging accuracy
#print("Viterbi Accuracy: ", (V_numcorrect / (V_numcorrect+V_numwrong)))


    ########################
    ## END UNCOMMENT CODE ##
    ########################

print("Most Frequent POS Accuracy: ", (M_numcorrect / (M_numcorrect+M_numwrong)))
