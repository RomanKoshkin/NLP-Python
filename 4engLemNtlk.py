import nltk
from xlrd import open_workbook
from xlutils.copy import copy
from txtdataENG import Qwer

lem = nltk.WordNetLemmatizer()

#read in the text
f = open('Eng_plaintext.txt', 'r')
source_text = f.read()
f.close()

# tokenize and POS-tag it
tokenized_text = nltk.word_tokenize(source_text)
a = nltk.pos_tag(tokenized_text)

# save POS-tagged text to xlsx file:
rb = open_workbook("test.xls")
wb = copy(rb)
sheet = wb.get_sheet(0)
for i in range(len(a)):
    sheet.write(i, 0, a[i][0])
    sheet.write(i, 1, a[i][1])
    Flag = ((list(a[i][1]))[0]).lower() # take the first char of the tag and convert to lowercase
    sheet.write(i, 2, Flag)
    lemma = lem.lemmatize(a[i][0], 'v' if Flag == 'v' else 'n')
    sheet.write(i, 3, lemma)


RF = Qwer()     # instantiate an instance of class Qwer from the imported module (see imports)
x = rb.sheet_by_index(0).col_values(3, 0, rb.sheet_by_index(0)._dimnrows)
x = list(set(x))
for i in range(len(x)):
    sheet.write(i, 4, x[i])
    q = RF.RequestFreq(x[i])
    print(q)
    sheet.write(i, 5, q)

wb.save('test.xls')
print(x)

