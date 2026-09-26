from agent import run_agent


def main():
    print("AI Research Agent")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        try:
            response = run_agent(user_input)
        except RuntimeError as error:
            print(f"Agent error: {error}")
            continue

        print("Agent:", response)


if __name__ == "__main__":
    main()