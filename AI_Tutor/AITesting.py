from groq import Groq

client = Groq(api_key="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")  # Add your API key here

completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": "Hello!"
            
        }
    ],
    temperature=0.7,
    max_completion_tokens=512,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


