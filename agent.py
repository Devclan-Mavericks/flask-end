from langchain.agents.agent_types import AgentType
import os
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd
from dotenv import load_dotenv



def agent(df):
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-4"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    return agent
































































