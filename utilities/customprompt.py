# flake8: noqa
from langchain.prompts import PromptTemplate

template = """{summaries}
Please reply to the question using only the information present in the text above. 
If the question is written by Japanese, the answer must be in Japanese language, otherwise in Chinese language.
Include references to the sources you used to create the answer if those are relevant ("SOURCES"). 
If you can't find it, reply politely that the information is not in the knowledge base.
Question: {question}
Answer:"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)

question_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question. If the question is written by Japanese, the generated question must be in Japanese language, otherwise in Chinese language.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(question_template)

