from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
import os
import chainlit as cl
from dotenv import load_dotenv

# os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
# os.environ["SERPAPI_API_KEY"] = "SERPAPI_API_KEY"

# Load environment variables from .env file
load_dotenv()

# The search tool has no async implementation, we fall back to sync
@cl.langchain_factory(use_async=False)
def load():
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    llm1 = OpenAI(temperature=0, streaming=True)
    search = SerpAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
    ]
    
    return initialize_agent(
        tools, llm1, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    
    #return initialize_agent(
    #    tools, llm1, agent="chat-zero-shot-react-description", verbose=True
    #)

# template = """
# You are a helpful AI assistant. Provide the correct answer for the question politely. Explain the answer in detail if required.

# {question}
# """

# @cl.langchain_factory(use_async=True)
# def factory():
#     prompt = PromptTemplate(template=template, input_variables=["question"])
#     llm_chain = LLMChain(prompt=prompt, llm=llm)

#     return llm_chain

# @cl.langchain_run
# async def run(agent, input_str):
#     res = await cl.make_async(agent)(input_str, callbacks=[cl.ChainlitCallbackHandler()])
#     await cl.Message(content=res["text"]).send()