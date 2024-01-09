print('\\\\\\--PALINDROME AND SYMMETRIC--\\\\\\')
n1=input('ENTER THE STRING : ')
def symandpal():
    if len(n1)%2==0:
        l=int(len(n1)/2)
        #print(l)
        s1,s2=n1[0:l],n1[l:] #print('s1:',s1,'s2:',s2)
        p1,p2=n1[0:l],n1[:l-1:-1] #print('p1:',p1,'p2:',p2)
    else:
        l=int(len(n1)/2)
        s1,s2=n1[0:l],n1[m.ceil(len(n1)/2):] #print('s1:',s1,'s2:',s2)
        p1,p2=n1[0:l],n1[:int(len(n1)/2):-1] #print('p1:',p1,'p2:',p2)
    if s1==s2 and p1==p2:
        pp='symmetric and palindrome'
        p=pp.upper()
    elif s1==s2 and p1!=p2:
        p='symetric and not palindrome'
    elif s1!=s2 and p1!=p2:
        p='not symmetric and not palindrome'
    elif s1!=s2 and p1==p2:
        p='palindrome and not symmetric'
    return p
print(symandpal())
'''
# Python program to demonstrate
# symmetry and palindrome of the
# string
# Function to check whether the
# string is palindrome or not
def palindrome(a):
    # finding the mid, start
    # and last index of the string
    mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign in line 21 
    start = 0                #so that you can compare the middle elements also.
    last = len(a)-1
    flag = 0
    # A loop till the mid of the
    # string
    while(start <= mid):
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             
    # Checking the flag variable to
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
         
# Function to check whether the
# string is symmetrical or not       
def symmetry(a):
     
    n = len(a)
    flag = 0
     
    # Check if the string's length
    # is odd or even
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start1 = 0
    start2 = mid
     
    while(start1 < mid and start2 < n):
         
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
      
    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
         
# Driver code
string = 'nooon'
palindrome(string)
symmetry(string)
'''
    
