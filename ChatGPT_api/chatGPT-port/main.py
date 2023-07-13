import itertools

import openai
import wandb
from prettytable import PrettyTable
from tenacity import stop_after_attempt, wait_exponential, retry
from tqdm import tqdm
# 设置ChatGPT的API密钥
openai.api_key = "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"
system_gen_system_prompt = """Your job is to generate system prompts for GPT-4, given a description of the use-case and some test cases.

The prompts you will be generating will be for freeform tasks, such as generating a landing page headline, an intro paragraph, solving a math problem, etc.

In your generated prompt, you should describe how the AI should behave in plain English. Include what it will see, and what it's allowed to output. Be creative with prompts to get the best possible results. The AI knows it's an AI -- you don't need to tell it this.

You will be graded based on the performance of your prompt... but don't cheat! You cannot include specifics about the test cases in your prompt. Any prompts with examples will be disqualified.

Most importantly, output NOTHING but the prompt. Do not include anything else in your message."""

# 创建一个函数，用于调用ChatGPT API生成聊天响应
def generate_chat_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content":system_gen_system_prompt },
            {"role": "user",
             "content":user_input }
        ],
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    ).choices[0].text.strip()

    return response

if __name__ == '__main__':
    # 在主程序中，调用generate_chat_response函数并传入用户输入，以生成聊天响应
    user_input = "你好"
    response = generate_chat_response(user_input)
    print(response)