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
