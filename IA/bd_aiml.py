import aiml
import os

bot_kernel = None


def initialize_aiml_module():
    global bot_kernel
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


def respond_from_aiml(input_statement):
    global bot_kernel
    return bot_kernel.respond(input_statement)
