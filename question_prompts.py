from Question import Question

question_prompts = [
    "what color are apples ?\n(a) Red/Green\n(b) purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries ?\n(a) Yellow \n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer==question.answer:
            score +=1;

    print("you got "+str(score) + " out of "+str(len(questions)))


run_test(questions)