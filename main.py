import pyfiglet
from colorama import init
from google import genai
from termcolor import colored

from tools import open_url, run_command, write_file

init()


class Agent_Gemini:
    def __init__(self) -> None:
        self.client = genai.Client()
        self.chat = self.client.chats.create(
            model="gemini-3-flash-preview",
            config={"tools": [write_file, open_url, run_command]},
        )

    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except EOFError as e:
            return "", str(e)

    def run(self):
        while True:
            print(colored("You: ", "green"), end="")
            user_input, ok = self.get_message()
            if not ok:
                break

            message = self.chat.send_message(user_input)

            print(colored("Agent:", "yellow"), message.text)


def main():
    banner = pyfiglet.figlet_format("AGENT", font="big")
    print(colored(banner, "cyan", attrs=["bold"]))
    agent = Agent_Gemini()
    agent.run()


if __name__ == "__main__":
    main()
