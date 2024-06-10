import openai


token = 'sk-proj-OSCVrMnZJImNGyTymdzCT3BlbkFJiQrSu5gKottJTryihymU'

def generateResponse(chat_memory):
    client = openai.OpenAI(api_key=token)
    chat_completion = client.chat.completions.create(
        messages=chat_memory,
        model='gpt-4o',
    )
    return chat_completion.choices[0].message.content