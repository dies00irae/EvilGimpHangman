# Author: Jake Smith
# Project:  Hangman Game
# Date Created: 4/24/2020
# Domain: evilgimpdesigns (ficticious name)
import sys
import random
import turtle
from turtle import textinput

list_of_words = ('harmony', 'memorization', 'collaborate', 'espionage', 'grogginess', 'glowworm', 'microwave',
                 'razzmatazz', 'rhythm', 'thumbscrew', 'unworthy', 'wristwatch', 'xylophone', 'beekeeper',
                 'knapsack', 'buffalo', 'megahertz', 'pajama', 'haphazard', 'jawbreaker', 'fishhook', 'cobweb',
                 'frazzled', 'numbskull', 'yachtsman', 'xylophone', 'wellspring', 'fluffiness', 'bandwagon')


# need to arrange hangman word in hidden format.
def get_players_word():
    """Assigns hangman word, and arranges it in a players hidden format.  Defaults to index 0."""
    global hangman_word
    hangman_word = random.choice(list_of_words)
    word = ''
    for c in hangman_word:
        word += '_'  # adds _ to hide the word from player.
    return word


# need player UI and interaction
def get_player_choice():
    """Gets players choice and if player already picked the letter it prompts for a new response"""
    while True:
        guess = textinput('Time to Choose', 'Choose a letter:  ')  # Sets up test box to input a letter
        if guess is None:  # quits game if cancel is chosen
            error_turtle.write('You\'re about to quit the game....', align='center', font=('Arial', 22, 'normal'))
            quit_game = textinput('Quit?', 'y or n')  # verifying player wants to quit
            if quit_game is None:  # returns to game
                error_turtle.clear()
                continue
            quit_game = quit_game.lower()
            if quit_game == 'n':  # returns to game
                error_turtle.clear()
                continue
            else:
                sys.exit()  # quits game
        else:
            guess = guess.lower()
        error_turtle.clear()
        if len(guess) > 1:  # This section is for incorrect user input
            error_turtle.write('Error:  Enter only one letter', align='center', font=('Arial', 22, 'normal'))
            continue
        if len(guess) == 0:
            error_turtle.write('Error:  Enter a letter', align='center', font=('Arial', 22, 'normal'))
            continue
        if guess in wrong_letters or guess in players_word:  # decides if letter has already been chosen
            error_turtle.write(f'Error:  You already picked \'{guess}\' dumb ass!!',
                               align='center', font=('Arial', 22, 'normal'))
        else:
            for num in range(97, 123):  # determines if players guess is a letter
                if guess == chr(num):
                    break
            else:
                error_turtle.write(f'Error:  \'{guess}\' is not a letter', align='center', font=('Arial', 22, 'normal'))
                continue
        break
    return guess


# need to see if players guess is correct and add letter(s) to players word
def players_guess(char):
    """Replaces unknown underscores with correctly guessed char or updates wrong guess by 1"""
    count = 0
    global players_word
    temp_players_word = []  # creates a list to add letters instead of underscores
    for letter in hangman_word:  # this loop sees if the player guessed a correct letter
        if char == letter:
            count += 1
    if count == 0:  # increments wrong_guess if the player chose a wrong letter
        global wrong_guess, wrong_letters
        wrong_guess += 1
        wrong_letters += char
        player_hanging(wrong_guess)
        return
    for correct_letter in players_word:  # adds however many correctly guessed letters to the temp list
        temp_players_word += correct_letter
    for key, value in enumerate(hangman_word):  # this replaces the underscore with the correct letter
        if char == value:
            temp_players_word[key] = char
    players_word = ''.join(temp_players_word)  # this takes the temp list and creates a string


# need to decide if game is over
def game_over():
    """Decides if the player has won, lost, or the game is still playing."""
    global players_word
    win = 0
    for i in players_word:
        if i != '_':
            win += 1
    if win == len(players_word):  # runs if player wins
        write_player_word()
        game_over_turtle.color('green')
        game_over_turtle.write('YOU WIN!!!', align='center', font=('segoe print', 36, 'bold'))
        return True
    elif wrong_guess == max_wrong_guess:  # runs if player loses
        game_over_turtle.color('orange')
        game_over_turtle.write('YOU\'RE DEAD!!!', align='center', font=('segoe print', 36, 'bold'))
        players_word = hangman_word
        write_player_word()
        return True
    return False  # only runs if game is still being played.


# need to decide if player wants to play again
def play_again():
    """Determines if player wants to play again"""
    end_game = textinput('Play Again?', 'y or n')
    if end_game.lower() == 'y':
        game_over_turtle.clear()
        return True
    return False


# draw the hangman noose
def draw_hangman():
    """Draws the initial hang man noose"""
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.goto(-100, 350)
    title_turtle.color('purple')
    title_turtle.write('Evil Gimp\'s Hangman Game', align='center', font=('segoe print', 22, 'normal'))

    hangman_turtle.speed(500)
    hangman_turtle.hideturtle()
    hangman_turtle.backward(200)
    hangman_turtle.forward(100)
    hangman_turtle.left(90)
    hangman_turtle.forward(320)
    hangman_turtle.right(90)
    hangman_turtle.forward(100)
    hangman_turtle.right(90)
    hangman_turtle.forward(25)


# player hanging
def player_hanging(num):
    """Slowly hangs player as wrong guesses increases"""
    hangman_turtle.color('red')
    if num == 1:
        hangman_turtle.left(80)
        for x in range(27):
            hangman_turtle.forward(10)
            hangman_turtle.right(20)
        hangman_turtle.left(100)
    elif num == 2:
        hangman_turtle.forward(10)
        hangman_turtle.left(35)
        hangman_turtle.forward(50)
        hangman_turtle.backward(50)
    elif num == 3:
        hangman_turtle.right(70)
        hangman_turtle.forward(50)
        hangman_turtle.backward(50)
    elif num == 4:
        hangman_turtle.left(35)
        hangman_turtle.forward(80)
    elif num == 5:
        hangman_turtle.left(35)
        hangman_turtle.forward(70)
        hangman_turtle.backward(70)
    else:
        hangman_turtle.right(70)
        hangman_turtle.forward(70)


# Write player word on turtle screen
def write_player_word():
    """Displays players hidden word on the screen"""
    player_turtle.clear()
    player_turtle.hideturtle()
    player_turtle.penup()
    player_turtle.goto(-100, -50)
    player_turtle.write(' '.join(players_word), align='center', font=('Arial', 22, 'normal'))


# Display the wrong letters selected on turtle
def write_wrong_letters():
    """Displays the wrong letters chosen on the screen"""
    wrong_letter_turtle.clear()
    wrong_letter_turtle.hideturtle()
    wrong_letter_turtle.penup()
    wrong_letter_turtle.goto(-100, -100)
    wrong_letter_turtle.write(f'The incorrect letters used are:  {wrong_letters}',
                              align='center', font=('Arial', 18, 'normal'))


# set up game over turtle
def over_turtle():
    """displays a win or loss on the screen"""
    game_over_turtle.penup()
    game_over_turtle.hideturtle()
    game_over_turtle.goto(-125, 100)


# set up error turtle
def entry_error_turtle():
    """displays any input errors on the screen"""
    error_turtle.hideturtle()
    error_turtle.penup()
    error_turtle.goto(-100, -150)


wrong_letters = []
hangman_word = []
players_word = get_players_word()
max_wrong_guess = 6
wrong_guess = 0
hangman_turtle = turtle.Turtle()
player_turtle = turtle.Turtle()
title_turtle = turtle.Turtle()
wrong_letter_turtle = turtle.Turtle()
game_over_turtle = turtle.Turtle()
error_turtle = turtle.Turtle()

draw_hangman()
over_turtle()
entry_error_turtle()

while True:
    write_player_word()
    write_wrong_letters()
    players_guess(get_player_choice())

    if game_over():
        if not play_again():
            break
        else:
            wrong_letters = []
            wrong_guess = 0
            players_word = get_players_word()
            hangman_turtle.reset()
            draw_hangman()
