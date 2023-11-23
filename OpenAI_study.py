from openai import OpenAI
import telegram
import asyncio
import time

token = "6824706855:AAEGeRWBJ3hNAslgVLBhZN-FKNLoIPPL4sI"
bot = telegram.Bot(token = token)
public_chat_name = "@opensw_yoon_ChatGPT"
chat_id = "6917261069"

client = OpenAI(
    api_key='api token key'
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "알고리즘 종류에 대해 설명해줘 json"}
  ],
  response_format={"type": "json_object"}
)

id_channel = asyncio.run(bot.sendMessage(public_chat_name, text=completion.choices[0].message.content)).chat_id
#print(completion.choices[0].message.content)