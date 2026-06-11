from sys import argv

script, user_name = argv # assiging ex14.py and smithaa, this two words come from command given in the terminal
prompt = '>' # assiging prompt as > 

print(f"Hi {user_name}, I'm the {script} script.") # printing the f"strings{variable}""
print("I'd like to ask you a few questions.") # printing the strings
print(f"Do you like me {user_name}?") # printing f"strings{variable}
likes = input(prompt) # asking user does they like me

print(f"Where do you live {user_name}?") # printing f"strings{variable}
computer = input(prompt) # asking user where they live 

print(f"""
Alright, so you said {likes} about liking me.
You live in {computer}. Not sure where it is.
And you have a {computer} computer . Nice.
""") # printing f"strings{variable} 