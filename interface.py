import cls_animal
import zoo
import create_animals_database
import command_parser


def print_greeting():
    hi = """Welcome, you're in the interactive zoo! Type <help> to see help anytime you want."""
    print(hi)


def print_help():
    help = """
Type one of the following:
    -> see_animals- prints all animals in the zoo in the following format: <name> : <species>, <age>, <weight>
    -> accommodate <species> <name> <age> <weight> - adds an animal to the zoo
    -> move_to_habitat <species> <name> - removes an animal from the zoo and returns it to it's natural habitat
    -> simulate <interval_of_time> <period> where: <interval_of_time> is 'days', 'weeks', 'months' or 'years' and <period> is a number
"""
    print(help)


def print_bye():
    print("Goodbye!")


def main():
    commands = []
    print_greeting()
    while True:
        command = input(">>> ")
        if command == "help":
            commands.append(command)
            print_help()
        elif command == "exit":
            commands.append(command)
            print_bye()
            break


if __name__ == '__main__':
    main()
