# Vocabulary List Generator
## Introduction

Ebbinghaus found the forgetting curve to be exponential in nature. Memory retention is 100% at the time of learning any particular piece of information. However, it drops rapidly to 40% within the first dew days. After which, the declination of memory retention slows down again. 
He went on to hypothesize that basic training in mnemonic techniques can help overcome those differences in part. He asserted that one of the best methods for increasing the strength of memory is: repetition based on active recall (especially spaced repetition)

His premise was that each repetition in learning increases the optimum interval before the next repetition is needed. He discovered that information is easier to recall when it's built upon things you already know, and the forgetting curve was flattened by every repetition. It appeared that by applying frequent training in learning, the information was solidified by repeated recalling.
By spacing our repetition by a day, 3 days, then a week, we allow ourselves to forget some of the information such that when we revise the topic – through active recall – it takes active brain power.

I wanted to apply this result to my vocabulary list generator by combining new vocabularies and the ones for repeatition.

## The Principle of this program
New words are added by user.  The program adds column of the date when the words are added and words are stacked up in the database excel file. Based on the date information and a repetition space, the program extracts vocabulary list for today. 
The file names of Database excel files and newly created words files are identified with the date. I will give you an example how this program works. You add a word list on Aug 25. The program searches database file with the date before; Aug 24, '20210824_Dutch_DB.csv' and put new list and DB file together into new DB file and create new file with the date of today; Aug 25, '20210825_Dutch_DB.csv'. From this file, vocabulary list for today are extracted to '20210825_Dutch_set.csv' file based on designated repetition intervals.

## How to Use
1. Create a folder you want to work with vocabulary. In this folder, you will save a new word list. Word database and word list generated for today is saved in this folder.
2. Create a new word list and save it in .txt file or .xlsx file. 
_txt file_
Words and their meanings are seperated by ;. This text file is converted into DataFrame with two columns.
In my case, I fill up words meaning in Korean. By using regular expressions, this program automatically split latin alphabet and korean letters. In this case, seperator is not needed.
_xlsx file_
Words and their meanings are filled up in two columns.
3. Once you made a word file and a folder to save input file and find output file, change the path in the program. 
 There is a function called [filename]. Change the path after 'filefolder' and file name in new_today. File name is written as 'NewDutchWords.xlsx' and supposed to be updated as yours.
4. Run the Program!
