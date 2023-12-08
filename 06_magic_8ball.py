name = input("What is your name? ")
question = input("Ask the Magic 8-Ball a question. ")
answer = ""

import random
random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "it is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook no so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if (name == "") and (question != ""):
    print("You asked the magic 8-Ball: ", question)
    print("The Magic 8-Ball says: ", answer)
elif (name != "") and (question == ""):
    print(name, " You need to ask the Magic 8-Ball a question.")
elif (name == "") and (question == ""):
    print("The Magic 8-Ball cannot answer without a question.")
else:
    print(name, " asked the magic 8-Ball ", question)
    print("The magic 8-Ball's says. ", answer)