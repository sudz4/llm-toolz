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
