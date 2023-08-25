# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name= name1.lower()+name2.lower()
# new_name_1=str(name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e"))
# new_name_2=str(name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e"))
t= new_name.count("t")
r=new_name.count("r")
u=new_name.count("u")
e=new_name.count("e") 
 
l=new_name.count("l")
o=new_name.count("o")
v=new_name.count("v")
e=new_name.count("e")
true=t+r+u+e
love=l+o+v+e
love_skor=str(true)+str(love)
love_skor=int(love_skor)

if love_skor<10 or love_skor>90:
    print(f"Your score is {love_skor}, you go together like coke and mentos.")
elif love_skor>40 and love_skor<50:
    print(f"Your score is {love_skor}, you are alright together.")

else: 
    print(f"Your score is {love_skor}.")