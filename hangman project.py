import sys #this importing is for exiting the terminal without poping terminate msg
print("- - - - - - LetterPuzzleChallenge - - - - - - ")
word="python"
hided_word=word[0]+"."*(len(word)-2)+word[-1]
print('Here is the word to guess : ',hided_word)

#To store this variable into list 
word2list=word[0]+"."*(len(word)-2)+word[-1]
l=[]
for i in word2list:
    l.append(i)

#this are the chances given to win the game !!
chances=len(word)-1

#This is the list to check the letter in word to guess !!
list0=[]
for i in word:
    list0.append(i)
wordd=list0[1:len(list0)-1]

#r=rigth
#w=wrong
r,w=0,0

#to check the guessing letter and take points
for i in range(chances):
    print(chances)
    chances=chances-1
    guessing_word=input("guess the letter contains : ")
    if guessing_word in wordd:
        s=""
        xx=word.index(guessing_word)
        l[xx]=""+ guessing_word
        for i in l:
            s+=i
        print(s)
        r+=1
        if r>=4 and w==0:
            print('---',s.upper(),'---')
            print("WON WITH REWARD !!")
            sys.exit()
    else:
        #print("not")
        w+=1
    if w>=2:
        print('LOST !!!')
        sys.exit()

#to check right and wrong conditions 
if r==4 and w==1:
    print('---',s.upper(),'---')
    print("RIGHT ONLY")



