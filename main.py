bot_name = "bot"

def get_user():
    global name
    print(f'{bot_name}: Hello! What is your name?')
    name = input()

def respond():
    return ""

def chatbot_loop():
    while True:
        # user input
        user_input = input(f'{name}: ')

        if user_input == 'quit':
            # save info before quitting
            break
        # bot response
        bot_response = respond()
        print(f'{bot_name}: {bot_response}')
    print(f'{bot_name}: Have a nice day!')

if __name__ == "__main__":
    get_user()
    chatbot_loop()