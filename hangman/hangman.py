# Game status categories
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.masked_word = '_' * len(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        
        if(self.status != STATUS_ONGOING):
            raise ValueError("Game over")

        if char in self.word and char not in self.masked_word:
            mutable = list(self.masked_word)
            
            for i in range(len(self.word)):
                if self.word[i] == char:
                    mutable[i] = char
            self.masked_word = ''.join(mutable)

        else:
            self.remaining_guesses -= 1
            
        if self.masked_word == self.word:
            self.status = STATUS_WIN

        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE


    def get_masked_word(self):
        return self.masked_word
        

    def get_status(self):
        return self.status
