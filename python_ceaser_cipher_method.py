'''nn=input(' ENTER S TO RUN  , N TO STOP: ')
while nn=='s':
    ans=input('enter the massage to encrypt: ')
    anss=ans.replace(' ','')
    newmsg=''
    al= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z']
    code=int(input('enter the code to run: '))
    for i in anss:
        s=al.index(i)
        encodeno=s+code
        #print(s,encodeno)
        if encodeno>26:
            encodeno=encodeno%26
        else:
            encodeno=encodeno
        typee=type(encodeno)
        if type(encodeno)==int:
            newmsg+=al[encodeno]
        else:
            newmsg+=ans.replace(' ','_')
    print(newmsg)
    nn=input(' ENTER S TO RUN  , N TO STOP: ')'''
ans=input('enter s to run and n to stop : ')
while ans=='s':
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
        code=int(input('enter code to decrypt : '))
        for i in n:
            if i!=' ':
                encode=al.index(i)+code
                encode=encode%26
                newmsg+=al[encode]
            elif i==' ':
                newmsg+=' '
        print(newmsg)
    else:
        pass
    ans=input('enter s to run and n to stop : ')



