# year=int(input("Enter your year :"))
# if(year%100==0) and (year%400==0):
#     print("Its a leap year")
# elif (year%100!=0 and year %4==0):
#     print("Its a leap year")
# else:
#     print("Not a leap year")

 
 ### For LOOPS works on range
#range(1,20,1)   #sequence[start:stop:step]

# for i in range(1,20,1):
#     print (i)

# for i in range(16,0,-1):
#     print (i)

# a="Asad Amanullah"
# for i in range (len(a)):
#     print(a[i])

# for i in range (1,21):
#     if(i==15):
#         break
#     print(i)

### print table
# n=int(input("Enter no for which u wan a table :"))
# for i in range(1,11,1):
#     print(f"{n} * {i}={n*i}")


#####
# n=int(input("please tell your number: "))
# fact =1
# for i in range (1,n+1):
#     fact=fact *i

# print(f"your factorial is : {fact}")

# a="ASAD"
# print(a[::-1])

# a="CATAC"
# b=""
# for i in range (len(a)-1,-1,-1):
#     b=b+a[i]
# print(b) 
# if b==a:
#     print("your string is palindrome")
# else:
#     print("Its not a palindrome")

# a="sdfsogn12413@#$%"
 
# char=0
# dig=0
# spchar =0

# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchar+=1

# print(f"your digits are {dig}\n your alphabets are {char}\n your special characters are {spchar} ")

####digit
# a=256
# while a>0:
#     print(a%10)
#     a=a//10

#####rev a number
# rev=0
# a =594
# while a>0:
#     rev=rev*10+a %10
#     a=a//10
# print(rev)

#####
import random
num=random.randint(1,10)
print(num)