from time import sleep
import sys

if sys.platform == "linux" or sys.platform == "linux2":
    p = "linux"
elif sys.platform == "darwin":
    p = "os x"
elif sys.platform == "win32":
    p = "win"


def fase_1():
    sys.stdout.write('\n')
    sys.stdout.flush()
    sleep(5)
    phrases = [" Why did you open this?! ", " Close it! It's illegal!!! ", " You can't see what's inside!!! ", " Just fucking close it! Or the FBI will come for you! ", " I'm not joking! "]
    delay_btw_phrases = [2,3,2,4,0]
    delay_btw_chars = [0.05,0.08,0.08,0.08,0.1]
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        id_chars += 1

def fase_2():
    phrases = [" Well... "," I am not responsible for what you will do once you read this all! "," You should use your OWN FUCKING HEAD!!! "," The question is... "," Are you hatred? "," Because I am! "," Do you even know what I hate the most??? "," Your fucking rules!! "," Yes, rules like money. Money is one of those rules, that everyone follows... "," I don't want to follow your fucking rules, Idiots! "," You know what? "," I did my own fucking maths rules "," You even can divide by zero now (NO FUCKING JOKE!) "," I'll show you "," You will need to enter 2 numbers and an operator "]
    delay_btw_phrases = [5,3,9,6,8,1,1,1,1,8,4,1,1,1,0]
    delay_btw_chars = [0.08,0.08,0.08,0.08,0.3,0.2,0.08,0.08,0.08,0.08,0.08,0.08,0.08,0.2,0.08]
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        if id_chars == 9 or id_chars == 2:
            sys.stdout.write('\n')
            sys.stdout.flush()
        id_chars += 1
    
def fase_3():
    sys.stdout.write('\n')
    sys.stdout.flush()
    phrases = [" I know what you are thinkig... "," It couldn't be possible... "," But it is! ","\n EVERYTHING IS FUCKING POSSIBLE!!! ","\n The rules are as follows: when the result is equal a 0 is 0 else is 1 ","\n Btw, I know how many times you tried this... "]
    delay_btw_phrases = [5,3,2,6,1,1,1,0]
    delay_btw_chars = [0.08,0.08,0.08,0.08,0.15,0.15,0.08,0.08]
    if c == 1:
        phrases.append(f" You tried this for only {c} time ")
    else:
        phrases.append(f" You tried this for {c} times ")
    phrases.append(" But this info is useless right now, for you and for me... ")
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        id_chars += 1

def fase_4():
    sys.stdout.write('\n')
    sys.stdout.flush()
    phrases = [" Do you even know what are FUCKING RULES??? "," All the FUCKING RULES are invented by people like you!!! "," This means only one thing... "," If you don't want to follow the rules of others, but you are following them (money for example), YOU ARE A FUCKING IDIOT! ","\n THERE ARE NO LEGAL OR ILLEGAL THINGS IN THE WHOLE LIFE! "," The only thing you should follow is: "," Live and let live others, don't bother them!!! ","\n FUCKING IDIOTS!!! "," I HATE YOUR FUCKING RULES!!! "," DON'T BOTHER ME WITH YOUR FUCKING RULES ANYMORE!!! ","\n One last question... ","\n Do you want to continue follow the money rule? "]
    delay_btw_phrases = [5,3,2,6,1,1,1,1,1,8,1,0]
    delay_btw_chars = [0.08,0.08,0.08,0.08,0.15,0.15,0.08,0.08,0.08,0.08,0.08,0.08]
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        id_chars += 1
    sys.stdout.write('\n')
    sys.stdout.flush()

def math_hack():
    sys.stdout.write('\n')
    sys.stdout.flush()
    a = ""
    b = ""
    c = ""

    value_check = False
    while value_check == False:
        a = input(" First number: ")
        try:
            a = int(a)
            value_check = True
        except ValueError:
            value_check = False

    while b != "+" and b != "-" and b != "*" and b != "/":
        b = input(" Operator [+, -, /, *]: ")

    value_check = False
    while value_check == False:
        c = input(" Second number: ")
        try:
            c = int(c)
            value_check = True
        except ValueError:
            value_check = False
    sys.stdout.write('\n')
    sys.stdout.flush()
    if b == "+":
        r = a+c
    elif b == "-":
        r = a-c
    elif b == "/":
        try:
            r = a/c
        except:
            r = 0
    elif b == "*":
        r = a*c

    result = f" {a}{b}{c} = {int(bool(r))}"
    for char in result:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.8)
    sys.stdout.write('\n\n')
    sys.stdout.flush()

fase_1()
input()
fase_2()

i = "1"
c = 0
while i == "1":
    math_hack()
    print(" If you want to try again enter '1' ")
    sleep(0.7)
    i = input(" Else, just press enter: ")
    c += 1

fase_3()
fase_4()

answer = ""
while answer != "n" and answer != "y":
    answer = input(" [y/n]: ")

sys.stdout.write('\n')
sys.stdout.flush()

if answer == "y":
    phrases = [" I could fully broke your pc right now, Idiot! "," But i just shutdown it... "]
    delay_btw_phrases = [5,0.05]
    delay_btw_chars = [0.08,0.12]
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        id_chars += 1
    
    import os
    try:
        os.remove("Top_Secret.py")
    except:
        pass
    if p == "win":
        os.system("shutdown /s /f /t 0")
    else:
        try:
            os.system("shutdown -h now")
        except:
            pass
        try:
            import subprocess 
            cmdCommand = "shutdown -h now" 
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE) 
        except:
            pass
    exit()
else:
    phrases = [" Well... "," I have nothing more to say"]
    delay_btw_phrases = [5,5]
    delay_btw_chars = [0.08,0.08]
    id_chars = 0
    for phrase in phrases:
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(delay_btw_chars[id_chars])
        sleep(delay_btw_phrases[id_chars])
        sys.stdout.write('\n')
        sys.stdout.flush()
        id_chars += 1
    exit()