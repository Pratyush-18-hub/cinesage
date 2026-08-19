from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
model = ChatGroq(model = "openai/gpt-oss-120b",temperature = 0.9)

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import Optional ,List
from langchain_core.output_parsers import PydanticOutputParser
# from langchain_core

class movie(BaseModel):
    tittle:str
    director:str
    cast:List[str]
    release_year:Optional[int]
    rating:float
    summary:str

parser = PydanticOutputParser(pydantic_object=movie)

prompt = ChatPromptTemplate.from_messages([(
     "system",
        """
Extract the information from the paragraph 
  {format_instructions}
"""
),(
    "human",
    "{paragraph}"
)])

para = input("Enter the paragraph: ")
final_prompt = prompt.invoke(
    {"paragraph": para,"format_instructions": parser.get_format_instructions()}
)

response = model.invoke(final_prompt)
moviedata = parser.parse(response.content)
print(response.content)
print(moviedata)