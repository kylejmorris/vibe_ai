# VibeAI 🌐

<div align="center">

[![Versão](https://img.shields.io/badge/version-0.1.0-blue.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)
[![Status](https://img.shields.io/badge/status-prototype-orange.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)
[![Licença](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)

> *Desenvolvido para a AGIHouseSF Hackathon* 🏆

</div>

---

## 📋 Visão Geral

O **VibeAI** é uma plataforma inteligente de inteligência de relacionamentos que consolida e analisa os dados da sua rede social de fontes diversas. Ele transforma informações de contatos dispersas em uma ferramenta poderosa para networking profissional, indicações estratégicas e insights acionáveis.

### ✨ Principais Recursos

<table>
  <tr>
    <td width="50%" align="center"><b>🔍 Consultas Inteligentes</b></td>
    <td width="50%" align="center"><b>🤝 Recomendações Estratégicas</b></td>
  </tr>
  <tr>
    <td>
      <ul>
        <li>"Quem na minha rede investe em empresas de IA de estágio inicial?"</li>
        <li>"Identifique contatos que deixaram seus cargos recentemente"</li>
        <li>"Encontre conexões no Google com experiência em machine learning"</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>"Seu amigo Jim está explorando novos projetos; sua contato Helen investe em fundadores. Sugira uma introdução com os detalhes de contato."</li>
        <li>"Alex precisa de um designer UX; seu contato Taylor está ativamente procurando novas oportunidades."</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🏗️ Arquitetura

O VibeAI é construído sobre uma arquitetura modular e extensível, focada em privacidade e flexibilidade.

<div align="center">

mermaid
graph TD
    A[Fontes de Dados] -->|Ingestão| B[Banco de Dados Local]
    B -->|Dados Estruturados| C[Camada de Análise IA]
    C -->|Insights e Recs| D[Interface do Usuário]
    D -->|Consultas do Usuário| C
    C -.->|Contexto| D


</div>

### 1. 📥 Camada de Ingestão de Dados

| Fonte | Tipo de Dado | Status |
|--------|-----------|--------|
| LinkedIn | Perfis, Conexões, Mensagens | ⏳ Em Progresso |
| Messenger | Histórico de Chat & Contexto | 🔜 Planejado |
| Email | Contatos & Correspondência | 🔜 Planejado |
| Twitter/X | Posts Públicos & Interações | 🔜 Planejado |

*Objetivo: Fornecer um framework de ingestão flexível para integrar facilmente novas fontes de dados via coletores personalizados.*

### 2. 💾 Banco de Dados Local

- **Função Principal**: Armazena com segurança pessoas, dados de rede e histórico de interações.
- **Tecnologia**: Movido pelo ChromaDB para armazenamento vetorial eficiente e busca semântica.
- **Foco em Privacidade**: Todos os dados permanecem na sua máquina local.

### 3. 🧠 Camada de Análise de IA

- **Geração de Insights**: Analisa sua rede para revelar oportunidades e conexões valiosas.
- **Motor NLP**: Compreende consultas complexas e contextos de relacionamento.
- **Aprendizado Adaptativo**: Refina recomendações com base nas interações e feedback do usuário.

### 4. 🖥️ Opções de Interface

- 🖱️ **Aplicativo Desktop**: Experiência nativa para usuários avançados.
- 🌐 **UI Streamlit**: Interface web rápida para acesso rápido.
- ⚛️ **Aplicativo Web React**: Cliente web moderno e completo.
- 📟 **CLI**: Interface de linha de comando para automação e scripts.

---

## 🤝 Como Contribuir

O VibeAI é projetado com uma arquitetura modular, permitindo que os componentes funcionem e sejam desenvolvidos de forma independente. Bem-vindos contribuições em qualquer uma das seguintes áreas:

### 📊 Coleta de Dados e Scrapers

Para contribuir com um novo coletor de dados:
1. Navegue até o diretório `/scrapers`.
2. Crie um novo arquivo ou função para sua fonte de dados alvo.
3. Implemente autenticação robusta e tratamento de erros.
4. Garanta que os dados sejam formatados para nosso padrão.
5. Envie um *Pull Request* com uma breve descrição da fonte e tipos de dados.

### 🧠 Lógica de IA e Análise

- Ajude a refinar os modelos NLP para melhor entendimento de consultas.
- Desenvolva novos algoritmos para geração de recomendações e insights.
- Contribua com a lógica de loop de feedback para aprendizado adaptativo.

### 🖥️ Desenvolvimento de UI/UX

- Construa novas interfaces (Web, Desktop, CLI).
- Melhore os fluxos de usuário e componentes de UI existentes.
- Aprimore a visualização de dados para insights de rede.

---

## 🚀 Início Rápido (Configuração Rápida)

> **Pré-requisitos**: Python 3.9+ e `pip` instalados.

1. **Clonar o Repositório**
   bash
   git clone https://github.com/yourusername/vibe_ai.git
   cd vibe_ai
   

2. **Instalar Dependências**
   bash
   pip install -r requirements.txt
   

3. **Configurar Fontes de Dados**
   - Configure suas chaves de API ou credenciais de autenticação em um arquivo `.env`.
   - Siga as instruções na documentação do `/scrapers`.

4. **Executar a Aplicação**
   bash
   # Exemplo para a interface Streamlit
   python -m streamlit run ui/streamlit_app.py
   

---

## 📜 Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.md) para detalhes.