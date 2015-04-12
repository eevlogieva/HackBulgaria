class CommandParser:
    def __init__(self):
        self.commands = {}

    def add_command(self, command, function):
        self.commands[command] = function

    def run_command(self, command):
        return self.commands[command]()
