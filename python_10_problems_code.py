def radtodeg():
    n=int(input('number of values to convert :'))
    for i in range(n):
        no=int(input('value :'))
        res=no*57.2958
        print('degtorad',res)
    return ''
def degtorad():
    n=int(input())
    for i in range(n):
        no=int(input())
        res=no*0.0174533
        print('radtodeg',res)
    return ''
def vowels():
    s=input('enter the string :')
    s.lower()
    c=0
    for i in s:
        if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
            c+=1
    return f'number of vowels in string is : {c}'
def consonants():
    s=input('enter the string :')
    s.lower()
    c=0
    for i in s:
        if i!='a' and i!='e' and i!='o' and i!='i' and i!='u':
            c+=1
    return f'number of consonants in string is : {c}'
def hidingno():
    n=input()
    l=len(n)
    nn=''
    for i in range(l):
        if l-i>4:
            nn+='*'
        else:
            nn=nn+str(n[i])
    return f'the hided encryped msg : {nn}'
def calculator():
    x,y=map(int,input().split())
    print('''enter 1 for +
enter 2 for -
enter 3 for *
enter 4 for /
''')
    opp=int(input('enter operation to perform : '))
    if opp==1:
        res=x+y
        return res
    elif opp==2:
        res=x-y
        return res
    elif opp==3:
        res=x*y
        return res
    elif opp==4:
        res=x/y
        return res
def discount():
    total=0
    print('''
 ______________________________
|    amount      | discount    |
|------------------------------|
| 1     -  5000   |    5%      |
| 5001  -  15000  |    12%     |
| 15001 -  25000  |    20%     |
| above 25000     |    30%     |
|______________________________|
''')
    nfpro=int(input('enter the number of products to purchase : '))
    if nfpro<2:
        pc=int(input('enter the cost of product :'))
        if pc>=1 and pc<=5000:
            dis=pc*0.05
            total=round(pc-dis)
            #print(dis,total)
        elif pc>=5001 and pc<=15000:
            dix=pc*0.12
            total=round(pc-dis)
            #print(dis,total)
        elif pc>=15001 and pc<=25000:
            dix=pc*0.20
            total=round(pc-dis)
            #print(dis,total)
        else:
            dis=pc*0.30
            total=round(pc-dis)
            #print(dis,total)
        return f'the cost of product after discount is : {"%.2f"%total} /-'
    else:
        for i in range(nfpro):
            pc=int(input('enter the cost of product :'))
            if pc>=1 and pc<=5000:
                dis=pc*0.05
                total+=round(pc-dis)
            elif pc>=5001 and pc<=15000:
                dis=pc*0.12
                total+=round(pc-dis)
            elif pc>=15001 and pc<=25000:
                dis=pc*0.20
                total+=round(pc-dis)
            else:
                dis=pc*0.30
                total+=round(pc-dis)
        return f'the cost of product after discount is : {"%.2f"%total} /-'
def fib():
    choice=int(input('''
1.TO GET THE FIBONACCI VALUE AT SPECIFIED POSTION :
2.TO GET THAT MANY FIBONACCI SERIES NUMBERS : '''))
    if choice==1:
        com=''
        while com=='':
            pos=int(input('enter the position : '))
            print('')
            f1,f2=0,1
            if pos==1:
                print(f1)
            elif pos==2:
                print(f2)
            else:
                f1,f2=0,1
                for i in range(pos-2):
                    res=f1+f2
                    f1=f2
                    f2=res
                print(res)
                print('')
            com=input('enter 2 run : ')
    elif choice==2:
        f1,f2=0,1
        leng=int(input(''))
        if leng==1:
            print(f1)
        elif leng==2:
            print(f2)
        else:
            print(f1 , f2 ,end=' ')
            for i in range(leng-2):
                res=f1+f2
                f1,f2=f2,res
                print(res,end=' ')
    return ''
def prime():
    choice=int(input('''
1.GET PRIME NUMBEBS UPTO THAT  :
2.GET HOW MANY NUMBER OF PRIME NUMBER TO GET : '''))
    if choice==1:
        leng=int(input('ENTER THE LENG OF PRIME NUMBER SERIES :'))
        
        for i in range(1,leng+1):
            c=0
            for j in range(1,i+1):
                if i%j==0:
                    c+=1
            if c==2:
                print('prime :',i)
        return ''
    elif choice==2:
        c=0
        num=int(input('enter the number to check that number is prime or no : '))
        if num<2:
            print('not')
        else:
            for i in range(1,num+1):
                if num%i==0:
                    c+=1
            if c==2:
                print('prime : ',num)
        return ''
def ciserchipher():
        x=int(input('''1.ENTER 1 TO CONVERT PLAIN TO CIPHER TEXT
2.ENTERT 2 TO CONVERT CIPHER TO PLAIN TEXT'''))
        if x==1:
            n=input('enter msg to encrypt : ')
            newmsg=''
            al= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
            code=int(input('enter code to encrypt : '))
            for i in n:
                if type(i)==str and i!=' ':
                    encode=code+al.index(i)
                    if encode<26:
                        encode=encode
                    else:
                        encode=encode%26
                    newmsg+=al[encode]
                else:
                    newmsg+='_'
            print(newmsg)
        elif x==2:
            n=input('enter msg to decrypt : ')
            newmsg=''
            al= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
            code=-(int(input('enter code to decrypt : ')))
            for i in n:
                if i!=' ':
                    encode=al.index(i)+code
                    encode=encode%26
                    newmsg+=al[encode]
                elif i==' ':
                    newmsg+=' '
            print(newmsg)
        return ''    



opp=1
while opp!=0:
    op=int(input('''
1.TO CONVERT RAD TO DEG :
2.TO CONVERT DEG TO RAD :
3.TO COUNT THE VOWELS IN STRING:
4.TO COUNT THE CONSONANTS IN STRING:
5.TO HIDE THE NUMBER IN CONTENT :
6.TO CALCULATE TO NUMBERS :
7.TO KNOW HOW MUCH DISCOUNT ON A PRODUCT :
8.TO GET THE FIBINOCI SERIES :
9.TO GET ABOUT PRIME NUMBER : '''
             ))
    if op==1:
        print(radtodeg())
    elif op==2:
        print(degtorad())
    elif op==3:
        print(vowels())
    elif op==4:
        print(consonants())
    elif op==5:
        print(hidingno())
    elif op==6:
        print(calculator())
    elif op==7:
        print(discount())
    elif op==8:
        print(fib())
    elif op==9:
        print(prime())
    elif op==10:
        print(ciserchipher())
    opp=int(input('zero to stoppp :'))
print('')
print('----------- HAVE A GOOD DAY -----------')








          

    
