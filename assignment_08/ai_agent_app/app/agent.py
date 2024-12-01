import logging
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from .config import settings
from .models import TaskInput, AgentResponse, TaskType

logger = logging.getLogger(__name__)

class AIAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=settings.TEMPERATURE,
            model_name=settings.MODEL_NAME,
            openai_api_key=settings.OPENAI_API_KEY,
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="output"
        )
        self.search = DuckDuckGoSearchRun()
        self.setup_tools()
        self.setup_agent()

    def setup_tools(self):
        """Initialize tools available to the agent"""
        self.tools = [
            Tool(
                name="Search",
                func=self.search.run,
                description="Useful for searching the internet for current information"
            ),
            Tool(
                name="Calculator",
                func=self.calculate,
                description="Useful for performing mathematical calculations"
            ),
            Tool(
                name="Summarizer",
                func=self.summarize,
                description="Useful for summarizing long pieces of text"
            )
        ]

    def setup_agent(self):
        """Initialize the agent with tools and memory"""
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent="chat-conversational-react-description",
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True
        )


    def calculate(self, expression: str) -> str:
        """Safe calculator tool"""
        try:
            allowed_chars = set("0123456789+-*/(). ")
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            result = eval(expression, {"__builtins__": {}})
            return str(result)
        except Exception as e:
            return f"Error calculating: {str(e)}"

    def summarize(self, text: str) -> str:
        """Summarize text using LLM"""
        summary_prompt = PromptTemplate(
            input_variables=["text"],
            template="Please summarize the following text:\n\n{text}\n\nSummary:"
        )
        summary_chain = LLMChain(llm=self.llm, prompt=summary_prompt)
        return summary_chain.run(text)

    async def process_task(self, task_input: TaskInput) -> AgentResponse:
        """Process incoming tasks based on their type"""
        try:
            # Prepare the prompt based on task type
            print(f"task type is: {task_input.task_type}")
            if task_input.task_type == TaskType.RESEARCH:
                prompt = f"Research the following topic and provide detailed information with sources: {task_input.task}"
            elif task_input.task_type == TaskType.ANALYSIS:
                prompt = f"Analyze the following and provide insights: {task_input.task}"
            else:
                prompt = task_input.task

            if task_input.context:
                prompt += f"\nContext: {task_input.context}"

            response = await self.agent.arun(prompt)
            sources = self.memory.chat_memory.messages[-2].content if self.memory.chat_memory.messages else None

            return AgentResponse(
                response=response,
                sources=[sources] if sources else None,
                confidence=0.85
            )

        except Exception as e:
            logger.error(f"Error processing task: {str(e)}")
            raise