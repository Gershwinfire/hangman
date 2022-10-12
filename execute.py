from hangman import GameWord, Player, UnusedLetters, Board


player1 = Player()
game_word  = GameWord()
game_letters = UnusedLetters()

game_word_length = len(game_word.word)

game_board = Board(player1, game_word, game_letters)

while True:

    game_board.game_letters.print_board_letters()
    display_word = game_board.display_game_word()
    if '_' not in display_word:
        print("CONGRATULATIONS")
        break
    game_board.compare_letter(game_board.guess_letter())
    if game_board.wrong_guesses >= 6:
        print(f"MAN WAS HANGED!\nGAME OVER\nGame Word: {game_word.word}")
        break
