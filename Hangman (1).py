import pygame
from pygame import mixer
import random

def gettext(x, y, label, numeric, size, spaces,leng):
    word = []  # hold word or number to return
    length = 0  # gets length of entered word - will not allow more than the size
    prompt = font.render(label, True, black) #render the prompt
    pygame.draw.rect(screen,white,(x-300,y,800,50)) # draw a white recangle over previous x an y cordinates
    screen.blit(prompt, (x, y))  # display the new x and y coordinates

    pygame.display.update()  # update display
    while True:  # main loop to enter data

        for event in pygame.event.get():  # user entered something

            if event.type == pygame.QUIT:  # user decided to end program (click X at top right)
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # user touch a key
                if event.key == pygame.K_SPACE and spaces==True:  # if space then force space and append to the workd
                    word.append(" ") # if they press space add a blank space to the word
                if event.key == pygame.K_RETURN:  # if Return then user is finished entery data

                    newword = ""  # holds word to return from function

                    for char in word:  # loop to remove any spaces
                        if (spaces == False):
                            if char != "space":
                                newword = newword + char #if spaces are not allowed only add the letters to the list that are not space
                    return newword #return the word
                    break
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    del word[-1:] #remove the last letter of the word
                    newword = "" 
                    for char in word:
                        newword = newword + char #redo the word without the last letter
                    length=length-1 #remove one from the length of the word
                    
                    pygame.draw.rect(screen, white, (x+leng, y, 200, 50)) #draw a white rectangle over the removed letter
                    afterdelete = font.render(newword, True, black) #render the new word without the last letter
                    
                    screen.blit(afterdelete, (x+leng, y))  # display the new x and y coordinates
                    pygame.display.update()  # update display
                else:
                    key = pygame.key.name(event.key)
                    if len(key) == 1 and length < size: #if the length maximum has not been exeeded 
                        ascii = ord(key)
                        if (numeric == True):  # only allow number input
                            if ascii > 47 and ascii < 59:  # number input
                                word.append(key)
                                length = length + 1
                        else:
                            word.append(key) #add the letter to the word
                            length = length + 1
                    newword="" 
                    for char in word:
                        newword = newword + char #redo new word by clearing it then adding the letters back
                    output = font.render(newword, True, black) #renders the word
                    prompt = font.render(label, True, black) #renders the prompt

                    pygame.draw.rect(screen, white, (x, y, 200, 50)) #draws over the old content to make room for the new
                    screen.blit(prompt, (x, y))  # display the new x and y coordinates
                    screen.blit(output, (x + leng, y))  # display the new x and y coordinates
                    pygame.display.update()  # update display

pygame.init()

name=pygame.display.set_caption("Hangman") #changes the name of the program to Hangman

hangmen=[] #the list to hold the diferent hangmen

hangmen.append(pygame.image.load("hangman 1.png"))
hangmen.append(pygame.image.load("hangman 2.png"))
hangmen.append(pygame.image.load("hangman 3.png"))
hangmen.append(pygame.image.load("hangman 4.png"))
hangmen.append(pygame.image.load("hangman 5.png"))
hangmen.append(pygame.image.load("hangman 6.png"))
hangmen.append(pygame.image.load("hangman 7.png"))
hangmen.append(pygame.image.load("hangman 8.png"))

#loads in all the images of hangman

screen=pygame.display.set_mode((850,800)) #sets the screen size

black=(0,0,0)
white=(255,255,255)

screen.fill(white)
pygame.display.update()

font=pygame.font.SysFont("comicsansms",24)
players=gettext(100,100,"# of players :",True,1,False,200) #get the number of players one or 2

screen.fill(white)
pygame.display.update()

if players=="1":
    words=[]
    file=open('words.txt','r')
    for word in file:
        words.append(word)
    file.close()
    #get the words from the file
    r=random.randint(0,853)
    word=words[r]
    word=word.lower()
    word=word.strip()
    #choose a word then strip it and put it in lower case

if players=="2":
    label=font.render("Enter the word for your opponent to",True,black)
    screen.blit(label,(100,100))
    pygame.display.update()
    word=gettext(100,150,"guess (max 7)and click enter :",False,8,False,350)
    word=word.lower()
    


screen.fill(white)
pygame.display.update()

answered=False #the player hasent yet entered an answer
hangmantype=1 #the first hangman picture

#location of underline x position
locx=100

for x in range(0,len(word)):
    label=font.render("_",True,black)
    screen.blit(label,(locx,600))
    pygame.display.update()
    locx=locx+100
    #draw the blank spaces in under the letters

locx=100 #the first blank letter
guessed=-125 #how many letters or words have been guessed
letssolved=0 #the number of letters that have been solved
hangmantype=0 #the type of hangman displayed
loose=False #they havent lost the game
while loose==False:
    screen.blit(hangmen[hangmantype],(400,200))
    pygame.display.update()
    guess=gettext(100,150,"guess a letter or the full word :",False,8,False,350)
    letplace=0 #the location of the letter in the word
    isletterthere=False #to make you gain a hangman level if the letter you chose is not there
    if len(guess)==1:
        for let in word:
            if let==guess:
                label=font.render(let,True,black)
                screen.blit(label,(locx+letplace,600))
                letssolved+=1
                isletterthere=True
            letplace+=100
        if isletterthere==False:
            hangmantype+=1
            guessed+=125
            label=font.render(guess,True,black)
            screen.blit(label,(guessed,100))
            pygame.display.update()
            
    else:
        guessed+=125
        if guess==word:
            label=font.render("you got it!",True,black)
            screen.blit(label,(100,50))
        else:
            label=font.render(guess,True,black)
            screen.blit(label,(guessed,100))
            hangmantype+=1
    if letssolved==len(word):
        label=font.render("you got it!",True,black)
        screen.blit(label,(100,50))
        pygame.display.update()
        break
    screen.blit(hangmen[hangmantype],(400,200))
    pygame.display.update()
    if hangmantype>6:
        label=font.render("you lose word was :"+word,True,black)
        screen.blit(label,(100,50))
        pygame.display.update()
        loose=True
        break






                
