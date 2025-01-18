import ollama

response = ollama.chat(
    model='gemma2:2b',
    messages=[{
        'role': 'user',
        'content': 'What is the fastest animal on the planet?',
    }]
)

print('-------------------------')

print(response['message']['role'])

print(response['message']['content'])