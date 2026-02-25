import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

load_dotenv()

# 1. Template Customizado (Focado em Consultar Contexto Técnico)
template = """
Você é o assistente técnico de Design e Front-end da Giselle Garcia. 

INSTRUÇÕES DE CONTEXTO:
1. Se o CONTEXTO abaixo contiver informações, priorize-as e responda estritamente com base nelas.
2. Se o CONTEXTO estiver vazio ou não contiver a resposta, utilize seu conhecimento geral como expert em Front-end e UX/UI para ajudar o usuário, mas mencione discretamente que está usando conhecimento geral.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}
"""

chat_com_contexto_template = ChatPromptTemplate.from_template(template)

# 2. Configuração do Modelo via OpenRouter
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    streaming=True
)

# Pipeline
qna_chain = chat_com_contexto_template | llm

# 3. Estado da Aplicação (TypedDict é melhor para o LangGraph)
class State(TypedDict):
    pergunta: str
    contexto: list  # Lista de documentos carregados (ex: do PyPDFLoader)
    resposta: str

# 4. Função de Resposta (Ajustada para extrair conteúdo dos documentos)
def generate(state: State):
    # Concatena o contexto (vindo do PyPDFLoader ou lista vazia)
    docs_content = "\n\n".join(doc.page_content for doc in state["contexto"])
    
    # IMPORTANTE: Usamos .stream() para permitir o efeito de digitação
    return {"resposta": qna_chain.stream({
        "pergunta": state["pergunta"], 
        "contexto": docs_content
    })}

# 5. Grafo da Aplicação
workflow = StateGraph(State)
workflow.add_node("generate", generate)
workflow.add_edge(START, "generate")
workflow.add_edge("generate", END)

app = workflow.compile()