<p align="right">
  <a href="#documentacao-pt">Ver em Português 🇧🇷</a> | 
  <a href="#readme-en">View in English 🇺🇸</a>
</p>

<a id="readme-en"></a>
<h1>📑 DEVsigner's Assistant</h1>
<h3>Hybrid Contextual AI for Developers & Designers</h3>

<p><strong>The balance between code logic and design sensitivity.</strong></p>

<p>
The <strong>DEVsigner's Assistant</strong> is an AI assistant designed to optimize the workflow of Front-end Developers and UX Designers, combining LLM-based architecture with a carefully crafted visual experience.
</p>

<p>
This project was developed as the final project for the <strong>Introduction to LLMs</strong> track of the TIC em Trilhas residency (PUC-Rio & Serratec).
</p>

<br>

<h2>✨ Overview</h2>

<p>The project aims to unite:</p>

<ul>
  <li>Contextual intelligence based on technical documents</li>
  <li>Interface with a consistent visual identity</li>
  <li>Real-time streaming responses</li>
  <li>Hybrid architecture with conversational flow orchestration</li>
</ul>

<p>
The result is an assistant capable of providing contextualized answers while maintaining a fluid and pleasant experience.
</p>

<br>

<h2>🎨 Visual Identity & UX</h2>

<p>
The interface was built based on the <strong>Dracula Theme</strong> aesthetic, prioritizing contrast, readability, and modernity.
</p>

<h4>Key UX Decisions</h4>

<ul>
  <li>Custom CSS injected into Streamlit</li>
  <li>Fully responsive layout</li>
  <li>Personalized focus states</li>
  <li>Vector icons via Font Awesome</li>
  <li>Sidebar with branding and quick access to portfolio</li>
</ul>

<p>
The visual proposal reinforces the core concept of the project: technology with design sensitivity.
</p>

<br>

<h2>🏗️ System Architecture</h2>



<h4>Interface Layer</h4>
<ul>
  <li><strong>Streamlit</strong> — Interface rendering and user interaction</li>
</ul>

<h4>Orchestration Layer</h4>
<ul>
  <li><strong>LangGraph</strong> — State management and conversational flows</li>
</ul>

<h4>Intelligence Layer</h4>
<ul>
  <li><strong>OpenRouter</strong> — Gateway for Large Language Models (LLMs)</li>
  <li><strong>RAG (Retrieval-Augmented Generation)</strong> — Context retrieval from technical PDF documents</li>
</ul>

<h4>Interaction Experience</h4>
<ul>
  <li>Real-time response streaming</li>
  <li>Contextualized conversation</li>
  <li>Modular structure for future expansion</li>
</ul>

<br>

<h2>🚀 How to Run the Project</h2>

<h4>1. Prerequisites</h4>

<ul>
  <li>Python 3.10+</li>
  <li>OpenRouter API Key</li>
</ul>

<br>

<h4>2. Environment Variables Configuration</h4>

<p>
To protect sensitive credentials, use environment variables.
</p>

<ol>
  <li>Clone the repository</li>
  <li>Create a <code>.env</code> file in the project root</li>
  <li>Add your key according to the template:</li>
</ol>

```env
OPENROUTER_API_KEY=your_key_here
```

<h4>3. Installation</h4>

```
pip install -r requirements.txt
```

<h4>4. Execution</h4>

```
streamlit run your_file.py
```


<h2>📁 Recommended Project Structure</h2>

```
.
├── .git
├── README.md
├── __pycache__
├── .env
├── .gitignore
├── .streamlit
├── chatbot_hybrid.py
├── interface_hybrid.py
├── requirements.txt
├── venv
```


<h2>📌 Future Improvements</h2>

<ul>
<li>User authentication</li>
<li>Persistent conversation history</li>
<li>Integration with a dedicated vector database</li>
<li>Cloud deployment (Streamlit Cloud, Render, AWS)</li>
<li>Multi-document mode</li>
</ul>


<h2>👩‍💻 About the Author</h2>

<p>
<strong>Giselle Garcia</strong><br>
Full-Stack Developer & UX Designer
</p>
<p>
Product Designer (UFF).<br>
Full Stack Developer (SENAI / Serratec).<br>
Focus on React, Java, and Spring Boot.
</p>


<br>
<hr>
<br>
<a id="documentacao-pt"></a>
<p>🇧🇷</p>
<h1>📑 DEVsigner's Assistant</h1>
<h3>IA Contextual Híbrida para Desenvolvedores & Designers</h3>

<p><strong>O equilíbrio entre a lógica do código e a sensibilidade do design.</strong></p>

<p>
O <strong>DEVsigner's Assistant</strong> é um assistente de IA projetado para otimizar o workflow de Desenvolvedores Front-end e UX Designers, combinando arquitetura baseada em LLMs com uma experiência visual cuidadosamente construída.
</p>

<p>
Este projeto foi desenvolvido como conclusão da trilha <strong>Introdução a LLMs</strong> da residência TIC em Trilhas (PUC-Rio & Serratec).
</p>

<br>

<h2>✨ Visão Geral</h2>

<p>O objetivo do projeto é unir:</p>

<ul>
  <li>Inteligência contextual baseada em documentos técnicos</li>
  <li>Interface com identidade visual consistente</li>
  <li>Respostas em tempo real via streaming</li>
  <li>Arquitetura híbrida com orquestração de fluxo conversacional</li>
</ul>

<p>
O resultado é um assistente capaz de fornecer respostas contextualizadas enquanto mantém uma experiência fluida e agradável.
</p>

<br>

<h2>🎨 Identidade Visual & UX</h2>

<p>
A interface foi construída com base na estética <strong>Dracula Theme</strong>, priorizando contraste, legibilidade e modernidade.
</p>

<h4>Principais decisões de UX</h4>

<ul>
  <li>CSS customizado injetado no Streamlit</li>
  <li>Layout totalmente responsivo</li>
  <li>Estados de foco personalizados</li>
  <li>Ícones vetoriais via Font Awesome</li>
  <li>Barra lateral com branding e acesso rápido ao portfólio</li>
</ul>

<p>
A proposta visual reforça o conceito central do projeto: tecnologia com sensibilidade de design.
</p>

<br>

<h2>🏗️ Arquitetura do Sistema</h2>

<h4>Camada de Interface</h4>
<ul>
  <li><strong>Streamlit</strong> — Renderização da interface e interação com o usuário</li>
</ul>

<h4>Camada de Orquestração</h4>
<ul>
  <li><strong>LangGraph</strong> — Gerenciamento de estados e fluxos conversacionais</li>
</ul>

<h4>Camada de Inteligência</h4>
<ul>
  <li><strong>OpenRouter</strong> — Gateway para modelos de linguagem (LLMs)</li>
  <li><strong>RAG (Retrieval-Augmented Generation)</strong> — Recuperação de contexto a partir de documentos PDF técnicos</li>
</ul>

<h4>Experiência de Interação</h4>
<ul>
  <li>Streaming de respostas em tempo real</li>
  <li>Conversação contextualizada</li>
  <li>Estrutura modular para expansão futura</li>
</ul>

<br>

<h2>🚀 Como Executar o Projeto</h2>

<h4>1. Pré-requisitos</h4>

<ul>
  <li>Python 3.10+</li>
  <li>Chave de API do OpenRouter</li>
</ul>

<br>

<h4>2. Configuração de Variáveis de Ambiente</h4>

<p>
Para proteger credenciais sensíveis, utilize variáveis de ambiente.
</p>

<ol>
  <li>Clone o repositório</li>
  <li>Crie um arquivo <code>.env</code> na raiz do projeto</li>
  <li>Adicione sua chave conforme o modelo:</li>
</ol>

```env
OPENROUTER_API_KEY=sua_chave_aqui
```

<br>

<h4>3. Instalação</h4>

```bash
pip install -r requirements.txt
```

<br>

<h4>4. Execução</h4>

```bash
streamlit run seu_arquivo.py
```

<br>

<h2>📁 Estrutura Recomendada do Projeto</h2>

```bash
.
├── .git
├── README.md
├── __pycache__
├── .env
├── .gitignore
├── .streamlit
├── chatbot_hibrido.py
├── interface_hibrida.py
├── requirements.txt
├── venv
```

<br>

<h2>📌 Possíveis Evoluções</h2>

<ul>
  <li>Autenticação de usuários</li>
  <li>Histórico persistente de conversas</li>
  <li>Integração com banco vetorial dedicado</li>
  <li>Deploy em ambiente cloud (Streamlit Cloud, Render, AWS)</li>
  <li>Modo multi-documento</li>
</ul>

<br>

<h2>👩‍💻 Sobre a Autora</h2>

<p>
<strong>Giselle Garcia</strong><br>
Full-Stack Developer & UX Designer
</p>

<p>
Designer de Produto pela UFF.<br>
Desenvolvedora Full Stack pelo SENAI/ Serratec.<br>
Foco em React, Java e Spring Boot.
</p>
