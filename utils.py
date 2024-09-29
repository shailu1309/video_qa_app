# Openai interactions

import openai

openai.api_key = 'your_openai_api_key'  # Replace with your actual API key

def ask_question(transcript, question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Based on the following transcript, answer this question: {question}\n\nTranscript: {transcript}"}
        ]
    )
    return response['choices'][0]['message']['content']
