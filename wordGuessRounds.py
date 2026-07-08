import os
def word_guessing_game():
    def display_word(word, guessed_letters):
        return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    
    def get_allowed_guesses(word):
        unique_letters = len(set(word.lower()))
        return unique_letters + 2
    
    def play_round(guesser, giver):
        word = ""
        while len(word) <= 1 or not word.isalpha():
            word = input(f"{giver}, enter a word (at least 2 letters) for {guesser} to guess: ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        input(f"{guesser}, press Enter to start...")
        
        guessed_letters = set()
        allowed_guesses = get_allowed_guesses(word)
        guesses_left = allowed_guesses
        
        while guesses_left > 0:
            print(f"\nWord: {display_word(word, guessed_letters)}")
            print(f"Guesses left: {guesses_left}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
            
            guess = input(f"{guesser}, guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            
            guessed_letters.add(guess)
            
            if guess not in word:
                guesses_left -= 1
                print(f"Wrong! {guess} is not in the word.")
            else:
                print(f"Correct! {guess} is in the word.")
            
            if all(letter in guessed_letters for letter in word):
                print(f"\n{guesser} wins! The word was: {word}")
                return guesser, giver
        
        print(f"\n{guesser} couldn't guess the word. The word was: {word}")
        return giver, guesser
    
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    
    current_guesser = player2
    current_giver = player1
    
    while True:
        print(f"\n*** {current_guesser} vs {current_giver} ***")
        winner, loser = play_round(current_guesser, current_giver)
        
        if winner == current_giver:
            print(f"\n🎉🎉🎉 Game Over! {winner} wins! {loser} loses!")
            break
        else:
            current_guesser, current_giver = current_giver, current_guesser

word_guessing_game()