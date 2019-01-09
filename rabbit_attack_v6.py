# Rabbit Attack!

def start():
    print("Welcome to RABBIT ATTACK!")
    print("""               ((`\

            ___ \\ '--._
         .'`   `'    o  )
        /    \   '. __.'
       _|    /_  \ \_\_
      {_\______\-'\__\_\ """)

def end():
    print("Goodbye. Thanks for playing!")
    print("""                 /gg\           /gg\ 
                /g.gg\         /gg.g\ 
               |gg..gg\       /gg..gg| 
               |gg...g|       |g...gg| 
               |gg...g|       |g...gg| 
                \gg..g/       \g..gg/ 
                 |gg.gvgggggggvg.gg| 
                /ggggggggggggggggggg\ 
               /gggg(((ggggggg)))gggg\ 
              |ggggg....ggggg....ggggg| 
              |ggggg....ggggg....ggggg| 
              |ggcccgggg\___/ggggcccgg| 
              |ggcccccgggg|ggggcccccgg| 
               \gggcccggg\---/gggcccgg/ 
                \ggccgggggggggggggccg/ """)
    
def confirm(question):
    while True:
        answer = input(question + " (y/n)")

        if answer.upper() in ["Y" , "YES"]:
            return True
        elif answer.upper() in ["N", "NO"]:
            return False

def play():
    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")
            
        if use_grenade:
            print("1... 2... 5... No, 3!")
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")


start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
