import os
import openai

openai.api_key = os.getenv("CHATGPT_OPEN_API_KEY")
#openai.api_key = os.getenv('OPENAI_API_KEY')

query = input("압력하세요:")
prompt = """
다음 문장이 긍정이면 positive, 부정이면 negative를 만드시오.
text: 이 영화 최악이다
sentiment: negative

text: 배우들이 연기를 너무 잘하네
sentiment: positive

text:"""

prompt = prompt + query + "\nsentiment:"

response = openai.Completion.create(model="text-davinci-003",
                                    prompt=prompt,
                                    temperature=0,
                                    max_tokens=7)

print(response)



