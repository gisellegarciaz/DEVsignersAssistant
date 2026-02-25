import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import AIMessage, HumanMessage
from chatbot_hibrido import app  # Seu arquivo com o grafo adaptado
import uuid

# 1. Configuração Visual
st.set_page_config(
    layout='wide', 
    page_title='Giselle Garcia | IA Context Assistant', 
    page_icon='📄'
)

# Font Awesome para ícones
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

# Estilo Dracula
st.markdown(
    """
    <style>
    .stApp {
        border-top: 15px solid #bd93f9 !important;
    }

    /* O input "amarelinho" do Dracula quando selecionado */
    .stChatInput:focus-within {
        border-color: #f1fa8c !important;
        box-shadow: 0 0 0 1px rgba(241, 250, 140, 0.8) !important;
        border-radius: 8px !important;
    }

    /* Remove bordas fantasmas vermelhas */
    .stChatInput div {
        border-color: transparent !important;
    }

    .stChatInput button {
        background-color: #bd93f9 !important;
    }
    
    .stChatInput button svg {
        fill: #282a36 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1><i class="fa-solid fa-microchip" style="color: #bd93f9;"></i> DEVsigner\'s Assistant</h1>', unsafe_allow_html=True)
st.markdown('<h5>Tire suas dúvidas sobre Front-end e UX usando seus guias técnicos.</h5>', unsafe_allow_html=True)

# st.title("DEVsigner's Assistant 📑")
# st.subheader("Tire suas dúvidas sobre Front-end e UX, usando seus próprios guias e documentações! 🚀")

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown('<h2><i class="fa-solid fa-sliders"></i>  Menu</h2>', unsafe_allow_html=True)
    
    # Upload do PDF
    uploaded_file = st.file_uploader("Suba seu PDF técnico pra contexto:", type=["pdf"])
    
    # Botão de Reset
    if st.button("Limpar Conversa"):
        st.session_state.message_history = [
            AIMessage(content='Histórico limpo! Vamos começar do zero?!')
        ]
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()

    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        """
        <style>
            .profile-card {
                text-align: center; 
                padding: 20px;
            }
            .profile-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                text-decoration: none;
                background-color: #282a36;
                color: #f8f8f2 !important;
                padding: 10px;
                border-radius: 8px;
                font-size: 0.85rem;
                width: 100%;
                transition: all 0.3s ease-in-out;
                border: 1px solid transparent;
            }
            .profile-btn:hover {
                background-color: #bd93f9;
                color: #282a36 !important;
                transform: translateY(-2px);
                border-color: #282a36;
            }
        </style>
        
        <div class="profile-card">
            <p style="font-size: 0.7rem; color: #6272a4; margin-bottom: 0; font-family: sans-serif;">Desenvolvido por:</p>
            <h2 style="color: #bd93f9; margin-bottom: 0; font-family: sans-serif;">Giselle Garcia</h2>
            <p style="font-size: 0.8rem; color: #f8f8f2; margin: 0px; font-weight: 500;">
                Full-Stack Developer & UX Designer</p>
            <div style="display: flex; gap: 10px; justify-content: center; margin-top: 15px;">
                <a href="https://github.com/gisellegarciaz" target="_blank" class="profile-btn">
                    <i class="fa-brands fa-github"></i> GitHub
                </a>
                <a href="https://linkedin.com/in/giselle-garcia" target="_blank" class="profile-btn">
                    <i class="fa-brands fa-linkedin"></i> LinkedIn
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- LÓGICA DE PROCESSAMENTO DO PDF ---
# Usamos o session_state para não ter que re-carregar o PDF a cada mensagem enviada
if "docs" not in st.session_state:
    st.session_state.docs = None

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    from langchain_community.document_loaders import PyPDFLoader
    loader = PyPDFLoader("temp.pdf")
    st.session_state.docs = loader.load()
    os.remove("temp.pdf")

# --- HISTÓRICO DE CONVERSA ---
if 'message_history' not in st.session_state:
    st.session_state.message_history = [
        AIMessage(content="Olá! Faça o upload de um PDF técnico (como um guia de CSS ou UX), para começarmos a análise, ou apenas faça sua pergunta.")
    ]

# Exibição da conversa
for message in st.session_state.message_history:
    role = "assistant" if isinstance(message, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(message.content)
        

user_input = st.chat_input("Pergunte algo (com ou sem documento)...")

if user_input:
    # Mostra pergunta do usuário
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.message_history.append(HumanMessage(content=user_input))
    
    # Resposta com efeito de digitação
    with st.chat_message("assistant"):
        contexto_para_ia = st.session_state.docs if st.session_state.docs else []
        
        # O invoke aqui chama o grafo, que por sua vez retorna o gerador de stream do nó
        output = app.invoke({
            'pergunta': user_input,
            'contexto': contexto_para_ia
        })
        
        # A mágica do efeito "ChatGPT"
        full_response = st.write_stream(output['resposta'])
        
    st.session_state.message_history.append(AIMessage(content=full_response))
    st.rerun()