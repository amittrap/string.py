import random
n = 3
m = 10
def main():
    print( f""" Bagles is  a logical game in this game you have to guess a no of (n)digits and you will
          get(m) chance to do that .you will be provided with a clue after each guessing which might be useful
          for you which can be used as a clue for your next Guess.the clue will be in the form
          Pico   ; correct digits but wrong place 
          Fermi  ;a coorect digits at correct place 
          Bagles ;no Correct digits is guessed.""")
    while True :
        secret_number = generate_number()
        print("i have thought of a number.")
        print(f"you have {m} attempt to guess the number.")
        
        attempt = 1
        while attempt <=m:
            guess = " "
            while len(guess) != n or not guess.isdigit():
                print(f"Attempt #{attempt}: ", end="")
                guess = input().strip()
                
            clues = get_clues(guess, secret_number)
            print(clues)
            attempt +=1
            
            if guess ==secret_number:
                break
            
            if attempt > m:
                print(f"Out of attempt! The numer was {secret_number}.")
                
        print("Do you want to play again? (yes/no)")
        if not input().strip().lower().startswith("y"):
             break
    print("thanks for playing!")
def generate_number():
      digits = list("0123456789")
      random.shuffle(digits)
      return "".join(digits[:n])
  
def get_clues(guess,secret):
      """Returns clues based on the player's guess."""
      if guess ==secret:
          return "you got it!"
      
      clues = []
      for i in range(len(guess)):
          if guess[i] ==secret[i]:
              clues.append("Fermi")
          elif guess[i] in secret:
              clues.append("Pico")
          
      return " ".join(clues) if clues else "Bagles"
  
  
if __name__ == "__main__":
     main()             
                    