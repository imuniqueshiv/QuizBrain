class QuizBrain:
    # Constructor method to initialize instance variables
    def __init__(self, question_list):
        self.score = 0  # Initialize the score to 0
        self.question_number = 0  # Initialize the question number to 0
        self.question_list = question_list  # Store the list of questions

    # Method to check if there are still questions left
    def still_has_question(self):
        return self.question_number < len(self.question_list)  # Return True if there are more questions

    # Method to display the next question
    def next_question(self):
        current_question = self.question_list[self.question_number]  # Get the current question
        self.question_number += 1  # Increment the question number
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")  # Prompt user for an answer
        self.check_answer(user_answer, current_question.answer)  # Check the user's answer

    # Method to check the user's answer and provide feedback
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # Compare the user's answer with the correct answer
            self.score += 1  # Increment the score if the answer is correct
            print("You are right!")  # Inform the user that their answer is correct
        else:
            print("That's wrong!")  # Inform the user that their answer is incorrect
        print(f"The correct answer was: {correct_answer}.")  # Display the correct answer
        print(f"Your score is: {self.score}/{self.question_number}")  # Display the current score and question number
        print("\n")  # Print a newline for spacing
