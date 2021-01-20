# Bioinformatics-work
Contains several algorithms and their dependancies used in learning about bioinformatics

BMP = Biology Meets Programming course 

BMPwk1 :
Pattern count - finds all occurences of a Pattern in a Text of bases.

Frequency Map -  computes the frequency map of a given string Text and integer k, returns a dictionary of each supplied k-mer value, eg. 3 and the provided Text

Frequent Words - list of all keys that have value in freq == m

Reverse Complement - finds the complement strand of a DNA strand

Pattern Matching

BMPwk2:
# Symbol array - helps to count the number of C in a window of Extended Genome, along with Pattern Count. Takes strings Genome and symbol as input and returns the symbol array of Genome corresponding to symbol.
* uses patterncount

# FasterSymbol array - takes genome and symbol but computes it quicker by using a better for loop
* uses patterncount

# Skew array - keeps track of total no of occurrences of C and G encountered so far in Genome

# Minimum skew - location where skew diagram obtains a minimum(location of ori)
* uses skewarray

# Hamming distance - pos i in kmers p and q is a mismatch if the symbols at pos i of the 2 strings are not the same. Total no. of mismatches bt strings p and q = hamming distance bt the strings

# Approximate Pattern Matching - finf all approx occurrences of a pattern in a string with at most d mismatches
* uses hammingdistance

# Approximate pattern count - find DnaA boxes by identifying frequent kmers, with d possible mismatches

BMPwk3:
# Count - creates a dictionary with all the nucleotides and how much they are present in the j-th column of the Motif matrix

# Profile - frequency of i-th nucleotide in the j-th column of the Motif matrix

# Consensus - string formed from the most frequent nucleotide per row in Motif matrix
* uses Count matrix

# Score - summing the number of symbols in the j-th column of Motifs that do not match the symbol in position j of the consensus string
* uses Consensus and Count matrix

# Probability(denoted as Pr) - of finding a chosen kmer given the profile matrix, eg: (Profile = {"A":[0.1,0.2],"T":[0.5,0.2] etc})

# Profile most probable kmer - a kmer tgat was most likely to have been generated by Profile among all kmers in Text
* Uses Pr function

BMPwk4:
# Count with Pseudocounts - takes a list of strings Motifs as input and returns the count matrix of Motifs with pseudocounts as a dictionary of lists (Similar to count matrix but it starts at 1 and not 0)

# Profile with Pseudocounts - takes a list of strings Motifs as input and returns the profile matrix of Motifs with pseudocount as a dictionary of lists

# Greedy Motif Search With Pseudocounts - generates each profile matrix with pseudocounts
* uses score, consensus,Pr ,ProfileMostProbableKmer, ProfileWithPseudocounts, CountWithPseudocounts

# Motifs - takes a profile Matrix Profile corresponding to a list of strings Dna as input and returns a list of the Profile most probable k-mers in each string from Dna
* Uses ProfileMostProbableKmer and Pr

# Random Motifs - choose a random kmer from each of t different strings Dna and returns a list of t strings which continuously iterates for as long as the score of the constructed motifs keep improving

# Randomized Motif Search - starts by generating a collection of random motifs using the RandomMotifs function which we set as the best scoring collection of motifs. It continuously runs until motif score stops improving.
* uses RandomMotifs, ProfileWithPseudocounts, Motifs, Score

# Repeated randomized motif search - finds best scoring motif
* uses randommotif, Profilewithpseudocounts,countwithpseudocounts,score,consensus,count,motifs,Pr,RandomizedMotifSearch

# Normalize - rescale a collection of probabilities so that they sum to 1. It takes a dict Probabilities whose keys are kmers. Values are probabilities of these kmers. It then divides each value in Probabilities by the sum of all values in Probabilities, returning the resulting dictionary

# Weighted die - takes a dict Probabilities whose keys are kmers and values are Prob of these Kmers. Returns a randomly chosen kmer key with respect to values in Probabilities

# Profile Generated String - returns a randomly generated kmer from Text whose probabilities are generated from Profile
* uses pr, normalize, weighteddie

# Gibbs sampler - discards a single kmer from the current set of motifs at each iteration and decides to either keep or replace one

* uses randommotifs, countwithpseudocounts,profilewithpseudocounts,profilegeneratingstring,normalize,weighteddie, pr,score,consensus,count

