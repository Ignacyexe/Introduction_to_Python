def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-=-=-=-=-=-=-=-=-=-=-=-")
        print(key)
        for i in answers[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("-=-=-=-=-=-=-=-=-=-=-=-")
    print("Results")
    print("-=-=-=-=-=-=-=-=-=-=-=-")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False


# creating dictionary because every question will have answer within its value

questions = {
    "Who created Python?": "A",
    "What year was Python created?": "D",
    "To which comedy group Python have tribute?": "C",
    "What is 9+10?": "B"
}

answers = [["A. Guido van Rossum", "B. Linus Torvalds", "C. Bill Gates", "D. Bjarne Stroustrup"],
           ["A. 1989", "B. 2001", "C. 1996", "D. 1991"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. 19", "B. 21", "C. True", "D. False"]]

new_game()

while play_again():
    new_game()
