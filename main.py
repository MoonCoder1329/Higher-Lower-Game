from art import logo, vs
from game_data import data
import random

print(logo)



def person1(person1):
    global person_count1
    person_count1 = 0
    person_name1 =  person1["name"]
    person_description1 =  person1["description"]
    person_country1 = person1["country"]
    person_count1 =person1["follower_count"]
    return (f"compare A: {person_name1}, {person_description1}, {person_country1} ")

def person2(person2):
    global person_count2
    person_count = 0
    person_name2 =  person2["name"]
    person_description2 =  person2["description"]
    person_country2 = person2["country"]
    person_count2 =person2["follower_count"]
    return (f"compare B: {person_name2}, {person_description2}, {person_country2} ")




score = 0

random_person1 = random.choice(data)
person_choice1 = person1(random_person1)

game = True
while game:
    random_person2 = random.choice(data)
    person_choice2 = person2(random_person2)

    print(person_choice1)
    print(vs)
    print(person_choice2)


    choose = input("Who has more followers? Type 'A' or 'B': ").lower()


    if choose =="a" and person_count1 < person_count2:
        print(f"Sorry, thats wrong. Final Score: {score} ")

        game = False
    elif choose=="a" and person_count1 > person_count2:
        score +=1
        person_choice1  = person_choice2

    elif choose=="b" and person_count1 < person_count2:
        score +=1
        person_choice1 = person_choice2
    elif choose == "b" and person_count1 > person_count2:
        print(f"Sorry, thats wrong. Final Score: {score} ")
        print(score)
        game = False


