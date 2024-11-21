import json
import os

users = {}
quizzes = {
    "quiz1": {
        "questions": [
        {
            "question": "What does DBMS stand for?",
            "choices": ["A. Data Base Management System", "B. Data Backup Management System", "C. Database Master System", "D. Data Backup Master System"],
            "answer": "A"
        },
        {
            "question": "Which of the following is used for database backup?",
            "choices": ["A. SQL", "B. DDL", "C. DML", "D. DBMS Utilities"],
            "answer": "D"
        },
        {
            "question": "What is a foreign key?",
            "choices": ["A. A key from a different table", "B. A primary key from the same table", "C. A unique key", "D. A key without constraints"],
            "answer": "A"
        },
        {
            "question": "Which normalization form eliminates transitive dependency?",
            "choices": ["A. 1NF", "B. 2NF", "C. 3NF", "D. BCNF"],
            "answer": "C"
        },
        {
            "question": "What is the purpose of a primary key?",
            "choices": ["A. To uniquely identify each record", "B. To define relationships", "C. To store metadata", "D. None of the above"],
            "answer": "A"
        }
        ]
    }
}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users:
        print("Username already exists.")
    else:
        users[username] = password
        print("User registered successfully.")
        with open('users.json', 'w') as f:
            json.dump(users, f)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful.")
        with open('logged_in_user.json', 'w') as f:
            json.dump({"username": username}, f)
        return username
    else:
        print("Invalid username or password.")
        return None

def attempt_quiz(username):
    score = 0
    for quiz_name, quiz_data in quizzes.items():
        print(f"Starting {quiz_name}")
        for question in quiz_data["questions"]:
            print(question["question"])
            for choice in question["choices"]:
                print(choice)
            answer = input("Enter your choice: ")
            if answer.lower() == question["answer"].lower():
                score += 1
    print(f"Your score is {score}/{len(quiz_data['questions'])}")
    
    # Save the score
    try:
        with open('scores.json', 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = {}
    
    scores[username] = score
    with open('scores.json', 'w') as f:
        json.dump(scores, f)

def view_score(username):
    try:
        with open('scores.json', 'r') as f:
            scores = json.load(f)
        if username in scores:
            print(f"Your score is {scores[username]}")
        else:
            print("No score available for this user.")
    except FileNotFoundError:
        print("No scores available yet.")

def main():
    logged_in_user = None
    if os.path.exists('logged_in_user.json'):
        with open('logged_in_user.json', 'r') as f:
            data = json.load(f)
            logged_in_user = data.get("username")
            print(f"Welcome back, {logged_in_user}!")

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. View Score")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            logged_in_user = login()
        elif choice == '3':
            if logged_in_user:
                attempt_quiz(logged_in_user)
            else:
                print("You need to login first.")
        elif choice == '4':
            if logged_in_user:
                view_score(logged_in_user)
            else:
                print("You need to login first.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()