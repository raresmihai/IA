# -*- coding: utf-8 -*-
from chatterbot import ChatBot

bot = ChatBot(
    "Math & Time Bot",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)


def get_math_response(statement):
    response = "I'm not good at math. Sorry!"
    return response


if __name__ == "__main__":
    # Print an example of getting one math based response
    response = bot.get_response("What is 4 + 9?")
    print(response)
