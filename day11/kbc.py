# print("Q.1 Who won the world cup T20 2024")
# print(" 1. SA 2. India 3. Australlia 4. USA")
questions = ["Who won the world cup T20 2024", "Who is the PM of India", "When was chandrayaan-2 launched"]
answers = [2, 3, 2]
mcq = [["1. SA", "2. India", "3. Australlia", "4. USA"], ["1. Rahul Gandhi", "2. Nitish Kumar", "3. Narendra Modi", "4. Asit Modi"], ["1. 16th March 2018", "2. 22nd July 2019", "3. 21st May 2019", "4. 4th July 2020"]]



print("Welcome to Kaun banega Crorepati")
count = 0
i,j,k = 0, 0, 0
while( i < len(questions)):
    print(f"Q.{i+1} {questions[i]}")
    print(mcq[j])
    a = int(input("Enter your answer: "))
    if a == answers[k]:
        count += 100
        print(f"You have won {count} rupees")
        print("Great lets move to the next question")
    else:
        print("Sorry but let's try again:)")
        print(f"You have won {count} rupees")  

    i, j, k = i + 1, j + 1, k + 1
print(f"Great you have won {count} rupees")

