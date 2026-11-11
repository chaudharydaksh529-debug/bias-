from groq_client import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to test bias mitigation: ").strip()
    if not prompt:
        print("No prompt provided. Exiting activity.")
        return

    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial Response: {initial_response}")

    modified_prompt = input("Modify the prompt to mitigate bias (or press Enter to keep it the same): ").strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified Response: {modified_response}")
    else:
        print("No modification made to the prompt. Exiting activity.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_promt = input("Enter a long prompt to test token limit: ").strip()
    if long_promt:
        long_response = generate_response(long_promt, temperature=0.3, max_tokens=512)
        preview = (long_response[500] + "..." if len(long_response) > 500 else long_response)
        print(f"\nResponse (first 500 chars): {preview}")
    else:
        print("No prompt provided. Exiting activity.")
    short_prompt = input("Enter a short prompt to test token limit: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=512)
        print(f"\nResponse: {short_response}")
    else:
        print("No prompt provided. Exiting activity.")

def run_activity():
    print("\n=== AI LEARNIBG ACTIVITIES ===\n")
    print("Choose an activity:")
    print("1) Bias mitigation")
    print("2) Token limit")
    choice = input("> ").strip()
    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choosse 1 or 2.")

if __name__ == "__main__":
    run_activity()