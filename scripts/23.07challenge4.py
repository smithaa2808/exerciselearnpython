questions = {
    "What is the capital of India?": "Delhi",
    "2 + 2 = ?": "4"
}

score = 0
questions_list = list(questions.items())
print(questions_list)
i = 0

while i < len(questions_list):
    q, a = questions_list[i]
  #  print(q, a)
    user = input(q + " ")
    if user == a:
        print("Correct")
        score += 1
    else:
        print("Incorrect")
    i += 1

print("Final Score:", score, "/", len(questions))

    
