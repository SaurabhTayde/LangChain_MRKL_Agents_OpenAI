from langchain import PromptTemplate, LLMChain
import os

from dotenv import load_dotenv
import chainlit as cl

# Load environment variables from .env file
load_dotenv()

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

template = """
You are a helpful AI assistant. Provide the correct answer for the question politely. Explain the answer in detail if required.

{question}
"""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose = True)

    return llm_chain

@cl.langchain_run
async def run(agent, input_str):
    res = await cl.make_async(agent)(input_str, callbacks=[cl.ChainlitCallbackHandler()])
    await cl.Message(content=res["text"]).send()
