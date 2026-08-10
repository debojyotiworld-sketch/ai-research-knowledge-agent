from agent import run_agent


def main():
    print("AI Research Agent")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        response = run_agent(user_input)

        print("Agent:", response)


if __name__ == "__main__":
    main()