import random
def game():
    print("hello dear welcome to my game ______🥰🥰🥰")
    name=input("Hello dear enter your name____🥰")
    print("welcome dear",name)
    num=set()
    i=1
    while i<=5:
        num.add(random.randint(0,9))
        if len(num)!=5:
            num.add(random.randint(0,9))
        if len(num)==5:
            break
        i=i+1
    list1=list(num)
    print(list1)
    
    j=0
    chance=9
    cow=0
    bull=0
    li2=[]
    li3=[]
    while 1<=chance:
        user_choice=int(input("enter the guess number____"))
        user_position=int(input("enter the position______"))
        li3.append(user_position)
        print("aapke pass bs ",chance,"chances hi bche h____😕😕😕😕😕😕")
        if user_choice in list1:
            li2.append(user_choice)  
            if li3[j]==list1.index(user_choice):
                bull+=1
                print(bull,"bull")
            else:
                cow+=1
                print(cow,"cow")
        if len(li2)==len(list1)==len(li3)==5:
            break
        chance-=1
        j+=1
    print(li2)
    print(li3)
    if cow<=1 :
        print("losser")
    else:
        print("* congratulations",name, "you have* ",bull,"bulls")
        print("dear",name,"aap jit gye")
    play=input("agr aap dobara khelna chahte ho to : yes/no me se ek dalo_____")
    if play=="yes":
        game()
    else:
        return "exit , jab aapka mn kre tb khel lena 🥰🥰🥰 "
print(game())