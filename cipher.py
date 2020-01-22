'''
Use a substitution cipher algorithm to encrypt and decrypt a plain text message.
'''

import doctest

def substitutionEncrypt (plainText, psw):
    '''
    (str, str) -> (str)

    This function returns the cipherText from the plainText string using the password (psw) for the encryption.
    You start with the plainText given in the parameters and look at each character and make it lower case, and remove the spaces,
    then add the character to the empty cipherText string to create the encryption.

    Example:
    
>>> substitutionEncrypt('the quick browon fox', 'ajax')
'qdznrexgjoltlkblu'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    plainText = plainText.lower()
    plainText = removeMatches(plainText, ' ')
    cipherText = ''
    key = genKeyFromPass(psw)
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def substitutionDecrypt(cipherText, psw):
    '''
    (str, str) -> (str)
    
    This function returns the plainText from the cipherText string using the password (psw) for the encryption.
    You start with the cipherText this time given in the parameters and look at each character and make it lower case, and remove the spaces, just as done before,
    then add the character to the empty plainText string to create the original text from the encryption.

    Example:
    
>>> substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
'thequickbrownfox'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = cipherText.lower()
    cipherText = removeMatches(cipherText, ' ')
    plainText = ''
    key = genKeyFromPass(psw)
    for ch in cipherText:
        idx = key.find(ch)
        plainText =  plainText + alphabet[idx]
    return plainText

def genKeyFromPass(password):
    '''
    (str) -> (str)

    This function is from the textbook and it calls upon removeDupes nad removeMatches. It is supposed to looked at the key from the alphabet
    and create the key to use for the encrption which we later refer to as the password (psw).
    Returns the key, has no side effects.

    Example:

>>> genKeyFromPass('ajax')
'ajxyzbcdefghiklmnopqrstuvw'
    '''
    key = 'abcdefghijklmnopqrstuvwxyz'
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def removeDupes(myString):
    '''
    (str) -> (str)

    Returns the new string after looking through each character in the original string and removing duplicte characters.
    No side effects.

    Example:

>>> removeDupes('topsecret')
'topsecr'
    '''
    newStr = ''
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr
    
def removeMatches(myString, removeString):
    '''
    (str, str) -> (str)

    This function returns the new string that does not contain the characters in the other string.
    If the character is in the myString, but not in the removeString, then it is added to the newStr. If the character is in both, then it is not added.

    Example:
>>> removeMatches('abcdefghijklmnopqrstuvwxyz','topsecr')
'abdfghijklmnquvwxyz'
    '''
    newStr = ''
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def main():
    '''
    This function in the main function that calls upon substitutionEncrypt and substitutionDecrypt to create an encrypted message with the input values for the message and the password used.
    Side effects of this function is printing the cipherText and the Plaintext. This function returns None.
    
    '''
    plainText = input('Enter a message to encrypt: ')
    psw = input('Enter a password you would like to use in this encryption: ')
    cipherText = substitutionEncrypt(plainText, psw)
    print(cipherText)
    plainText = substitutionDecrypt(cipherText, psw)
    print(plainText)
    return None

print(doctest.testmod())

main() 
