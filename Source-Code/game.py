# ******************************************************************************   
#  Bingo
#
#  @author: Elisha Lai
#  @desciption: Program that allows a player to play Bingo
#  @version: 1.3 12/03/2014
# ******************************************************************************

import sys

# negate_mini_bingo_card: (listof Int) (listof Int) -> (listof Int)
# Conditions:
#     PRE: lst1 and lst2 must be non-empty lists.
#          len(lst1) = 9
#          The first three values in lst1 are between 1 and 15 inclusively.
#          The next three values in lst1 are between 16 and 30 inclusively.
#          The last three values in lst1 are between 31 and 45 inclusively.
#          len(lst2) = 5
#          The values in numbers_called are between 1 and 45 inclusively.
#     POST: The length of the produced list is the same length as lst1
# Purpose: Consumes two lists of integers, lst1 and lst2. Produces a list of
#          integers.
# Effects: Mutates lst1 so that all values in lst1, which are also in lst2, are
#          negated.

def negate_mini_bingo_card(lst1,lst2,ind):
    if ind<len(lst2):
        if lst2[ind] in lst1:
            lst1[lst1.index(lst2[ind])] = -lst2[ind]
            negate_mini_bingo_card(lst1,lst2,ind+1)
        else: 
            negate_mini_bingo_card(lst1,lst2,ind+1)

# is_row_negative: (listof Int) -> Bool
# Conditions:
#     PRE: card must be a non-empty list.
#          len(card) = 9
#          No values in card are zero.
# Purpose: Consumes a list of integers, card. Produces True if any row of card
#          contains three negated numbers. Otherwise, False is produced.

def is_row_negative (card):
    if (card[0] < 0 and card[3] < 0 and card[6] < 0) or\
       (card[1] < 0 and card[4] < 0 and card[7] < 0) or\
       (card[2] < 0 and card[5] < 0 and card[8] < 0):
        return True
    else:
        return False

# is_col_negative: (listof Int) -> Bool
# Conditions:
#     PRE: card must be a non-empty list.
#          len(card) = 9
#          No values in card are zero.
# Purpose: Consumes a list of integers, card. Produces True if any column of
#          card contains three negated numbers. Otherwise, False is produced.

def is_col_negative (card):
    if (card[0] < 0 and card[1] < 0 and card[2] < 0) or\
       (card[3] < 0 and card[4] < 0 and card[5] < 0) or\
       (card[6] < 0 and card[7] < 0 and card[8] < 0):
        return True
    else:
        return False

# is_diag_negative: (listof Int) -> Bool
# Conditions:
#     PRE: card must be a non-empty list.
#          len(card) = 9
#          No values in card are zero.
# Purpose: Consumes a list of integers, card. Produces True if diagonal of
#          card contains three negated numbers. Otherwise, False is produced.

def is_diag_negative (card):
    if (card[0] < 0 and card[4] < 0 and card[8] < 0) or\
       (card[2] < 0 and card[4] < 0 and card[6] < 0):
        return True
    else:
        return False

# mini_bingo: (listof Int) (listof Int) -> Bool
# Conditions:
#     PRE: mini_bingo_card and numbers_called must be non-empty lists.
#          len(mini_bingo_card) = 9
#          The first three values in lst1 are between 1 and 15 inclusively.
#          The next three values in lst1 are between 16 and 30 inclusively.
#          The last three values in lst1 are between 31 and 45 inclusively.
#          len(numbers_called) = 5
#          The values in numbers_called are between 1 and 45 inclusively.
# Purpose: Consumes two lists of integers, mini_bingo_card and numbers_called.
#          Produces True if one or more rows, columns, or diagonals have all
#          negative numbers. Otherwise, False is produced.
# Effects: Mutates mini_bingo_card so that all values in mini_bingo_card, which
#          are also in numbers_called, are negated. Prints out the mutated
#          mini_bingo_card only if one or more rows, columns, or diagonals have
#          all negative numbers.
# Examples:
# mini_bingo([5,2,9,17,23,26,33,38,44],[5,10,23,31,44]) will print the
# following screen output:
# -5 17 33
# 2 -23 38
# 9 26 -44
# and True is produced.
# mini_bingo([5,2,9,17,23,26,33,38,44],[1,2,3,4,5]) will have no screen output
# and False is produced.

def mini_bingo(mini_bingo_card, numbers_called):
    negate_mini_bingo_card(mini_bingo_card, numbers_called, 0)
    if is_row_negative(mini_bingo_card) == True or\
       is_col_negative(mini_bingo_card) == True or\
       is_diag_negative(mini_bingo_card) == True:
        print mini_bingo_card[0],mini_bingo_card[3],mini_bingo_card[6]
        print mini_bingo_card[1],mini_bingo_card[4],mini_bingo_card[7]
        print mini_bingo_card[2],mini_bingo_card[5],mini_bingo_card[8]
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    bingo_card = map(int, sys.argv[1].split())
    numbers_drawn = map(int, sys.argv[2].split())
    mini_bingo(bingo_card, numbers_drawn)
