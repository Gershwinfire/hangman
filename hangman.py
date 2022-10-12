from enum import Enum
from dataclasses import dataclass
import random



class Letters(Enum):
    a = ('🄰', 'A')
    b = ('🄱', 'B')
    c = ('🄲', 'C')
    d = ('🄳', 'D')
    e = ('🄴', 'E')
    f = ('🄵', 'F')
    g = ('🄶', 'G')
    h = ('🄷', 'H')
    i = ('🄸', 'I')
    j = ('🄹', 'J')
    k = ('🄺', 'K')
    l = ('🄻', 'L')
    m = ('🄼', 'M')
    n = ('🄽', 'N')
    o = ('🄾', 'O')
    p = ('🄿', 'P')
    q = ('🅀', 'Q')
    r = ('🅁', 'R')
    s = ('🅂', 'S')
    t = ('🅃', 'T')
    u = ('🅄', 'U')
    v = ('🅅', 'V')
    w = ('🅆', 'W')
    x = ('🅇', 'X')
    y = ('🅈', 'Y')
    z = ('🅉', 'Z')


    @property
    def unused(self):
        return self.value[1]

    @property
    def dead(self):
        return self.value[0]



class Player:

    def __init__(self):
        self.name = self.get_name()
        self.score = 0

    def get_name(self):

        while True:

            user_name = input("Your Name:  ")
            confirmation = input(f"Your name is {user_name}? Y/N: ")
            confirmation = confirmation.lower().strip()

            if confirmation == "y":
                return user_name


class GameWord:

    def __init__(self):

        self.word = self.populate()
        ###print(self.word)


    def populate(self):

        game_words = []

        with open('words.txt') as file:

            for line in file:
                game_words.append(line.rstrip('\r\n'))

            word = random.choice(game_words)
            return word

    def print_word(self):
        print(self.word)


class TheMan:

    def __init__(self):

        self.body_parts = ['O', '|', '/', '\\','/', '\\']
        self.printed_body
        
        '''What does the printed body look like?
                      12O35
                      /2|4\\
                      1/3\5
        '''         

class UnusedLetters:

    def __init__(self):
        
        self.live_letters = []
        self.initialize_live_letters()
        self.dead_letters = []
        self.board_letters = []
        self.populate_board_letters()
        

    def initialize_live_letters(self):

        for letter in Letters:
            self.live_letters.append(letter)
    
    def live_to_dead(self, input_letter):
        
        input_letter = input_letter.upper()
        for letter in Letters:
            if input_letter == letter.unused:
                input_letter = letter
            else:
                pass
        self.live_letters.remove(input_letter)
        self.dead_letters.append(input_letter)
        self.populate_board_letters()
    
    def populate_board_letters(self):

        if len(self.board_letters) > 0:
            self.board_letters = []

        for letter in Letters:
            if letter in self.live_letters:
                self.board_letters.append(letter.unused)
            elif letter in self.dead_letters:
                self.board_letters.append(letter.dead)
            else:
                print("ERROR: ONE LETTER DID NOT APPEND TO GAME BOARD")

    def print_board_letters(self):
        print(self.board_letters)
        

            



class Board:

    def __init__(self, player, gameword, game_letters):

        self.player = player
        self.gameword = gameword
        self.game_letters = game_letters
        self.wrong_guesses = 0
        self.display = ""
    


    def display_game_word(self):

        display_word = ''
        for letter in self.gameword.word:
            new_letter = self.convert_input(letter)
            if new_letter in self.game_letters.dead_letters:
                display_word += f"{letter} "
            elif new_letter in self.game_letters.live_letters:
                display_word += "_ "
            else:
                print("ERROR: That letter isnt found")
        print(display_word)
        
        self.display = display_word
        return display_word
                
    def convert_input(self, input_letter):

        input_letter = input_letter.upper()
        for letter in Letters:
            if input_letter == letter.unused:
                input_letter = letter
                return input_letter
            else:
                pass

    def guess_letter(self):

        while True:
            letter = input("GUESS: ")

            if len(letter) == 1:
                break
            print("Please Only Choose One Letter at a Time")
        letter = letter.strip()
        return letter


    def compare_letter(self, letter):

        if self.convert_input(letter) in self.game_letters.live_letters:
            if letter in self.gameword.word:
                print("Found letter")
                self.game_letters.live_to_dead(letter)

            elif letter not in self.gameword.word:
                #Hang the man
                print("Letter not in Word")
                self.game_letters.live_to_dead(letter)
                self.wrong_guesses += 1

            else:
                print("Somehow Letter not Found Anywhere")
        else:
            print(f"{letter} was already Guessed. Please Pick a different Letter.")
