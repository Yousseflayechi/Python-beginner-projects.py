
"Question with score " 

print("================================")
print("hello there welcome to my game")
print("================================")
score = 0
press = int(input("press 1 to continue "))
print("================================")
while press == 1 :
    se = input("Question number 1 :    \n A:  / B :  / C :  ")
    while se not in ["a","b","c" ,"A","B","C"] :
        se = input("A:  / B :  / C :  ")
    if se == 'a' or se == "A" :
        score +=1
    else:
        score +=0

    se2 = input("Question number 2 :  \n A:  / B :  / C :  ")
    while se2 not in ["a", "b", "c", "A", "B", "C"]:
        se2 = input("A:  / B :  / C : ")
    if se2 == 'c' or se2 == "C":
        score += 1
    else:
        score +=0

    se3 = input("Question number 3 : \n A: / B :  / C :  ")
    while se3 not in ["a", "b", "c", "A", "B", "C"]:
        se3 = input("A: / B : / C : ")
    if se3 == 'a' or se3 == "A":
        score += 1
    else:
        score += 0

    se4 = input("Question number 4 : \n A: / B : / C :  ")
    while se4 not in ["a", "b", "c", "A", "B", "C"]:
        se4 = input("A: / B : / C :  ")
    if se4 == 'a' or se4 == "A":
        score += 1
    else:
        score += 0

    se5 = input("Question number 5 : ? \n A: / B : / C :  ")
    while se5 not in ["a", "b", "c", "A", "B", "C"]:
        se5 = input("A: / B : / C :  ")
    if se5 == 'c' or se5 == "C":
        score += 1
    else:
        score += 0

    se6 = input("Question number 6 : ? \n A: / B : / C :  ")
    while se6 not in ["a", "b", "c", "A", "B", "C"]:
        se6 = input("A: / B : / C :  ")
    if se6 == 'a' or se6 == "A":
        score += 1
    else:
        score += 0

    se7 = input("Question number 7 : \n A: / B : / C :  ")
    while se7 not in ["a", "b", "c", "A", "B", "C"]:
        se7 = input("A: / B : / C :  ")
    if se7 == 'b' or se7 == "B":
        score += 1
    else:
        score += 0

    se8 = input("Question number 8 : ? \n A: / B : / C : ")
    while se8 not in ["a", "b", "c", "A", "B", "C"]:
        se8 = input("A: / B : / C :  ")
    if se8 == 'a' or se8 == "A":
        score += 1
    else:
        score += 0
    se9 = input("Question number 9 : ? \n A: / B : / C : ")
    while se9 not in ["a", "b", "c", "A", "B", "C"]:
        se9 = input("A:  / B : / C : ")
    if se9 == 'b' or se9 == "B" or se9 == "a" or se9 == "A" or se9 == "C" or se9 == "c" :
        score += 1
    else:
        score += 0
    se10 = input("Question number 10 :  \n A: / B : / C :  ")
    while se10 not in ["a", "b", "c", "A", "B", "C"]:
        se10 = input("A: / B : / C :  ")
    if se10 == 'a' or se10 == "A":
        score += 1
    else:
        score += 0
    break


print("your score is",score,"/10")





"Number Guessing " 


import random

se = random.randint(10,20)

tries = 0

while tries < 5 :
    sz = int(input("insert the number  "))
    if sz < se :
        print("to small ")
    if sz > se:
        print("to big")
    if sz == se :
        print("l3adad kan" , se)
        break
    tries += 1

print("tries : ",tries)
