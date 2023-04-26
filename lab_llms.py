"""
Setup steps:
1-open terminal
git clone
cd llm-toolz
python3 -m venv llm_venv
source llm_venv/bin/activate

2-pip install -r requirements.txt

3-create .env file in project root directory

4-create new environment vars if you want

* also install the code shell command form the terminal.
set your venv and cd to the directory and then open vs code
-write the shell command 'code' in the computer terminal
"""

# import libs
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents.load_tools import get_all_tool_names
from langchain import ConversationChain
from langchain.utilities import SerpAPIWrapper

# import AND load KEY vars
from dotenv import load_dotenv, find_dotenv # import -> reads the contents of the .env file and loads the key
load_dotenv(find_dotenv()) # load KEYs (your environment vars)

# you can access your KEY vars and environment vars when you need to
import os
# api_KEY = os.environ['OPEN_API_KEY']

# --------------------------------------------------------------
# LLMs: Get predictions from a language model
# --------------------------------------------------------------

llm = OpenAI(model_name="text-davinci-003")
prompt = "Write a poem about the smallest shark to ever live"

#prints to termnal
llm_output = llm(prompt)
print(llm_output)

# saves output to file in directory
with open("catena_out_NEW", "w") as file:
    file.write(llm_output)

# EXAMPLE -> if you need to append later
# with open("output.txt", "a") as file:
#     file.write(llm_output)