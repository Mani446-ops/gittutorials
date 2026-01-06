def generate_response(prompt):
    return f"GenAI response for: {prompt}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    print(generate_response(prompt))
