[README.mb.md](https://github.com/user-attachments/files/22953215/README.mb.md)
<!-- Banner (substitua o caminho pelo seu arquivo) -->
<p align="center">
  <img src="assets/banner-totem-ia.png" alt="Totem IA – Educacional" width="100%">
</p>

<h1 align="center">🧠 TOTEM IA – Educacional (FIAP + FlexMidia)</h1>

<p align="center">
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white"></a>
  <a href="#"><img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-protótipo-FF4B4B?logo=streamlit&logoColor=white"></a>
  <a href="#"><img alt="ESP32" src="https://img.shields.io/badge/ESP32-CAM-000000"></a>
  <a href="#"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg"></a>
  <a href="#"><img alt="Status" src="https://img.shields.io/badge/status-Sprint%201-informational"></a>
</p>

<p align="center">
  Solução de <b>IA educacional</b> para escolas públicas e privadas, com totem físico, interação por voz/texto, sensores e análise de dados em nuvem.
</p>

---

## 📌 Sumário
- [Descrição](#-descrição)
- [Objetivos](#-objetivos)
- [Arquitetura Técnica](#-arquitetura-técnica)
- [Instalação & Execução (protótipo)](#-instalação--execução-protótipo)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Cronograma de Sprints](#-cronograma-de-sprints)
- [Parcerias e Aplicações](#-parcerias-e-aplicações)
- [Equipe](#-equipe)
- [Repositório & Evidência de Versionamento](#-repositório--evidência-de-versionamento)
- [Licença](#-licença)

---

## 📖 Descrição
O **Totem IA** é uma solução de **inteligência artificial educacional** para escolas públicas e privadas.  
Promove uma experiência interativa de aprendizado via **totem físico com IA**, sensores (presença/ultrassom, ESP32-CAM) e **coleta de dados anônimos** para insights pedagógicos.

---

## 🎯 Objetivos
- **Geral:** inclusão digital e uso pedagógico de IA no ambiente escolar.  
- **Específicos:**
  - Protótipo com **ESP32-CAM** + sensores.
  - Interface cognitiva em **Python (Streamlit/Gradio)** com voz/texto.
  - **Cloud** para APIs e armazenamento.
  - **Análise de dados** (Python/R) com anonimização.
  - Proposta de **escala** para redes públicas/privadas e parcerias governamentais.

---

## 🧩 Arquitetura Técnica
| Camada | Descrição |
|---|---|
| **Hardware** | Sensores de presença/ultrassom + **ESP32-CAM** para detecção/captura. |
| **Software (Python)** | Protótipo em **Streamlit** ou **Gradio**. |
| **IA & Dados** | Modelos de **voz, imagem, recomendação** (ML/DL). |
| **Cloud** | Coleta, APIs, banco e dashboards. |
| **Segurança** | Autenticação, criptografia em trânsito, anonimização de dados. |

---

## 💻 Instalação & Execução (protótipo)
> Pré-requisitos: Python 3.11+, Git, (opcional) FFmpeg para áudio.

```bash
# 1) Clonar
git clone https://github.com/lnosiqueira/Totem-IA-Educacional.git
cd Totem-IA-Educacional

# 2) Ambiente
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3) Dependências (arquivo será adicionado nas próximas sprints)
pip install -r requirements.txt

# 4) Executar protótipo (ex.: Streamlit)
streamlit run app/app.py

---

Totem-IA-Educacional/
├─ app/                 # Interface (Streamlit/Gradio)
├─ firmware/            # Códigos ESP32-CAM e sensores
├─ cloud/               # Infra, APIs, IaC (ex.: Terraform), diagramas
├─ data/                # Dados simulados para EDA (R/Python)
├─ notebooks/           # Exploração (R e Python)
├─ docs/                # Relatórios, proposta, diagramas
├─ assets/              # Imagens (banner, logos, ícones)
├─ tests/               # Testes
├─ README.md
└─ LICENSE

---

| Sprint | Período          | Mentoria | Pontos | Entregas                           |
| ------ | ---------------- | -------- | ------ | ---------------------------------- |
| **1**  | 16/10 – 31/10/25 | 12/11/25 | 3      | Estrutura base + protótipo inicial |
| **2**  | 13/11 – 28/11/25 | 10/12/25 | 9      | Integração HW/SW + APIs            |
| **3**  | 10/02 – 06/03/26 | 18/03/26 | 9      | Modelos de IA + Cloud              |
| **4**  | 20/03 – 17/04/26 | 29/04/26 | 9      | Otimização, testes, apresentação   |

---

🤝 Parcerias e Aplicações

FIAP + FlexMidia
Projetado para Secretarias de Educação, redes públicas/privadas e empresas de tecnologia, visando expansão em escala com indicadores de engajamento e impacto educacional.

---

👥 Equipe

Integrantes: Leno Siqueira
Integrantes: 

Orientador: André Godoi
Parceria: FIAP + FlexMidia

---

🔗 Repositório & Evidência de Versionamento

Este repositório consolida código, protótipos, diagramas e relatórios do projeto.
Commits e PRs documentam a colaboração entre os integrantes.

---

🧾 Licença

Projeto acadêmico sob MIT License.
© 2025 FIAP + FlexMidia.
