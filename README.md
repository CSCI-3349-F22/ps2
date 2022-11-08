# Problem Set 2: POS tagging: most frequent vs. HMM vs. LSTM

In this problem set, you will be experimenting with different sequence tagging algorithms for part-of-speech (POS) tagging. These methods will be:

* Looking up the most frequent POS by calling the nltk POS tagger on invidual words (in `hmm/viterbi.py`)
* An HMM using Viterbi search to find the best POS tags given emission and transition probabilities (also in `hmm/viterbi.py`)
* An LSTM for sequence taggging (in `lstm/postag-lstm.ipynb`)

You will add, commit, and push (1) your own version of `viterbi.py` and (2) a PDF containing the answers to all questions beginning with Q in this README and the one Q in the Jupyter motebook. **This is due Friday, November 18, at 11:59pm EST.**


## Part 1: Comparing most frequent POS tagging approach with HMM tagger
Clone your repo down to your own machine. You will find two directories: `hmm` and `lstm`. In the `hmm` directory you'll find some data files and a python program called `viterbi.py`. You will be writing your code for this part of the problem set in the `viterbi.py` files.

A week or two ago, we learned about part of speech (POS) tagging and about Hidden Markov Models (HMMs). You will be putting these two ideas together by building a part of speech HMM and implementing a search algorithm to tag each word in a sentence with a part of speech label. 

HMMs require two sets of probabilities: *emission probabilities* and *transition probabilities*. I have calculated these probabilities for you from a large corpus of POS-tagged text, which you can find in the `lstm` directory. In `viterbi.py`, I provide skeleton code for reading these probabilities from two files (`emissProbs.txt` and `transitProbs.txt`) into data structures that you can use when implementing your algorithm. I also provide code for testing your algorithm on the provided file of input test sentences (`test-ps2.txt`) and measuring the accuracy of your implementations. 

The code has lots of comments to help you along. Please refer to the slides from Week 9 and Week 10 for full details on how HMMs and Viterbi search work and how our example in class about ice creams relates to the task of POS tagging.

### Task 1: Most frequent POS
NLTK has a part of speech tagger that you can call with `nltk.pos_tag()`. If you call it on one word at a time (as opposed to a whole sentence), it will return the most frequent part of speech tag associated with that word. If you run `viterbi.py`, without modifying it in any way, it will print out each test sentence, its correct POS sequence, and the sequence that you'd get if you just picked the most frequent POS tag using `nltk.pos_tag()`.

**Q1: What is the accuracy of this system, as reported by the program?**

**Q2: Give specific examples of errors where context would have helped the system select the correct part of speech tag.**

### Task 2: Viterbi search
In this part of the problem set, you will implement Viterbi search to determine the best sequence of part of speech tags for an input sentence using the probabilities I have provided. Everything you need to do is outlined in the comments of `viterbi.py`. To summarize, you will write a function that does the following: (1) for a given input sentence, populate the Viterbi lattice, as shown in the slides from class; (2) using backpointers, print out the most probable part of speech sequence for that input sentence. Follow the instructions. Then answer the following questions.

**Q3: What is the accuracy of your Viterbi POS tagger? (If you are doing it right, your accuracy should be above 90%.)**

**Q4: Explain why this yields higher accuracy than just selecting the most frequent part of speech tag for each word, as you did in Part 1.**

**Q5: Identify three errors made by the Viterbi search and try to determine why this error was made. You will need to understand what the tags mean. It will also help to think about both the emission and the transition probabilities, as well as stuff like OOVs and word frequency.** 

*Here's an example: "Saturday mornings" was tagged as NNP NNP instead of NNP NNS. This could be because P(NNP|NNP) (the probability of seeing NNP after NNP) is much higher than P(NNS|NNP) (the probability of seeing NNS after NNP). Thus, even though the emission probability of NNS for "mornings" was quite high, the high transition probability from NNP to NNP may tipped the scales for NNP.*

---

## Part 2: Comparing an LSTM POS tagger to your HMM tagger
In the `lstm` directory, you'll find Jupyter notebook and some text files. Then open the Jupyter notebook in Colab, as we have done for the past two labs. Then upload the text files to your Google Drive in a directory called `ps2` or use the temporary file storage thing in Colab (and adjust the paths in the code accordingly).

Read the explanations and then run the code cell by cell. Then in your PDF include answers to **Q6** and **Q7**, which appear at the end of the notebook.

---

Add, commit, and push (1) your  version of `viterbi.py`; and (2) a PDF containing the answers to all questions beginning with Q in this README *and* in the Jupyter notebook. 

**This is due Friday, November 18, at 11:59pm EST.**
