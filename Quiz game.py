questions = ["How many bones are in the human body?", "Which of the following is NOT a baryon?",
             "Which of the following is NOT a Prime number?", "What is the order of the planets in our solar system from the sun?",
             "Which of the following is NOT a programming language?",
             "Which element has the chemical symbol 'Rf'?",
             "Which of these numbers is a perfect square and a perfect cube?",
             "Which planet has the shortest day, measured by its rotation period?",]

options = [["A: 116", "B: 206", "C: 256", "D: 286"],
           ["A: Proton", "B: Neutron", "C: Electron", "D: Lambda"],
           ["A: 9", "B: 11", "C: 13", "D: 17"],
           ["A: Venus Earth Mercury Mars Jupiter Saturn Uranus Neptune", "B: Mercury Venus Mars Earth Jupiter Saturn Uranus Neptune", "C: Mercury Venus Earth Mars Jupiter Uranus Saturn Neptune", "D: Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune"], 
           ["A: Python", "B: Java", "C: C++", "D: HTML"],
           ["A: Rutherfordium", "B: Rhenium", "C: Roentgenium", "D: Radon"],
           ["A: 343", "B: 125", "C: 216", "D: 64"],
           ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"]]

answers = ["B", "C", "A", "D", "D", "A", "D", "C"]
Score = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[questions.index(question)]:
        print(option)
    user_answer = input("Enter your answer:").strip().upper()
    if user_answer == answers[questions.index(question)]:
        Score += 1
        print(f"Correct answer! Your score is {Score}")
    else:
        print("Incorrect answer.")
print(f"Your final score is: {Score}")