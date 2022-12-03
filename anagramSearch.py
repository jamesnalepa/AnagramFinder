# JAMES NALEPA
# Python code to find all anagrams of a given word using a dictionary file

def anagramSearch(word):
    w = [''] * len(word)                                                                                 # characters of the given word
    f = []                                                                                               # found characters when searching later on
    anagrams = []                                                                                        # final anagrams to return when finished

    for index, ele in enumerate(word):                                                                   # filling w
        w[index] = ele

    print(w, end='  ')
    print(len(word), " characters\n")

    with open(r"C:\Users\james\PycharmProjects\codeKataMay262022\dictionary.dat") as file:

        for line in file:                                                                                # looping through every line in the file
            line = line.rstrip()                                                                         # the line includes a NEWLINE that you have to strip to make sure the size is correct
            f.clear()
            found = 0
            if len(word) != len(line):                                                                   # if the line isn't the same length as the word it can't be the word
                continue
            for c in w:                                                                                  # looping through every character in the given WORD
                for char in line:                                                                        # looping through every character in the LINE
                    if c == char and c not in f:                                                         # if char is c
                        found += 1                                                                       # counting the found characters
                        f.append(c)                                                                      # adding the found character to f

            if found == len(word):                                                                       # if the number of found characters equals the size of the original word
                anagrams.append(line.rstrip('\n'))                                                       # add the word to list of anagrams

    return anagrams

# DRIVER CODE
word = input("Enter a word: ")
print("All Anagrams of your word: ", anagramSearch(word))
