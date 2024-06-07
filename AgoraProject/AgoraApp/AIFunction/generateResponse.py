import openai


token = 'sk-proj-OSCVrMnZJImNGyTymdzCT3BlbkFJiQrSu5gKottJTryihymU'
chat_memory = []

def generateResponse(input_content):
    client = openai.OpenAI(api_key=token)
    chat_memory.append({'role': 'user', 'content':input_content})
    chat_completion = client.chat.completions.create(
        messages=chat_memory,
        model='gpt-4o',
    )
    chat_memory.append({'role':'assistant','content':chat_completion.choices[0].message.content})
    return chat_completion.choices[0].message.content