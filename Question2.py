# Define the Question class
class Question:
    def __init__(self, question, option1, option2, option3, option4, correct_answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        print("1. " + self.option1)
        print("2. " + self.option2)
        print("3. " + self.option3)
        print("4. " + self.option4)
    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
# Create a list of 10 Question objects
questions = [
    Question("What is the capital of France?", "London", "Berlin", "Paris", "Madrid", 3),
    Question("Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", 1),
    Question("What is the largest mammal?", "Elephant", "Blue whale", "Giraffe", "Hippopotamus", 2),
    Question("Who painted the Mona Lisa?", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo", 2),
    Question("What's the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4),
    Question("Which country is known as the Land of the Rising Sun?", "China", "Korea", "Japan", "Vietnam", 3),
    Question("Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen", 2),
    Question("What is the primary ingredient of guacamole?", "Tomato", "Avocado", "Onion", "Chili", 2),
    Question("Which mountain range is the longest in the world?", "Andes", "Himalayas", "Rockies", "Alps", 1),
    Question("Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2)
]
def main():
    player1_score = 0
    player2_score = 0
    # Player 1's turn
    for i in range(10):
        print("\nPlayer 1:")
        questions[i].display_question()
        user_input = int(input("Enter your answer (1-4): "))
        if questions[i].check_answer(user_input):
            player1_score += 1
    # Player 2's turn
    for i in range(10):
        print("\nPlayer 2:")
        questions[i].display_question()
        user_input = int(input("Enter your answer (1-4): "))

        if questions[i].check_answer(user_input):
            player2_score += 1
    # Display results
    print("\nGame Over!")
    print(f"Player 1's score: {player1_score}")
    print(f"Player 2's score: {player2_score}")
    # Display which player wins
    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
# call the main function
if __name__ == "__main__":
    main()
