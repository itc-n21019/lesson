qs = ["What is your name?",
      "What is your fav.color?",
      "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    answer = input(questions[n])
    if answer == "q":
        break
    n = (n + 1) % 3
