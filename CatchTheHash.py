import keyboard
import random
import time
import simpleaudio as sa

def pwnl(string = ""):
    print(string,end="")
    
def newline(x = 1):
    for num1 in range(x):
        pwnl("\n")

def space(y = 1):
    for num2 in range(y):
        pwnl(" ")

x,y = 40,11

sound = ['gameplay.wav','win.wav','lose.wav','menu.wav','select.wav','enter.wav','lifelost.wav']
wave,play = list([0]*7),list([0]*7)

for l in range(7):
    wave[l] = sa.WaveObject.from_wave_file(sound[l])

try:
    while True:     # entire game begins
        
        ppos = [1,1]
        epos = [random.randint(2,x),random.randint(2,y)]
        
        counter = 0
        cursor = list([1]*3)
        flag = list([False]*8)
        
        mode = ['Easy','Medium','Hard','Insane']
        factor = list([0]*3)
        life = 3
        
        play[3] = wave[3].play()
        
        while True:     # menu and character selection
        
            while True:     # menu displayed
                
                time.sleep(0.15)
                
                newline(7)
                space(33)
                pwnl("CATCH THE HASH")
                newline(6)
                space(18)
                pwnl("Which difficulty would you like to play on?")
                newline(4)
            
                for m in range(4):
                    space(36)
                    if cursor[0] == m+1:
                        pwnl(">")
                    else:
                        pwnl(" ")
                    print(mode[m])
                
                newline(3)
                
                while True:
                    if keyboard.is_pressed('up') and cursor[0] > 1:
                        cursor[0] -= 1
                        play[4] = wave[4].play()
                        time.sleep(0.05)
                        break
                    elif keyboard.is_pressed('down') and cursor[0] < 4:
                        cursor[0] += 1
                        play[4] = wave[4].play()
                        time.sleep(0.05)
                        break
                    elif keyboard.is_pressed('enter'):
                        play[5] = wave[5].play()
                        play[5].wait_done()
                        time.sleep(0.05)
                        flag[1] = True
                        break
                
                if flag[1] == True:
                    flag[1] = False
                    break
                
            if cursor[0] == 1:
                factor = [10,100,14]
            elif cursor[0] == 2:
                factor = [8,80,19]
            elif cursor[0] == 3:
                factor = [6,60,24]
            elif cursor[0] == 4:
                factor = [4,40,29]
            
            while True:     # character selection screen
                
                time.sleep(0.1)
                
                newline(10)
                space(30)
                pwnl("Select a character: ")
                newline(3)
                
                space(37)
                if cursor[2] == 1:
                    pwnl(">")
                else:
                    pwnl(" ")
                print(" O")
                space(37)
                if cursor[2] == 2:
                    pwnl(">")
                else:
                    pwnl(" ")
                print(" ~")
                space(37)
                if cursor[2] == 3:
                    pwnl(">")
                else:
                    pwnl(" ")
                print(" +")
                newline(9)
                
                while True:
                    if keyboard.is_pressed('up') and cursor[2] > 1:
                        cursor[2] -= 1
                        play[4] = wave[4].play()
                        time.sleep(0.1)
                        break
                    elif keyboard.is_pressed('down') and cursor[2] < 3:
                        cursor[2] += 1
                        play[4] = wave[4].play()
                        time.sleep(0.1)
                        break
                    elif keyboard.is_pressed('enter'):
                        play[5] = wave[5].play()
                        play[5].wait_done()
                        time.sleep(0.1)
                        flag[4] = True
                        flag[5] = False
                        break
                    elif keyboard.is_pressed('backspace'):
                        play[5] = wave[5].play()
                        play[5].wait_done()
                        time.sleep(0.1)
                        flag[4] = True
                        flag[5] = True
                        break
                
                if flag[4] == True:
                    flag[4] = False
                    break
            
            if cursor[2] == 1:
                player,follower = "O","o"
            elif cursor[2] == 2:
                player,follower = "~","-"
            elif cursor[2] == 3:
                player,follower = "+","."
            
            if flag[5] == False:
                break
        
        if play[3].is_playing():
            play[3].stop()
        
        fpos = list([[0,0]]*factor[2])
        
        lastmove = ''
        
        play[0] = wave[0].play()
        
        while True:     # gameplay begins
            
            time.sleep(0.1)
            
            newline(3)
            
            for i in range(1,y+1):
                for j in range(1,x+1):
                    
                    r1 = random.randint(1,5)
                    
                    if i == ppos[1] and j == ppos[0]:
                        pwnl(player+" ")
                        continue
                    for k in range(factor[2]):
                        if i == fpos[k][1] and j == fpos[k][0]:
                              pwnl(follower+" ")
                              flag[6] = True
                              break
                    if flag[6] == True:
                        flag[6] = False
                        continue
                    if i == epos[1] and j == epos[0]:
                        if r1 != 1:
                            pwnl('# ')
                            continue
                        elif r1 == 1:
                            pwnl('- ')
                            continue
                    pwnl("  ")
                newline()
            
            space(2)
            print("Steps:",counter,"/",factor[1],end="")
            space(7)
            print("Mode:",mode[cursor[0]-1],end="")
            space(7)
            pwnl("Life: ")
            
            if life == 3:
                print((chr(9829)+" ")*3)
            elif life == 2:
                print("- " + (chr(9829)+" ")*2)
            elif life == 1:
                print("- "*2 + (chr(9829)+" "))
            elif life == 0:
                print("- "*3)
                win = False
                flag[7] = True
                break
            
            if ppos in fpos:
                life -= 1
                play[6] = wave[6].play()
                play[6].wait_done()
            
            for n1 in range(0,factor[2]-1):
                fpos[n1] = fpos[n1+1]
            fpos[factor[2]-1] = ppos
            
            while True:
                
                if keyboard.is_pressed('w'):
                    if lastmove == 'down':
                        continue
                    ppos = [ppos[0],ppos[1]-1]
                    lastmove = 'up'
                    if ppos[1] < 1:
                        ppos[1] += y
                    time.sleep(0.05)
                    break
                elif keyboard.is_pressed('a'):
                    if lastmove == 'right':
                        continue
                    ppos = [ppos[0]-1,ppos[1]]
                    lastmove = 'left'
                    if ppos[0] < 1:
                        ppos[0] += x
                    time.sleep(0.05)
                    break
                elif keyboard.is_pressed('s'):
                    if lastmove == 'up':
                        continue
                    ppos = [ppos[0],ppos[1]+1]
                    lastmove = 'down'
                    if ppos[1] > y:
                        ppos[1] -= y
                    time.sleep(0.05)
                    break
                elif keyboard.is_pressed('d'):
                    if lastmove == 'left':
                        continue
                    ppos = [ppos[0]+1,ppos[1]]
                    lastmove = 'right'
                    if ppos[0] > x:
                        ppos[0] -= x
                    time.sleep(0.05)
                    break
                elif keyboard.is_pressed('q'):
                    flag[0] = True
                    win = False
                    flag[3] = True
                    break
            
            if flag[0] == True:
                break
            
            rand = random.randint(1,factor[0])
            
            if epos[0] <= x and epos[0] >= 1 and rand == 1:
                epos[0] += random.randint(int((1-epos[0])//2),int((x-epos[0])//2))
            if epos[1] <= y and epos[1] >= 1 and rand == 1:
                epos[1] += random.randint(1-epos[1],y-epos[1])
                
            counter += 1
            
            if ppos == epos:
                newline(7)
                space(36)
                pwnl("YOU WIN!")
                newline(5)
                space(32)
                print("Steps:",counter,"/",factor[1],end="")
                newline(3)
                win = True
                break
            elif counter == factor[1]:
                newline(7)
                space(36)
                pwnl("YOU LOSE!")
                newline(5)
                space(30)
                if flag[7] == True:
                    pwnl("You ran out of lives!")
                elif flag[7] == False:
                    pwnl("You ran out of steps!")
                newline(3)
                win = False
                break
            
        if play[0].is_playing():
            play[0].stop()
            
        if win == True:
            play[1] = wave[1].play()
        elif win == False:
            play[3] = wave[2].play()
        
        while True:     # end screen is displayed
            
            time.sleep(0.1)
            
            if win == True:
                newline(7)
                space(36)
                pwnl("YOU WIN!")
                newline(5)
                space(32)
                print("Steps:",counter,"/",factor[1],end="")
                newline(3)
            elif win == False:
                
                if flag[3] == True:
                    newline(10)
                    space(36)
                    pwnl("YOU QUIT!")
                    newline(5)
                elif flag[3] == False:
                    newline(7)
                    space(36)
                    pwnl("YOU LOSE!")
                    newline(5)
                    space(30)
                    if flag[7] == True:
                        pwnl("You ran out of lives!")
                    elif flag[7] == False:
                        pwnl("You ran out of steps!")
                    newline(3)
                    
            space(26)
            pwnl("Would you like to play again?")
            newline(3)
            space(37)
            
            if cursor[1] == 1:
                pwnl(">")
            else:
                pwnl(" ")
            print("Yes")
            space(37)
            if cursor[1] == 2:
                pwnl(">")
            else:
                pwnl(" ")
            print("No")
            newline(5)
            
            while True:
                if keyboard.is_pressed('up') and cursor[1] > 1:
                    cursor[1] -= 1
                    play[4] = wave[4].play()
                    time.sleep(0.1)
                    break
                elif keyboard.is_pressed('down') and cursor[1] < 2:
                    cursor[1] += 1
                    play[4] = wave[4].play()
                    time.sleep(0.1)
                    break
                elif keyboard.is_pressed('enter'):
                    play[5] = wave[5].play()
                    play[5].wait_done()
                    time.sleep(0.1)
                    flag[2] = True
                    break
                
            if flag[2] == True:
                break
            
        if cursor[1] == 1:
            continue
        elif cursor[1] == 2:
            break
        
except:
    
    newline(3)
    print("Some error seems to have occured...")
    keyboard.wait('enter')
