from Bot import Bot
from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self, commands):
        pass

    @abstractmethod
    def get_user_input(self):
        pass

class ConsoleView(View):
    def display_contacts(self, contacts):
        message = "Contacts:\n"
        for contact in contacts:
            message += f"Name: {contact['name']}\n"
            if contact['phones']:
                message += f"Phones: {', '.join(contact['phones'])}\n"
            if contact['birthday']:
                message += f"Birthday: {contact['birthday'].strftime('%d/%m/%Y')}\n"
            if contact['email']:
                message += f"Email: {contact['email']}\n"
            if contact['status']:
                message += f"Status: {contact['status']}\n"
            if contact['note']:
                message += f"Note: {contact['note']}\n"
            message += "_" * 50 + "\n"
        self.display_message(message)

    def display_commands(self, commands):
        message = "Available Commands:\n"
        for command in commands:
            message += command + "\n"
        self.display_message(message)

    def get_user_input(self):
        return input("Enter a command: ").strip().lower()

    def display_message(self, message):
        print(message)
        


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                print(format_str.format(command))
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        if action == 'exit':
            break
