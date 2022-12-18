class Base:

    def __init__(self, id, user):
        self.id = id
        self.user = user

    
    def print_commands(self):
        for key, command in self.commannds.items():
            print(f"{command} - {key}")