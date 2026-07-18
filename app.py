"""
ResearchMind-AI v2
Professional CLI

"""

import os

from agent.research_agent import ResearchAgent
from config.validator import StartupValidator
from config.version import APP_NAME, AUTHOR, DESCRIPTION, VERSION
from services.history_manager import HistoryManager

history = HistoryManager()


def banner():

    print("=" * 70)
    print(f"{APP_NAME} {VERSION}")
    print(DESCRIPTION)
    print(f"Author : {AUTHOR}")
    print("=" * 70)

    print("\nType 'help' to view available commands.")
    print("Type 'history' to view conversation history.")
    print("Type 'clear history' to delete history.")
    print("Type 'version' to view version.")
    print("Type 'exit' to quit.\n")


def main():
    validator = StartupValidator()

    validator.validate()
    banner()

    agent = ResearchAgent()

    while True:

        try:

            question = input("research> ").strip()

            if not question:
                continue

            lower = question.lower()

            # -----------------------------------------
            # Exit
            # -----------------------------------------

            if lower in ["exit", "quit"]:

                print("\nGoodbye!\n")

                break

            # -----------------------------------------
            # Version
            # -----------------------------------------

            elif lower == "version":

                print()
                print(APP_NAME)
                print(f"Version : {VERSION}")
                print(f"Author  : {AUTHOR}")
                print()

                continue

            # -----------------------------------------
            # Clear Screen
            # -----------------------------------------

            elif lower in ["cls", "clear"]:

                os.system("cls")

                banner()

                continue

            # -----------------------------------------
            # Show History
            # -----------------------------------------

            elif lower == "history":

                data = history.load()

                if not data:

                    print("\nNo history found.\n")

                else:

                    print()

                    for i, item in enumerate(data, start=1):

                        print("=" * 70)
                        print(f"Conversation #{i}")
                        print(f"Time : {item['time']}")
                        print()
                        print("Question:")
                        print(item["question"])
                        print()
                        print("Answer:")
                        print(item["answer"])
                        print()

                continue

            # -----------------------------------------
            # Clear History
            # -----------------------------------------

            elif lower == "clear history":

                history.clear()

                print("\nConversation history cleared.\n")

                continue
            elif lower == "export last":

                print()

                print(agent.export_last_output())

                print()

                continue

            # -----------------------------------------
            # Ask AI
            # -----------------------------------------

            print()

            response = agent.ask(question)

            print(response)

            print()

        except KeyboardInterrupt:

            print("\n\nInterrupted.\n")

            break

        except Exception as e:

            print("\nERROR")
            print(e)
            print()


if __name__ == "__main__":

    main()
