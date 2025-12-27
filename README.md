# VibeAI 🌐

<div align="center">

[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)
[![Status](https://img.shields.io/badge/status-prototype-orange.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](https://github.com/yourusername/vibe_ai)

> *Developed for the AGIHouseSF Hackathon* 🏆

</div>

---

## 📋 Overview

**VibeAI** is an intelligent relationship intelligence platform that consolidates and analyzes your social network data into a secure, local database. By leveraging advanced AI, it transforms scattered contact information into a powerful tool for professional networking, strategic introductions, and actionable insights.

### ✨ Key Capabilities

<table>
  <tr>
    <td width="50%" align="center"><b>🔍 Intelligent Queries</b></td>
    <td width="50%" align="center"><b>🤝 Strategic Recommendations</b></td>
  </tr>
  <tr>
    <td>
      <ul>
        <li>"Who in my network is investing in early-stage AI companies?"</li>
        <li>"Identify contacts who have recently left their roles in the last 3 months"</li>
        <li>"Find connections at Google with expertise in machine learning"</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>"Your friend Jim is exploring new ventures; your contact Helen invests in founders. Suggest an introduction with their contact details."</li>
        <li>"Alex needs a UX designer; your network contact Taylor is actively seeking new opportunities."</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🏗️ Architecture

VibeAI is built on a modular, extensible architecture designed for privacy and flexibility.

<div align="center">

mermaid
graph TD
    A[Data Sources] -->|Ingestion| B[Local Database]
    B -->|Structured Data| C[AI Analysis Layer]
    C -->|Insights & Recs| D[User Interface]
    D -->|User Queries| C
    C -.->|Context| D


</div>

### 1. 📥 Data Ingestion Layer

| Source | Data Type | Status |
|--------|-----------|--------|
| LinkedIn | Profiles, Connections, Messages | ⏳ In Progress |
| Messenger | Chat History & Context | 🔜 Planned |
| Email | Contacts & Correspondence | 🔜 Planned |
| Twitter/X | Public Posts & Interactions | 🔜 Planned |

*Goal: Provide a flexible ingestion framework to easily integrate new data sources via custom collectors.*

### 2. 💾 Local Database

- **Core Function**: Securely stores people, network data, and interaction history.
- **Technology**: Powered by ChromaDB for efficient vector storage and semantic search.
- **Privacy-First**: All data remains on your local machine.

### 3. 🧠 AI Analysis Layer

- **Insight Generation**: Analyzes your network to surface valuable opportunities and connections.
- **NLP Engine**: Understands complex queries and relationship contexts.
- **Adaptive Learning**: Refines recommendations based on user interactions and feedback.

### 4. 🖥️ Interface Options

- 🖱️ **Desktop App**: Native experience for power users.
- 🌐 **Streamlit UI**: Rapid, web-based interface for quick access.
- ⚛️ **React Web App**: Modern, full-featured web client.
- 📟 **CLI**: Command-line interface for automation and scripting.

---

## 🤝 How to Contribute

VibeAI is designed with a modular architecture, allowing components to function and be developed independently. We welcome contributions in any of the following areas:

### 📊 Data Collection & Scrapers

To contribute a new data collector:
1. Navigate to the `/scrapers` directory.
2. Create a new file or function for your target data source.
3. Implement robust authentication and error handling.
4. Ensure data is formatted for our standard schema.
5. Submit a Pull Request with a brief description of the source and data types.

### 🧠 AI & Analysis Logic

- Help refine the NLP models for better query understanding.
- Develop new algorithms for recommendation and insight generation.
- Contribute to the feedback loop logic for adaptive learning.

### 🖥️ UI/UX Development

- Build new interfaces (Web, Desktop, CLI).
- Improve existing UI components and user flows.
- Enhance data visualization for network insights.

---

## 🚀 Getting Started (Quick Setup)

> **Prerequisites**: Python 3.9+ and `pip` installed.

1. **Clone the Repository**
   bash
   git clone https://github.com/yourusername/vibe_ai.git
   cd vibe_ai
   

2. **Install Dependencies**
   bash
   pip install -r requirements.txt
   

3. **Configure Data Sources**
   - Set up your API keys or authentication credentials in a `.env` file.
   - Follow the instructions in the `/scrapers` documentation.

4. **Run the Application**
   bash
   # Example for the Streamlit interface
   python -m streamlit run ui/streamlit_app.py
   

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.