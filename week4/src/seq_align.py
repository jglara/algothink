'''
Created on Nov 3, 2015

@author: ejogarv
'''

def get_score(char1, char2, diag_score, off_diag_score, dash_score):
    """ compute score
    """
    if char1 == '-' or char2 == '-':
        return dash_score
    
    if char1 == char2:
        return diag_score
    
    return off_diag_score

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """Takes as input a set of characters alphabet and three scores diag_score, off_diag_score, and dash_score. 
        The function returns a dictionary of dictionaries whose entries are indexed by pairs of characters in alphabet plus '-'. 
        The score for any entry indexed by one or more dashes is dash_score. 
        The score for the remaining diagonal entries is diag_score. 
        Finally, the score for the remaining off-diagonal entries is off_diag_score.
    """
    alphabet_extended = list(alphabet)
    alphabet_extended.append('-')
    
    
    scoring_matrix= dict([ (alpha,None) for alpha in alphabet_extended])
    for entry1 in alphabet_extended:
        scoring_matrix[entry1] = dict([(entry2,get_score(entry1,entry2, diag_score, off_diag_score, dash_score)) for entry2 in alphabet_extended])
        
    return scoring_matrix


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix. 
    The function computes and returns the alignment matrix for seq_x and seq_y as described in the Homework. 
    If global_flag is True, each entry of the alignment matrix is computed using the method described in Question 8 of the Homework.
    If global_flag is False, each entry is computed using the method described in Question 12 of the Homework.
    """
    
    # init matrix
    matrix = [ [0 for _ in range(0,len(seq_y)+1)] for _ in range(0,len(seq_x)+1)]
    
    if global_flag:    
        # calculate first row
        for i_item in range(1,len(seq_x)+1):
            matrix[i_item][0] = matrix[i_item-1][0] + scoring_matrix[ seq_x[i_item-1] ]['-']
    
        # calculate first column    
        for j_item in range(1,len(seq_y)+1):
            matrix[0][j_item] = matrix[0][j_item-1] + scoring_matrix['-'][ seq_y[j_item-1] ]
            
    # the rest of the matrix
    for i_item in range(1,len(seq_x)+1):
        for j_item in range(1,len(seq_y)+1):
            x_1 = seq_x[i_item-1]
            y_1 = seq_y[j_item-1]
            matrix[i_item][j_item] = max (matrix[i_item-1][j_item-1]+scoring_matrix[ x_1 ][y_1],
                                matrix[i_item-1][j_item]+scoring_matrix[ x_1 ]['-'],
                                matrix[i_item][j_item-1]+scoring_matrix['-'][ y_1 ]
                                )
            if not global_flag:
                if matrix[i_item][j_item] < 0:
                    matrix[i_item][j_item] = 0
    
    return matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix. 
    This function computes a global alignment of seq_x and seq_y using the global alignment matrix alignment_matrix.
    The function returns a tuple of the form (score, align_x, align_y) where score is the score of the global alignment align_x and align_y. 
    Note that align_x and align_y should have the same length and may include the padding character '-'.
"""

    i_item = len(seq_x)
    j_item = len(seq_y)
    
    align_x = []
    align_y = []
    score = 0
    
    if i_item>0:
        x_1 = seq_x[i_item-1]
        
    if j_item>0:
        y_1 = seq_y[j_item-1]
    
    while i_item>0 and j_item>0:
        x_1 = seq_x[i_item-1]
        y_1 = seq_y[j_item-1]
        if alignment_matrix[i_item][j_item] == (alignment_matrix[i_item-1][j_item-1] + scoring_matrix[x_1][y_1]):
            align_x.append(x_1)
            align_y.append(y_1)
            score += scoring_matrix[x_1][y_1]
            i_item = i_item-1
            j_item = j_item-1
        else:
            if alignment_matrix[i_item][j_item] == (alignment_matrix[i_item-1][j_item] + scoring_matrix[x_1]['-']):
                align_x.append(x_1)
                align_y.append('-')               
                score += scoring_matrix[x_1]['-']
                i_item = i_item-1
            else:
                align_x.append('-')
                align_y.append(y_1)
                j_item = j_item-1                
                score += scoring_matrix['-'][y_1]
                
    while i_item>0:
        align_x.append(seq_x [i_item-1])
        align_y.append('-')
        score += scoring_matrix[x_1]['-']
        i_item=i_item-1
        
    while j_item>0:
        align_y.append(seq_y [j_item-1])
        align_x.append('-')
        score += scoring_matrix['-'][y_1]
        j_item=j_item-1

    align_x.reverse()
    align_y.reverse()
    return(score, ''.join(align_x), ''.join(align_y))


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix scoring_matrix. 
    This function computes a local alignment of seq_x and seq_y using the local alignment matrix alignment_matrix.
    The function returns a tuple of the form (score, align_x, align_y) where score is the score of the optimal local alignment align_x and align_y. 
    Note that align_x and align_y should have the same length and may include the padding character '-'.
"""

    # find the max value
    
    i_item = len(seq_x)
    j_item = len(seq_y)
    max_value = None
    max_i = 0
    max_j = 0
    for i_item in range (0,len(seq_x)+1):
        for j_item in range (0,len(seq_y)+1):
            if alignment_matrix[i_item][j_item] > max_value:
                max_value = alignment_matrix[i_item][j_item]
                max_i = i_item
                max_j = j_item
            
        
    
    align_x = []
    align_y = []
    score = 0
    
    i_item = max_i
    j_item = max_j
    while alignment_matrix[i_item][j_item] > 0:
        x_1 = seq_x[i_item-1]
        y_1 = seq_y[j_item-1]
        if alignment_matrix[i_item][j_item] == (alignment_matrix[i_item-1][j_item-1] + scoring_matrix[x_1][y_1]):
            align_x.append(x_1)
            align_y.append(y_1)
            score += scoring_matrix[x_1][y_1]
            i_item = i_item-1
            j_item = j_item-1
        else:
            if alignment_matrix[i_item][j_item] == (alignment_matrix[i_item-1][j_item] + scoring_matrix[x_1]['-']):
                align_x.append(x_1)
                align_y.append('-')               
                score += scoring_matrix[x_1]['-']
                i_item = i_item-1
            else:
                align_x.append('-')
                align_y.append(y_1)
                j_item = j_item-1                
                score += scoring_matrix['-'][y_1]
                

    align_x.reverse()
    align_y.reverse()
    return(score, ''.join(align_x), ''.join(align_y))