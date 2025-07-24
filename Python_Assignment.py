import os
import random

def get_user_details():
    print("\nPlease answer the following questions:")

    # List of questions as (key, question_text) pairs
    questions = [
        ("name", "Your name: "),
        ("age", "Your age: "),
        ("favorite_color", "Your favorite color: "),
        ("favorite_food", "Your favorite food: "),
        ("city", "City you live in: "),
        ("shs", "SHS you attended: "),
        ("favorite_team", "Your favorite soccer team: ")
    ]

    # Randomize the question order
    random.shuffle(questions)

    details = {}
    for key, question in questions:
        details[key] = input(question)
    return details

def display_summary(details):
    summary = (
        f"\nHello, {details['name']}!\n"
        f"You are {details['age']} years old, love the color {details['favorite_color']}, "
        f"and enjoy eating {details['favorite_food']}.\n"
        f"Life must be awesome in {details['city']}!\n"
        f"Great to know you attended {details['shs']} and support {details['favorite_team']}!"
    )
    print(summary)
    return summary

def save_to_file(details, summary, rating):
    filename = f"{details['name']}.txt"
    with open(filename, "w") as file:
        file.write(summary + "\n")
        file.write(f"User Rating: {rating} stars\n")
    print(f"\n✅ Summary saved to {filename}")

def main():
    while True:
        details = get_user_details()
        summary = display_summary(details)

        # Ask to save
        save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            # Ask for rating
            while True:
                try:
                    rating = int(input("Rate the assistant (1 to 5 stars): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")
            save_to_file(details, summary, rating)
        else:
            print("Okay, not saving to file.")

        # Ask to restart
        restart_choice = input("\nDo you want to restart and enter details again? (yes/no): ").strip().lower()
        if restart_choice != "yes":
            print("\n👋 Thank you for using the assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()
