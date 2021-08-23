# Vocabulary List Generator
## Introduction

Ebbinghaus found the forgetting curve to be exponential in nature. Memory retention is 100% at the time of learning any particular piece of information. However, it drops rapidly to 40% within the first dew days. After which, the declination of memory retention slows down again. 
He went on to hypothesize that basic training in mnemonic techniques can help overcome those differences in part. He asserted that one of the best methods for increasing the strength of memory is: repetition based on active recall (especially spaced repetition)

His premise was that each repetition in learning increases the optimum interval before the next repetition is needed. He discovered that information is easier to recall when it's built upon things you already know, and the forgetting curve was flattened by every repetition. It appeared that by applying frequent training in learning, the information was solidified by repeated recalling.
By spacing our repetition by a day, 3 days, then a week, we allow ourselves to forget some of the information such that when we revise the topic – through active recall – it takes active brain power.

I wanted to apply this result to my vocabulary list generator by combining new vocabularies and the ones for repeatition.

## The Principle of this program
New words are added by user. Those words are stacked up in the database. The program adds column of the date when the words are added. Based on the date information and a repetition space, the program extracts vocabulary list for today. 

## How to Use
1. Create a folder you want to work with vocabulary. In this folder, you will save new word list. Word database and word list for today will be generated and saved in this folder. Once you made a folder, change the folder path in the program. 
2. Create a new word list in .txt file or .xlsx file. 
3. 
If you use .txt file, you can use ; as a seperator.
2. Change the file name in the filename() function.
3. Change the directory. 
4. Run the Program.

* This program is designed to use everyday.
* Once you create a Database file, the program will use the DB file the next day.
