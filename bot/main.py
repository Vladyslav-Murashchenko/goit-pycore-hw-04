from parsers import parse_input
from handlers import add_contact, change_contact, show_contact, show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            if command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_contact(args[0], contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command in ["close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")
        except ValueError:
            print("An error occurred, try again.")

if __name__ == "__main__":
    main()
