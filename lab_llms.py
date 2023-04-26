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
# prompt = "Write me a poem about the tiniest shark to ever live."
prompt = "Write me a story about how the software company ServiceNow was founded."

#prints to termnal
llm_output = llm(prompt)
print(llm_output)

# saves output to file in directory
with open("catena_out_NEW", "w") as file:
    file.write(llm_output)

# EXAMPLE -> if you need to append later
# with open("output.txt", "a") as file:
#     file.write(llm_output)

"""
Notes: using .env
find_dotenv(): This function searches for a .env file in the current directory and its parent directories, recursively. 
-It returns the path to the first .env file it finds. 
-This is useful when you have a project with multiple nested directories and you want to locate the .env file without hardcoding its path.

load_dotenv(): This function reads the contents of the .env file and loads the key-value pairs as environment variables. 
These environment variables can then be accessed using os.environ in your Python code. 
The load_dotenv() function takes the path of the .env file as its argument.

"""

# --------------------------------------------------------------
# Prompt Templates: Manage prompts for LLMs
# --------------------------------------------------------------

prompt = PromptTemplate(
    input_variables=[
    "module", # i.e. ITSM
    "platform", 
    "release_version"],

    template="""
    For the {release_version} release;
    list all ServiceNow {module} capabilities,
    list all ServiceNow {platform} capabilies.
    """
)

prompt.format(module="IT Service Management",
              platform="Now Platform",
              release_version="Utah")

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(
    """My company is deploying ServiceNow {module}.
    We are also deploying core {platform} configurations and components, 
    as well as other {platform} capabilites."""
))

# --------------------------------------------------------------
# Chains: Combine LLMs and prompts in multi-step workflows
# --------------------------------------------------------------




# # --------------------------------------------------------------
# # Agents: Dynamically Call Chains Based on User Input
# # --------------------------------------------------------------


# # --------------------------------------------------------------
# # Memory: Add State to Chains and Agents
# # --------------------------------------------------------------