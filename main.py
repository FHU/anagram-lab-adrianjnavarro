#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    #remove the white space with this code!
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    #check for empty space
    if not word1 or not word2:
        return False
    #Find the length of both words and compare them while also finding if they have the same letters. 
    if len(word1) != len(word2):
        return False
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    #If they have simmillar letters and the same length print true otherwise false. 
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False

if __name__ == '__main__':
#This is where the input of the code will go before being put into the def anagram(word1, word2)
    word1 = input()
    word2 = input()
#Once the code above finishes we will bring it out of its function with result and then print it as normal. 
    result = anagram(word1, word2)
    print(result)
