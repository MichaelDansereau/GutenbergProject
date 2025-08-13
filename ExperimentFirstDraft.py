#open the file in read mode
with open('../Texts/The Meditations of the Emperor Marcus Aurelius Antoninus by Marcus Aurelius.txt', encoding = 'utf-8') as file:
    # Read the contents of the file
    content = file.read()

#take user input for specifications about the quote being sought
authors = []
keywords = []

i = False
while i == False:
    authors.append(input("Enter Author Name- if no more authors to add, type 'Done': "))
    if authors[-1] == "Done":
        authors.pop()
        i = True

i = False
while i == False:
    keywords.append(input("Enter Keywords- if no more keywords to add, type 'Done': "))
    if keywords[-1] == "Done":
        keywords.pop()
        i = True

#split the string containing the text on all instances of whitespace
#the resultant list should contain each word as a string of its own
srch = content.split()

#results list contains a list of every quote to be output
numquotes = 0
results = []

results = []
numquotes = 0

#the below loop iterates through the text and adds every applicable quote to the results list
for idx, srchi in enumerate(srch):
    #check each word in srch against the keywords
    if srchi in keywords:
        #find start of sentence
        start_idx = 0
        for rvrsi in range(idx, -1, -1):
            if "." in srch[rvrsi]:
                start_idx = rvrsi + 1
                break

        #collect sentence words until the next period
        sentence_words = []
        for fwd_i in range(start_idx, len(srch)):
            sentence_words.append(srch[fwd_i] + " ")
            if "." in srch[fwd_i] or "?" in srch[fwd_i] or "!" in srch[fwd_i]:
                break
        sentence_words.append("\n")
        results.append(sentence_words)
        numquotes += 1    

#formatting output to look nice
output = ""
for x in results:
    for y in x:
        output += y
        
print(output)
