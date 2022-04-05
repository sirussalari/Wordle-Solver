# Wordle-Solver

This Python program will solve the game of Wordle. In case you're unaware, Wordle is a computer game played in a browser. In the game, the player gets 6 chances to correctly guess a 5 letter word. With each guess, the player gets hints. There are 3 hints given to players. One of the hints given is whether a given letter is in the correct word, another hint lets the player know if a letter is in the word but in the wrong spot on their guess, and finally there's a hint where the player knows the exact position of a letter if it was in the word they guessed. The link to the website where you can play Wordle is: https://www.nytimes.com/games/wordle/index.html

Before I started programming, I needed to find a way of having a source of English words that the program would be able to pull from. I found a GitHub repository that has a publicly available text file containing hundreds of thousands of English words. The owner of the repository pulled these words from an excel file provided by infochimps. Copyright belongs to infochimps.
The link to the repository where I downloaded the text file is: https://github.com/dwyl/english-words

The link to the infochimps dataset is: https://web.archive.org/web/20131118073324/http://www.infochimps.com/datasets/word-list-350000-simple-english-words-excel-readable

After I downloaded the text file onto my computer, I then used Terminal to output all the words with only 5 letters into a new text file. 
The exact command to use is: grep '^......$' words_alpha.txt | less > fiveLetter.txt
After running this command, you now have a new text file that contains all of the words from the original file that are only 5 letters long. This newly created text file is what I then used in my Python program.

The program contains only one function, and the function takes 3 arguments.

The intended use is to first enter no arguments, and then enter the ouput given into the Wordle webpage. After Wordle gives you feedback on the hints, you then enter in the appropiate arguments, and keep repeating this process till you get the correct word.

If you don't enter any arguments, then the program will output a random word from the text file.

The first argument is "none", which is supposed to be an array. The user inputs letters into this array that are not contained in the correct word. Each letter is its own element. For example, if you know that the letters "t" and "s" are not in the word, then you would enter: '['t','s']'. This tells the program to exclude all words that contain these letters from being chosen as a guess.

The second argument is "match" which is supposed to be a dictionary. The user inputs a letter as a key, and then the corresponding value is the index at which the letter occurs in the correct word. The corresponding value to a key can either be an integer or an array. For example, let's say that you know that the letter "e" appears in the word at the 1st index. You would then enter: '{"e": 1}'. Then, let's say that after another guess, you discover that the letter "e" is also in the 2nd index, then you would simply enter: '{"e": [1,2]}'. This tells the program to include all the words that have the correct letter at the correct index.

The last argument is "close" which is also supposed to be a dictionary. The user inputs a letter as a key, and then the corresponding value is the index at which the letter DOES NOT occur in the correct word. Similar to "match" argument, the values can either be integers or arrays. For example, let's say that you know "p" appears in the word but is not in the 4th index. You would then enter: '{"p": 4}'. Then, let's say that after another guess, you discover that "p" is not in the 4th index nor the 0th index. You would then enter: {"p": [0, 4]}'. This tells the program to include all the words that have these letters but that are not in the index specified.

The program is set up to take all possible combinations of arguments. This means that you can enter no arguments, all arguments, 2 arguments, or 1 argument. Unless there are no arguments given, all of the valid words end up in an array at which the program chooses a random word from this array. If no arguments are given, the program outputs a random word from the entire text file.

I added some cool features that are not functional to the program, but could be useful if you're curious. One of the features includes an ouput of the runtime of the program. Another feature is that the search space is outputted, as well as the percentage chance that the outputted word is correct. I also included the ability to be able to run this program directly from the terminal through the use of the sys and json libraries.

Finally, as a side note: I constantly modify the fiveLetter.txt file. Not all of the words in this text file are in Wordle's list of possible words. To address this issue, each time that I enter an outputted word and Wordle tells me that it's not in their list, I then run a command in the Terminal to remove this word from the text file permanently.
The exact command that I use is: sed -i '' '/word/d' fiveLetter.txt
Replace "word" with the word that you are trying to delete.
