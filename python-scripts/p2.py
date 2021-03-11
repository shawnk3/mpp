
from machine import Pin
from utime import sleep

letters = {
      'A': '.-', 
      'B': '-...', 
      'C': '-.-.', 
      'D': '-..', 
      'E': '.', 
      'F': '..-.', 
      'G': '--.', 
      'H': '....', 
      'I': '..', 
      'J': '.---', 
      'K': '-.-', 
      'L': '.-..', 
      'M': '--', 
      'N': '-.', 
      'O': '---', 
      'P': '.--.', 
      'Q': '--.-', 
      'R': '.-.', 
      'S': '...', 
      'T': '-', 
      'U': '..-', 
      'V': '...-', 
      'W': '.--', 
      'X': '-..-', 
      'Y': '-.--', 
      'Z': '--..', 
      '1': '.----', 
      '2': '..---', 
      '3': '...--', 
      '4': '....-', 
      '5': '.....', 
      '6': '-....', 
      '7': '--...', 
      '8': '---..', 
      '9': '----.', 
      '0': '-----', 
      ' ': '/'
          }


led = Pin(25, Pin.OUT)
hint = Pin(8,Pin.OUT, Pin.PULL_DOWN)
one = Pin(6, Pin.IN, Pin.PULL_UP)
two = Pin(7, Pin.IN, Pin.PULL_DOWN)
three = Pin(10, Pin.IN, Pin.PULL_UP)

def level(num):
    for i in range(num):
        led.on()
        sleep(1)
        led.off()
        sleep(1)


def message(str):
    for letter in str:
        time_convert(letters[letter])
        
    
def time_convert(msg):
    
    for char in msg:
#         print(char)
        if char is '.':
            outputMsg(1)
        if char is '-':
            outputMsg(3)
        if char is '/':
            sleep(5)
        else:
            outputMsg(0)
            
   
def outputMsg(time):
    hint.on()
    sleep(time)
    hint.off()
    sleep(1)

solve1,solve2,solve3 = False, False, False

print("CHECK MESSAGES FROM PIN 8")
while not solve1:
    level(1)
    print("LEVEL1")
    message("GROUND PIN 6")
    if one.value == 0:
        solve1 = True

while not solve2:
    level(2)
    print("LEVEL2")
    message("POWER PIN 7")
    if two.value == 1:
        solve2 = True

while not solve3: 
    level(3)
    print("LEVEL3")
    message("GROUND PIN 10")
    if two.value == 0:
        solve3 = True

print("Puzzle Solve!")
print("c3438f7f8f92d75ff197b17a13a3a667fdf0920074aabffc6ce0c2b9fce9a46e")




