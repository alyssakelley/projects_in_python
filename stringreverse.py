'''
String Reversal. Project 5-2

Author: Alyssa Kelley

Credits: None

Write and implement iterative and recursive algorithms to reverse a string.

''' 
import doctest

def strReverseI(s):
    '''
    (str) -> (str)
    Returns the reverse of the string input. This function finds the reverse string
    via an interative implementation.


    NOTE TO MYSELF: I could also have chosen to do a while loop being

    (s[n:] != ''):

    This is using a while loop and as long as the slice of the string is not an empty string,
    it will continue to run the loop. As soon as the slice becomes an empty string,
    it will stop the loop and you will have the reverse string.

    Examples:

    >>> strReverseI('hello, world')
    'dlrow ,olleh'
    >>> strReverseR('')
    ''
    >>> strReverseR('a')
    'a'
    '''
    result = ""
    n = 0
    for i in range(1, len(s) + 1):
        result += s[len(s) - i]
    return result
        
def strReverseR(s):
    '''
    (str) -> (str)
    Returns the reverse of the string input. This function finds the reverse string
    via recuersion. The base case would be an empty string so the function would still return out an empty string and not have any errors.
    After we can confirm the string is not empty, we return the last element of the string, followed by
    the string without that last element/character. Since this continues to call upon itself, it will continue to cut the string
    of the "last" element to grow the reverse string. 

    Examples:

    >>> strReverseR('hello, world')
    'dlrow ,olleh'
    >>> strReverseR('')
    ''
    >>> strReverseR('a')
    'a'
    ''' 
    if (len(s) == 1) or (len(s) == 0):
        return s
    else:
        return strReverseR(s[1:]) + s[0]

def main():
    '''
    () -> None
    This main function is to call upon the iterative reversal function strReverseI and the recursive reversal function strReverseR.
    It returns None and has two print side effects of the doctest and then the original string after being reversed twice. 
    
    '''
    print(doctest.testmod())
    s = input('Enter a string to be reversed: ')
    print(strReverseR(strReverseI(s)))
    return None

#main()


def test_reverse(f):
    '''
    function ->

    '''

    list = (
            ('', ''),
            ('a', 'a'),
            ('aaaa', 'aaaa'),
            ('abc', 'cba'),
            ('hello', 'olleh'), ('racecar', 'racecar'),
            ('testing123', '321gnitset'), ('#CIS 210', '012 SIC#'), ('a', 'b')
            )
    
    for i in list:
        
        if f(i[0] == i[1]):
            
            print("Checking", f(i[0]),"... its value", f(i[1]), "is correct!")
        
        else:
        
            print("Checking", f(i[0]), "... Error: has wrong value", f(i[1]), "expcected")
        
    return None







