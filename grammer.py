import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    matches = tool.check(text)

    if not matches:
        print("\nNo grammar mistakes found.")
        return

    print("\nGrammar issues found:\n")

    for i, match in enumerate(matches, start=1):
        wrong_part = text[match.offset: match.offset + match.error_length]

        print(f"{i}. Problem: {match.message}")
        print(f"   Wrong text: {wrong_part}")

        if match.replacements:
            print(f"   Suggestions: {', '.join(match.replacements[:5])}")
        else:
            print("   Suggestions: No suggestion available")

        print()

    corrected_text = language_tool_python.utils.correct(text, matches)
    print("Corrected sentence:")
    print(corrected_text)


print("=== English Grammar Checker ===")

while True:
    user_text = input("\nEnter a sentence or paragraph: ")
    check_grammar(user_text)

    again = input("\nDo you want to check again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break