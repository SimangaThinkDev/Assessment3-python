import re

def generate_fibonacci_sequence(n: int) -> list:
    """
    Generates the first n numbers in the Fibonacci sequence.
    The Fibonacci sequence starts with 0 and 1.
    Example: n=5 -> [0, 1, 1, 2, 3]
             n=1 -> [0]
             n=0 -> []

    Args:
        n (int): The number of Fibonacci numbers to generate. Must be non-negative.

    Returns:
        list: A list containing the first n Fibonacci numbers.
              Returns an empty list if n is 0 or negative.

    Learning Outcomes: Functions, Loops (1D), Control Flow, Data Structures (lists), Problem-solving.
    """
    # TODO: Implement this function
    lst = list()
    lst.extend( [0, 1] )
    if n <= 0: return []
    if n == 1 or n == 2: return lst[:n]
    
    while len( lst ) < n:
        lst.append( lst[-1] + lst[-2] )

    return lst


def is_palindrome_advanced(text: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case, spaces, and punctuation.
    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same backward as forward.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the text is a palindrome after cleaning, False otherwise.

    Learning Outcomes: Functions, String Manipulation, Control Flow, Problem-solving.
    Hint: You might find string methods like .lower(), .isalpha(), or the `re` module useful.
    """
    # TODO: Implement this function
    from string import ascii_lowercase
    text = text.lower().strip()
    new_string = ""
    for char in text:
        if char in ascii_lowercase:
            new_string += char
    
    return new_string == new_string[::-1]


def find_elements_in_matrix_greater_than_value(matrix: list, value: int or float) -> list:
    """
    Given a matrix (list of lists of numbers) and a value, returns a list
    of all elements in the matrix that are strictly greater than the given value.
    The order of elements in the returned list does not matter.

    Args:
        matrix (list of list of int/float): The input matrix.
        value (int/float): The threshold value.

    Returns:
        list: A list of numbers from the matrix that are greater than 'value'.
              Returns an empty list if the matrix is empty or no elements are greater.

    Learning Outcomes: Functions, Loops (2D - nested), Control Flow, Data Structures (lists).
    """
    # TODO: Implement this function
    result = []
    for line in matrix:
        for num in line:
            if num > value:
                result.append( num ) 
    
    return result


def format_names_list(names_list: list) -> list:
    """
    Takes a list of strings, where each string is a full name "FirstName LastName".
    Returns a new list of dictionaries, where each dictionary has keys
    'first_name' and 'last_name' with the corresponding values.

    Example: ["Ada Lovelace", "Charles Babbage"] ->
             [{'first_name': 'Ada', 'last_name': 'Lovelace'},
              {'first_name': 'Charles', 'last_name': 'Babbage'}]

    Args:
        names_list (list of str): A list of full names.

    Returns:
        list of dict: A list of dictionaries, each representing a parsed name.
                      Returns an empty list if the input list is empty.
                      Assumes valid "FirstName LastName" format for each string.

    Learning Outcomes: Functions, Loops (1D), String Manipulation (split), Data Structures (lists, dictionaries).
    """
    # TODO: Implement this function
    
    result = list( dict() )
    
    for name in names_list:
        split_name = name.strip().split( " " )
        if len( split_name ) == 0 : continue
        if len( split_name ) == 1 :
            result.append( 
                          { 
                           "first_name" : split_name[0], 
                           "last_name"  : ""
                           }, 
                        )
        if len( split_name ) == 2 :
            result.append( 
                          { 
                           "first_name" : split_name[0], 
                           "last_name"  : split_name[1],
                           }, 
                        )

    return result


def sum_diagonals_square_matrix(matrix: list) -> int or float:
    """
    Calculates the sum of the elements on the main diagonal and the anti-diagonal
    of a square matrix.
    - Main diagonal: (0,0), (1,1), (2,2), ...
    - Anti-diagonal: (0,n-1), (1,n-2), ..., (n-1,0)
    If the matrix has an odd dimension, the center element (which is on both diagonals)
    should only be counted once in the total sum.

    Args:
        matrix (list of list of int/float): A square matrix.

    Returns:
        int/float: The sum of the diagonal elements.
                   Returns 0 if the matrix is empty.
                   Returns 0 if the matrix is not square (e.g., rows have different lengths,
                   or number of rows != number of columns).

    Learning Outcomes: Functions, Loops (1D or 2D), Control Flow, Data Structures (lists of lists), Problem-solving.
    """
    # TODO: Implement this function
    if len( matrix ) <= 0 : return 0
    if len( matrix ) != len( matrix[0] ): return 0
    
    # Even row length
    if len( matrix[0] ) % 2 == 0 :
        lest  = [ matrix[i][i] for i in range( len(matrix) ) ]
        lest += [ matrix[i-1][i-1] for i in range( len(matrix), 0, -1 ) ]
        return sum( lest )
    else:
        x = len( matrix[0] ) // 2 + 1
        lest = []
        lest.append( matrix[x][x] )
        lest  += [ matrix[i][i] for i in range( len(matrix) ) if i != x ]
        lest += [ matrix[i-1][i-1] for i in range( len(matrix), 0, -1 ) if i != x ]
    
    return sum(lest)

print( sum_diagonals_square_matrix( [[1, 2],
                   [3, 4]]) )