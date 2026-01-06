def generate_response(prompt):
    return f"AI generated response: {prompt}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    response = generate_response(prompt)
    print(response)
