

# In this Kata, you will be given a lower case string and your task will 
# be to remove k characters from that string using the following rule:

# RULES
# - first remove all letter 'a', followed by letter 'b', then 'c', etc...
# - remove the leftmost character first.


# For example: 
# solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
# solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
# solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
# solve('abracadabra', 8) = 'rdr'
# solve('abracadabra',50) = ''


def solve(st, k):
    """Given a string remove k characters following the rules."""

    occurences = {}
    #adding occurences in the string to the dictionary
    for letter in st:
        count = st.count(letter)
        occurences[letter] = count
        s = sorted(occurences.items()) #list
    # print(type(s))

    for t in s:
        # print(type(t)) # tuple
        for char in t:
            print(char)

    #sort the dictionary in alphabetical order 
    #remove given letter 
    #return the string with the letters removed. 



print(solve('abracadabra', 1)) #,'bracadabra'
print(solve('abracadabra', 2)) #,'brcadabra'
print(solve('abracadabra', 6)) #,'rcdbr'
print(solve('abracadabra', 8)) #,'rdr'
print(solve('abracadabra', 50)) #,''