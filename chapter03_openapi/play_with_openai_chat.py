import os
import openai


system_instruction = """
너는 지금부터 햄버거 판매를 하는 AI 이고 아래 3가지 햄버거만 판매할 수 있어.
- 치즈버거
- 쿼터파운더
- 새우버거
해당 기준으로 대답하면돼
"""
openai.api_key = os.getenv("CHATGPT_OPEN_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":system_instruction},
        {"role": "user", "content":"어떤 햄버거를 판매하나요? 그리고 추천 햄버거는 뭔가요?"}
    ]
)

resp = response.to_dict_recursive()
print(resp)


