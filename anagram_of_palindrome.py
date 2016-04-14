"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""
    


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1

    values = letter_count.values()
    odd = 0
    for num in values:
        if num % 2 != 0:
            odd = odd + 1
        else:
            continue
    if odd > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
