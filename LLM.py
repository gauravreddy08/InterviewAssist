from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class LLM():
    def __init__(self, model_name='gpt-4o'):

        self.model = OpenAI()
        self.model_name = model_name

        self.messages = []

        system_prompt_file ='system.txt'
        if not os.path.exists(system_prompt_file):
            raise FileNotFoundError
        
        file = open(system_prompt_file, 'r')
        system_prompt = file.read()

        self._append('system', system_prompt)

    def call(self, prompt=None):

        if prompt: self._append('user', prompt)
        
        completion = self.model.chat.completions.create(
                        model=self.model_name,
                        messages=self.messages, 
                    )
        
        response = completion.choices[0].message.content
        return response
    
    def _append(self, role: str, content: str):
        self.messages.append({'role': role,
                              'content': str(content)})


        



