# Hangman-game
Python-based version of the beloved game: Hangman!


## requirements
**python:** 3.6 or higher
## Explanation & Details

Like in every other hangman game, here you have to guess a secret word.

first, you will need to insert a path to txt file containing a bunch of words seperated by new-lines (I will provide one for you so you won't need to work too hard). The game will choose a random word from that file for you to guess.

After doing so, the game will start and you can start guessing letters according to the number of letters left to discover in the word - ***each letter at the time***.

For each guess (whether correct or not) the game will display an appropriate output with the help of a suitable message and an ASCII drawing (if the guess is incorrect).

Note that you have 6 attempts to guess the word. After the trials are over, the chosen word will be displayed. Finally, whether you won or not the game will give you the option to play again.

The program knows how to deal with incorrect input at all stages of reception.

## Appendix
The game is text-interface based. 

This project is based on the rules of the original game (Hangman) as you can see in https://www.wikihow.com/Play-Hangman 


## Run Locally

Clone the project

```bash
  git clone https://github.com/netanelazuz/Hangman-game.git
```

Go to the project directory

```bash
  cd Hangman-game
```

Run the game

```bash
  py hangman.py
```




## Authors

- [@netanelazuz](https://www.github.com/netanelazuz)

