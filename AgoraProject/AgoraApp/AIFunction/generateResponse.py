import openai


token = 'sk-proj-OSCVrMnZJImNGyTymdzCT3BlbkFJiQrSu5gKottJTryihymU'
def generateResponse(input_content):
    client = openai.OpenAI(api_key=token)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_content,
            }
        ],
        model="gpt-4o",
    )

    return chat_completion.choices[0].message.content