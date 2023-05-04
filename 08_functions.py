#def print_codanics():
    #print("this is saad learning data science")
    #print("this is saad learning data science")
    #print("this is saad learning data science")
    
#print_codanics()

#2nd way of defning functions 
#def saad():
    #text="i am learning data science with ammar"
    #print(text)
    #print(text)
#saad()
#3rd way of defining finctions 
#def saad2(text):
    #print(text)
    #print(text)
    #print(text)
#a=5
#saad2(a)
#defining if else and elif and else statements 

def age_calculator(age):
    if age==18:
        print("you are eligible to watch Netflix")
    elif age>18:
        print("you can watch and subscribe premium services")
    else:
        print("you aren't eligible for using Netflix")

age=input("enter your age ")
age=int(age)
age_calculator(age)

def future_age(age):
    new_age=age+20
    return new_age

newage=future_age(age)
print("your name would be ",newage)

    
