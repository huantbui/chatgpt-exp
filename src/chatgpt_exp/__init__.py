import openai

def main():
    """Entry point for the application script"""
    openai.api_key = "YOUR_API_KEY_HERE"
    model_engine = "gpt-3.5-turbo"
    print("Hello! Welcome to ChatGPT Experiment, please fill out the promt to start convo with our ChatGPT")
    # response = openai.ChatCompletion.create(
    #     model='gpt-3.5-turbo',
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": "Hello, ChatGPT!"},
    #     ])
    # message = response.choices[0]['message']
    # print("{}: {}".format(message['role'], message['content']))

    messages = [{"role": "system", "content":
                "You are a intelligent assistant."}]
    while True:
        message = input("You: ")
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
