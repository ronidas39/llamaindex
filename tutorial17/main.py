from llama_index.llms.openai import OpenAI
from pydantic import BaseModel
from llama_index.program.openai import OpenAIPydanticProgram

llm=OpenAI(model="gpt-4o")
# response=llm.complete("get information on contient,polulation and currency for India")
# print(response)

class Country(BaseModel):
    name: str
    continent: str
    population: str
    currency: str

prompt_template_str="""
generate an information on a country,
with name,continent,population and currency
using the {country_name} as input
"""
instruction=OpenAIPydanticProgram.from_defaults(
    output_cls=Country,
    prompt_template_str=prompt_template_str,llm=llm,verbose=True

)
response=instruction(country_name="china",description="Data model for a country")
print(type(response))
