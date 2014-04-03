class CommandParser():
    """docstring for CommandParser"""
    def __init__(self):
        self.commands = {}

    def add_command(self, command, function):
        self.commands[command] = function

    def take_command(self, input):
        unformated_input = input.split()
        command = unformated_input[0]
        arguments = unformated_input[1:]
        if command in self.commands:
            self.commands[command](arguments)
