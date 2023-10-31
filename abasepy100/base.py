from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from sqlalchemy import create_engine
import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
import pymysql


class DatabaseConnector:
    def __init__(self, db_user=None, db_password=None, db_host=None, db_name=None):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
        self.db = None
        self.connection_status = {"connected": False, "message": None}

    def connect(self):
        if None in [self.db_user, self.db_password, self.db_host, self.db_name]:
            self.connection_status["message"] = "All database credentials must be provided"
            return self.connection_status
        
        try:
            self.db = SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")
            self.connection_status["connected"] = True
            self.connection_status["message"] = "Connection successful"
            
        

        except Exception as e:
            self.connection_status["message"] = str(e)
        
        return self.connection_status
    
    def getdbinstance(self):
        if None in [self.db_user, self.db_password, self.db_host, self.db_name]:
            self.connection_status["message"] = "All database credentials must be provided"
            return self.connection_status
        
        try:
            self.db = SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")
        
        except Exception as e:
            self.connection_status["message"] = str(e)
        
        return self.db
 
class AgentRunner:
    def __init__(self, llm, toolkit, verbose=True,
                  agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION):
        self.llm = llm
        self.toolkit = toolkit
        self.verbose = verbose
        self.agent_type = agent_type
        self.agent_runner = None
        self.error = None

        try:
            # Initialize the agent_runner instance here
            self.agent_runner = create_sql_agent(
                llm=self.llm,
                toolkit=self.toolkit,
                verbose=self.verbose,
                agent_type=self.agent_type
            )
            
            # Check for initialization success or error
            if self.agent_runner is not None:
                print("Agent runner instance:", self.agent_runner)
            else:
                print("Error occurred during initialization.")
        except Exception as e:
            self.error = e
            print("Error occurred:", e)

    def run(self, query):
        if self.agent_runner:
            return self.agent_runner.run(query)
        else:
            print("Agent runner is not initialized.")
            return None

    
    
