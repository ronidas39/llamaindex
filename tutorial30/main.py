from pydantic import BaseModel,Field
from typing import Literal,Optional
from datetime import date
from llama_index.readers.file import PDFReader
from pathlib import Path
import json
from llama_index.llms.openai import OpenAI

llm=OpenAI(model="gpt-4o")



class Insurance(BaseModel):
    Customer_Name: str = Field(..., description="Full name of the customer.")
    Policy_Number: str = Field(..., description="Unique policy number assigned to the customer.")
    Insurance_Type: str = Field(..., description="Type of insurance purchased (e.g., Business, Health, etc.).")
    Purchase_Date: date = Field(..., description="Date when the insurance policy was purchased.")
    Premium: str = Field(..., description="Annual premium amount for the insurance policy.")
    Insurer: str = Field(..., description="Name of the insurance company providing the policy.")
    Invoice_Number: str = Field(..., description="Unique invoice number associated with the policy payment.")
    Payment_Type: str = Field(..., description="Type of payment method used (e.g., Debit Card, Credit Card, etc.).")



pdf_reader=PDFReader()
docs=pdf_reader.load_data(file=Path("/Users/roni/Documents/GitHub/llamaindex/tutorial30/sample.pdf"))
sllm=llm.as_structured_llm(Insurance)
for doc in docs:
    response=sllm.complete(doc.text)
    json_response=json.loads(response.text)
    print(json.dumps(json_response,indent=2))