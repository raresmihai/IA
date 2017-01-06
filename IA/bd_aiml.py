import aiml
import os


def create_bot_kernel():
    bot_kernel = aiml.Kernel()
    for subdir, dirs, files in os.walk("aimls"):
        for aiml_file in files:
            bot_kernel.learn(os.path.join(subdir, aiml_file))

    properties_file = open(os.path.join(os.getcwd(), "bot.properties"))
    for line in properties_file:
        parts = line.split('=')
        key = parts[0]
        value = parts[1][:-1] #to remove \n from string final
        bot_kernel.setBotPredicate(key, value)

    return bot_kernel


def respond_from_aiml(input_statement, bot_kernel):
    return bot_kernel.respond(input_statement)


if __name__ == "__main__":
    kernel = create_bot_kernel()
    while True:
        print respond_from_aiml(raw_input(">>"), kernel)
