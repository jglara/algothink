"""
Provide code and solution for Application 4
"""
from seq_align import compute_local_alignment, compute_alignment_matrix,\
    compute_global_alignment, build_scoring_matrix
import csv
from math import sqrt
from pyparsing import WordStart
import string

DESKTOP = True

import math
import random
import urllib2


import matplotlib.pyplot as plt

    

# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list


def compare_sequence(seq_x, seq_y):
    coincidences = [(x==y) for (x,y) in zip(seq_x,seq_y)]
    return (reduce(lambda x,y: x+y, coincidences) / float(len(seq_x))) * 100 

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    
    scoring_distributions = {}
    for _ in range(0,num_trials):
        l_seq_y = list(seq_y)
        random.shuffle(l_seq_y)
    
        alignment_matrix = compute_alignment_matrix(seq_x, l_seq_y, scoring_matrix, False)
        (score, _, _) = compute_local_alignment(seq_x, l_seq_y, scoring_matrix, alignment_matrix)
        
        if (score in scoring_distributions):
            scoring_distributions[score] = scoring_distributions[score] + 1
        else:
             scoring_distributions[score] = 1
             
    return scoring_distributions


def question1():
    human_eyeless_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_eyeless_protein = read_protein(FRUITFLY_EYELESS_URL)
    
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    
    alignment_matrix = compute_alignment_matrix(human_eyeless_protein, fruitfly_eyeless_protein, scoring_matrix, False)
    (score, align_human, align_fruitfly) = compute_local_alignment(human_eyeless_protein, fruitfly_eyeless_protein, scoring_matrix, alignment_matrix)
    
    print score
    print align_human
    print align_fruitfly
    
def question2():
    align_human = "HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ".replace("-","")
    align_fruitfly = "HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ"
    
    consensus = read_protein(CONSENSUS_PAX_URL)
    
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    
    alignment_matrix = compute_alignment_matrix(align_human, consensus, scoring_matrix, True)
    (score, align_human_consensus, align_consensus) = compute_global_alignment(align_human, consensus, scoring_matrix, alignment_matrix)
    
    print compare_sequence(align_human_consensus, align_consensus)
    print align_human_consensus
    print align_consensus
    
    print (score - 51.956) / 7.169
    
    
    alignment_matrix = compute_alignment_matrix(align_fruitfly, consensus, scoring_matrix, True)
    (score, align_fruitfly_consensus, align_consensus) = compute_global_alignment(align_fruitfly, consensus, scoring_matrix, alignment_matrix)
    
    print compare_sequence(align_fruitfly_consensus, align_consensus)
    print align_fruitfly_consensus
    print align_consensus
    
    print (score - 51.956) / 7.169
    
def question3():
    
    
    human_eyeless_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_eyeless_protein = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    
    iterations = 1000
    dist = generate_null_distribution(human_eyeless_protein, fruitfly_eyeless_protein, scoring_matrix, iterations)
    
    plt.xlabel("scores")
    plt.ylabel("fraction of total trials")
    plt.title("Null distribution")
    plt.bar(dist.keys(), [(x/float(iterations)) *100 for x in dist.values()])
    plt.show()
    
def generate_dist():
    human_eyeless_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_eyeless_protein = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    
    iterations = 1000
    dist = generate_null_distribution(human_eyeless_protein, fruitfly_eyeless_protein, scoring_matrix, iterations)
    
    w = csv.writer(open("dist.csv", "w"))
    for key,val in dist.items():
        w.writerow([key,val])
    
def question4():
    dist = {}
    for key, val in csv.reader(open("dist.csv")):
        dist[int(key)] = int(val)
        
    # calculate mean
    mean = sum([x*y for (x,y) in dist.items()]) / 1000.0
    
    print mean
    
    # deviation
    dev = sum([ ((x - mean)**2) * y for (x,y) in dist.items() ]) / 1000.0
    print sqrt(dev) 
    
    
def calculate_distance(checked_word, word, scoring_matrix):
    
    
    alignment_matrix = compute_alignment_matrix(checked_word, word, scoring_matrix, True)
    (score, _, _) = compute_global_alignment(checked_word, word, scoring_matrix, alignment_matrix)
    
    return len(checked_word) + len(word) - score


def check_spelling(checked_word, dist, words):
    mispelled = []
    scoring_matrix = build_scoring_matrix(string.ascii_lowercase, 2, 1, 0)
    for word in words:
        if calculate_distance(checked_word, word, scoring_matrix) <= dist:
            mispelled.append(word)

    return mispelled

def question8():
    words = read_words(WORD_LIST_URL)
    
    humble_list = check_spelling("humble",1,words)
    print humble_list
    
    firefly_list = check_spelling("firefly",2,words)
    print firefly_list
    
    
    
if __name__ == "__main__":
    question8()

