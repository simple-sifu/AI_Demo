# !pip install langchain langchina-chroma langchina-openai

import getpass
import os

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

from langchain_core.documents import Document

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"}
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"}
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care..",
        metadata={"source": "fish-pets-doc"}
    ),  
    Document(
        page_content="Parrots are intelligent birds that can learn to talk and perform tricks.",
        metadata={"source": "bird-pets-doc"}
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around..",
        metadata={"source": "mammal-pets-doc"}
    ),
    Document(
        page_content="LangChain helps building LLM-based applications.",
        metadata={"source": "lang-chain-doc"}
    ),
    Document(
        page_content="LLMs have changed the scene in AI and ML",
        metadata={"source": "llm-doc"}
    ),
]

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)

# No need to embed the query, the vectorstore will do it for you
'''
It does embed "cat" — you just don’t do it yourself.

When you built the store with embedding=OpenAIEmbeddings(), 
Chroma kept that embedder. On similarity_search_with_relevance_scores("cat", 3)
it roughly:

1. Embeds "cat" with that same model
2. Compares that vector to the stored document vectors
3. Returns the closest docs + scores

So you pass a string; the vectorstore handles the embedding. 
You only need to embed the query yourself if you’re calling a lower-level API 
that expects a vector, not text.
'''

results = vectorstore.similarity_search_with_relevance_scores("cat", 3)
for doc, score in results:
    print(f"Relevance score: {score}")
    print(doc.page_content)
    print("="*15)