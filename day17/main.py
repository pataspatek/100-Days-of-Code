from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():    
    question_bank = create_question_bank()

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


def create_question_bank():
    '''Retrieve the question_data and make a list of question object'''
    question_bank = []

    for data in question_data:
        question = Question(data["text"], data["answer"])
        question_bank.append(question)

    return question_bank


if __name__ == "__main__":
    main()