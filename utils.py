from typing import Any
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def get_chat_response(prompt,memory,openai_api_key) -> Any:

   model = ChatOpenAI(model="gpt-3.5-turbo",api_key=openai_api_key)

   chain = ConversationChain(llm=model, memory=memory)

   response = chain.invoke({"input":prompt})

   return response['response']