def fn(word, arr, x=''):    
    for i in word:
        st = x+i
        temps = word.copy()
        temps.remove(i)
        if len(word) == 1:
            arr.append(st)    
        fn(temps,arr,st)




def check(arr,checked_words):
    flag = 0
    #checking with word list and printing:
    with open("dict.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            #process:
            for i in arr:
                if i == line.strip().upper():
                    flag +=1        #anagrams counter
                    checked_words.append(i)
    return flag

def check_validity(wrd):
    with open("dict.txt") as source:
        while 1:
            line = source.readline()
            if not line:
                break
            if wrd == line.strip().upper():
                return 1
    return 0


#main program
def main():
    arr=[]
    checked_words=[]
    valid = 1
    #input validity
    while(valid):
        in_word = input("Enter a valid Engish Word:")
        in_word = in_word.strip().upper()
        valid = 0
        if not check_validity(in_word):
            print("Your word is not a valid english word")
            print("Do you want to correct the entry or continue anyway?")
            ch = input("1.Correct \n2.Continue Anyway\n")
            if ch.strip() == '2':
                valid = 0
            else:
                valid = 1

    #processing:
    letters = list(in_word)
    fn(letters,arr)                                  #all possibles anagrams
    
    counter = check(arr,checked_words)               #checks dictionary for meaningful words
    checked_words=set(checked_words)                 #removing repetition
    try:
        checked_words.remove(in_word)                    #removing given word
    except:
        pass

    #Displaying Results: 
    if counter:
        print('Hurray! We found ',len(checked_words),' anagrams for your word "',in_word,'" :')
        for p in checked_words:
            print(p.capitalize())
    else:
        print("Sorry, No anagrams are found for the given word :(")


#Start of program:

yes = 1
while (yes):
    main()
    yn = input("\nDo you want me to find more anagrams for you? (Y or N)\n")
    if yn.lower() in ['n','no','nope']:
        yes = 0
        print("***THANK YOU***")
    else:
        print("=========================================================\n\n")
       


#REFRENCE For WORD-LISTS
#  http://www.gwicks.net/dictionaries.htm : (ENGLISH - 194,000 words)

