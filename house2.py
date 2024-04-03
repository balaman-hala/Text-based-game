import curses
from curses import wrapper
from curses.textpad import Textbox
import time
from tools2 import Sword
from tools2 import Knife
from tools2 import Lighter
from tools2 import Mystery
from tools2 import Fangs
from tools2 import Spray
from tools2 import Fist

def clr(window):
    global line_counter
    global keyy
    window.addstr(line_counter+2,0,"PRESS ANY KEY TO CONTINUE!",curses.A_BOLD)
    keyy = window.getkey()
    window.clear()
    time.sleep(1)
    line_counter = 0
    window.refresh()

def display_text(stdscr, text,start_col,color_pair_id):
    global line_counter
    stdscr.refresh()
    time.sleep(0.2)  # Wait for a second before displaying each letter
    for i in range(len(text)):
        stdscr.addch(line_counter, start_col + i, text[i],curses.color_pair(color_pair_id))
        stdscr.refresh()
        time.sleep(0.05)
    line_counter += 1

line_counter=0
class Character:
    def __init__(self,name: str,health: int,tool ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.tool=tool


    def attack(self,stdscr,target, power: int =1):
        global line_counter
        self.power=power
        target.health -= self.tool.damage*self.power
        target.health = max(target.health, 0)
        display_text(stdscr,f"{self.name} dealt a {self.tool.damage*self.power} damage to {target.name} with {self.tool.name}",0,4)
        display_text(stdscr,f"{self.name} health is: {self.health}",0,4)
        display_text(stdscr,f"{target.name} health is: {target.health}",0,4)
        line_counter += 1



        


key='a'
points=100
inventory=[Mystery,Knife,Sword,Lighter]



    

def find (inventory,key):
    for i in range(len(inventory)):
        if(key == inventory[i].name):
            return i
        return -1


def house_entry(stdscr,key):
    display_text(stdscr,"How you want to enter the house?\n",0,1)
    display_text(stdscr,"Please press:\n",0,4)
    display_text(stdscr,"w:for window\n",2,4)
    display_text(stdscr,"d: for door\n",2,4)
    key = stdscr.getkey()
    if key == 'w':
        display_text(stdscr,"you managed to force the window open\n",0,3)
    elif key == 'd':
        display_text(stdscr,"The door is locked. you can't force it open. find another way in\n",0,2)
        house_entry(stdscr,key)
    else:
        display_text(stdscr,"Invalide choice. try again\n",0,2)
        house_entry(stdscr,key)

def fight_show(stdscr, enemy_name : str , enemy_health : int , enemy_weapon  ,hero_health : int , hero_weapon ,hero_power: int):
    global line_counter
    rows ,col =stdscr.getmaxyx()
    hero =Character(name="Charlotte",health=hero_health,tool=hero_weapon)
    enemy=Character(name=enemy_name,health=enemy_health,tool=enemy_weapon)
    
    while(hero.health!=0 and enemy.health!=0 ):
            hero.attack(stdscr,enemy,hero_power)
            if enemy.health!=0:
                enemy.attack(stdscr,hero,1)
            if line_counter > rows-10:
                stdscr.clear()
                time.sleep(1.5)
                line_counter = 0
                stdscr.refresh()
                stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
                line_counter +=3

    if(hero.health==0):
        display_text(stdscr,"you lost game over\n",0,2)
        clr(stdscr)
    else:
        display_text(stdscr,f"The {enemy_name} has been defeated",0,3)
        clr(stdscr)
    
    
    
    

def help (stdscr,key,enemy_name:str,enemy_weapon,hero_health: int, enemy_health: int,hero_weapon,power):
    global line_counter
    display_text(stdscr,"Who do you want to ask\n",0,1)
    display_text(stdscr,"Please press\n",0,4)
    display_text(stdscr,"j: to ask jeremy\n",3,4)
    display_text(stdscr,"m: to ask the master\n",3,4)
    key=stdscr.getkey()
    line_counter +=1
    if key == 'j':
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter +=3
        jeremy=Character("jeremy",100,Spray)
        enemy=Character(enemy_name,enemy_health,enemy_weapon)
        jeremy.attack(stdscr,enemy,1)
        display_text(stdscr,"jerymys attack served as a distraction",0,3)
        clr(stdscr)
        display_text(stdscr,f"It gave you enough time to pick up {jeremy.tool.name} and start attacking again",0,4)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,hero_weapon,power)
        
    elif key== 'm':
        display_text(stdscr,"The master can't help. He took an oath not to interfere with the mission",0,2)
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        enemy=Character(enemy_name,enemy_health,enemy_weapon)
        hero=Character("charlotte",hero_health,Fist)
        enemy.attack(stdscr,hero,1)
        
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,Fist,1)
        
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        help(stdscr,key,enemy_name,enemy_weapon,hero_health,enemy_health,hero_weapon,power)
        
    

def tool_drop(stdscr,key,enemy_name :str,enemy_health: int,enemy_weapon, hero_health: int,hero_weapon,power):
    global line_counter
    display_text(stdscr,"The attack of the spider caused you to drop your weapon\n",0,4)
    display_text(stdscr,"How do you want to procede?\n",0,1)
    display_text(stdscr,"Please press\n",0,4)
    display_text(stdscr,"h: to ask for help\n",3,4)
    display_text(stdscr,"p: to try and pick up the weapon\n",3,4)
    key=stdscr.getkey()
    line_counter += 1
    if key == 'p':
        clr(stdscr)
        display_text(stdscr,"you weren't quick enough. you have to finish the fight with your fists",0,2)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        enemy=Character(enemy_name,enemy_health,enemy_weapon)
        hero=Character("charlotte",hero_health,Fist)
        enemy.attack(stdscr,hero,1)
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,Fist,1)
        clr(stdscr)
        
    elif key == 'h':
        help(stdscr,key,enemy_name,enemy_weapon,hero_health,enemy_health,hero_weapon,power)
       
        
          
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        tool_drop(stdscr,key,enemy_name,enemy_health,enemy_weapon,hero_health,hero_weapon,power)



def attack_area (stdscr,key,hero_weapon,hero_health:int ,enemy_name: str, enemy_weapon):
    global line_counter
    display_text(stdscr,"Where do you want to hit?\n",0,1)
    display_text(stdscr,"Please press\n",0,4)
    display_text(stdscr,"o: for over the head\n",3,4)
    display_text(stdscr,"s: for sliding under\n",3,4)
    key= stdscr.getkey()
    line_counter += 1
    if key == 'o':
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,hero_weapon,1)
        clr(stdscr)
    elif key == 's':
        clr(stdscr)
        hero=Character("Charlotte",100,hero_weapon)
        enemy=Character(enemy_name,100,enemy_weapon)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        hero.attack(stdscr,enemy,2)
        enemy.attack(stdscr,hero,1)
        clr(stdscr)
        tool_drop(stdscr,key,enemy_name,enemy.health,enemy_weapon,hero.health,hero_weapon,2)
        
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        attack_area(stdscr,key,hero_weapon,hero_health,enemy_name,enemy_weapon)
        


def fight(stdscr,key,enemy_name: str,enemy_weapon,hero_health):
    global line_counter
    display_text(stdscr,"It's time for you to attack now.\n",0,4)
    display_text(stdscr,"What tool do you want to use?\n",0,1)
    display_text(stdscr,f"Your options are:{inventory[0].name} ,{inventory[1].name} ,{inventory[2].name}\n",0,4)
    curses.echo()
    key= stdscr.getstr().decode('utf-8')
    curses.noecho()
    line_counter += 1
    if key == Mystery.name:
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,Mystery,1)
        clr(stdscr)
    elif key == Lighter.name:
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,Lighter,1)
        clr(stdscr)
    elif key == Sword.name:
        attack_area(stdscr,key,Sword,hero_health,enemy_name,enemy_weapon)
        clr(stdscr)
    elif key == Knife.name:
        attack_area(stdscr,key,Knife,hero_health,enemy_name,enemy_weapon)
        clr(stdscr)
    else:
        display_text(stdscr,"Invalide choice.try again.",0,3)
        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,hero_health)
        
           
def door2_entery(stdscr,key,enemy_name: str,enemy_weapon):

    global line_counter
    display_text(stdscr,f"You used the key to open the other door. As you enter you find a giant {enemy_name}\n",0,4)
    display_text(stdscr,"It's attacking you act quick!\n",0,4)
    display_text(stdscr,"what do you want to do?\n",0,1)
    display_text(stdscr,"Please press:\n",0,0)
    display_text(stdscr,"b: for block\n",3,4)
    display_text(stdscr,"d: for dodge\n",3,4)
    key=stdscr.getkey()
    line_counter += 1
    if key == 'd':
        display_text(stdscr,"You successfully dodged.\n",0,3)
        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,100)

    elif key =='b':
        display_text(stdscr,"Its attack was too strong. you didn't have enough time to get into the right stance\n",0,2)
        line_counter += 3
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        hero=Character(name="charlotte",health=100,tool=Fist)
        enemy=Character(name= enemy_name,health=100,tool=enemy_weapon)
        enemy.attack(stdscr,hero,1)
        line_counter += 1
        stdscr.addstr(line_counter,4,"******Fight\E******",curses.color_pair(5) | curses.A_BOLD)

        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,hero.health)
        
    else:
        display_text(stdscr,"Invalide choice. try again\n",0,2)
        clr(stdscr)
        door2_entery(stdscr,key,enemy_name,enemy_weapon)


#def door2_attack(stdscr,key,points):
 #   display_text(stdscr,"Its time for you to attack now.\n",line_counter,0,0)
  #  display_text(stdscr,"What tools do you want to use during the fight.\n",line_counter,0,1)
   # key=stdscr.getstr().decode(encoding="utf-8")
    #if key != "gun" and key != "knife":



def main (stdscr):
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    stdscr.clear()
    display_text(stdscr,"As you walk deep in this path. you encounter a house with an unwelcoming exterior\n",0,4)
    house_entry(stdscr,key)
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()
    global line_counter
    line_counter=0
   
    door2_entery(stdscr,key,"Monster",Fangs)
    stdscr.getch()
    time.sleep(1)
    stdscr.clear()
    stdscr.refresh()



wrapper(main)
