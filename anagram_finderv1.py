
def check_validity(wrd):
    with open("dict.txt") as source:
        while 1:
            line = source.readline()
            if not line:        #EOF Check
                break
            if wrd.lower() == line.strip():
                return True
    return False

def anagram(word):
    letters = list(word.lower())
    letters.sort()
    anagrams = []
    with open("dict.txt") as source:
        while 1:
            line = source.readline()
            #EOF Check
            if not line:
                break

            line = line.strip()
            line_alpha = list(line)
            line_alpha.sort()
            #check if all letters match but the words are not same.
            if line_alpha == letters and line != word:
                anagrams.append(line)

    return anagrams

#driver program

if __name__ == "__main__":

    while True:
        print("Enter any Valid english word.")
        in_word = input()
        print(' ')    
        if not check_validity(in_word):
            print("It is not a valid dictionary word.\nProcessing anyway...\n")

        words = anagram(in_word)
        count = len(words)
        if count:
            print("We found", count, "anagrams for the word'",in_word.capitalize(),"'.")
            for word in words:
                print(word.capitalize())
        else:
            print("Sorry! No anagrams found for given word :(") 


        print("\nCheck more words?(Y/N)")
        if input() in ["n", "N"]:
            break
