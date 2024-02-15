import random
import string

def Password_Generator(adjectives, nouns):
    
    while (True):
    
        # Using Random module's choice function () which chooses a random element from a non-empty sequence.
    
        adjective = random.choice(adjectives)
    
        noun = random.choice(nouns)
    
        number = random.randint(0,100)
    
        special_chr = random.choice(string.punctuation)   # A constant is a special type of variable whose contents can’t be changed. The constant "string.punctuation" holds a string of characters used for punctuation. !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ are the Characters in this constant

        password = adjective + noun + str(number) + special_chr
    
        print ("Your new password is %s", password)

        response = input ("""Would you like another password ? 
Type 'yes' or 'no': -\n""")
        
        if response == "no":
            break
        else :
            continue 
    
    return

def main():
    
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome Password Picker Application ~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    adjectives = ['sleepy', 'slow', 'smelly','wet', 'fat', 'red', 'orange', 'yellow', 'green','blue', 'purple', 'fluffy','white', 'proud', 'brave','happy', 'sad', 'funny', 'loud','quiet', 'shiny', 'furry','silly', 'bumpy', 'sparkling','chubby', 'slick', 'gloomy','jolly', 'vivid', 'zesty']
    
    nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda','banana', 'robot', 'cloud', 'guitar', 'star', 'cupcake','tiger', 'rainbow', 'rocket','cactus', 'umbrella', 'pizza','whale', 'moon', 'firefly']
    
    Password_Generator (adjectives, nouns)   

    print ("The Program is Terminated")
    return 0

if __name__ == "__main__":
    main()
