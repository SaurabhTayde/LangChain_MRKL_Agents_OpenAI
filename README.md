# Chat UI using LangChain, Chainlit and OpenAI

Part 1: "LangChain_ChainLit_OpenAI.py"
Chatbot in this respository is created using LangChain Framework, Open AI chatgpt API and ChainLit. Deployment is done using ChainLit which provides great Aesthetic UI for AI to user communication.

This repository can run in Github codespaces or locally. Please add your OpenAI API token and input it in .env (Rename example.env to .env). After running 'requirements.txt' please run following command to start the chat UI:

chainlit run LangChain_ChainLit_OpenAI.py -w

Part 2: "LangChain_Agents.py"
Above 'Part 1' only relies on LLM's (GPT-3.5) knowledge. But, With the help of Agents, we can integrate our LLM with search tool, calculator tool and many other tools. Here we have integrated search tool and calculator tool with OpenAI's GPT-3.5 turbo and used chainlit for UI. After running 'requirements.txt' please run following command to start the chat UI:

chainlit LangChain_Agents.py -w

