# AI Data Support Agent (Excel + Gemini)

An AI-powered Excel analysis assistant that enables users to query structured data in natural language.

This project demonstrates how Large Language Models (LLMs) can act as intelligent copilots for structured data analysis.

---

## 🚀 Problem

Business users frequently work in Excel but lack advanced data analysis skills. 

Extracting insights typically requires:
- Writing formulas
- Creating pivot tables
- Using Python or SQL
- Or asking a data team

This creates friction and slows decision-making.

---

## 💡 Solution

This application allows users to:

1. Upload a Microsoft Excel file (.xlsx)
2. Automatically generate a dataset summary
3. Ask natural-language questions about the data
4. Receive AI-generated analysis and explanations

Example questions:
- “Which column appears most correlated with revenue?”
- “What trends do you see in monthly sales?”
- “Which category has the highest average profit?”

The app uses Google Gemini to interpret structured data and provide analytical responses.

### Technologies Used

- **Python** – Core application logic
- **Streamlit** – Lightweight web UI framework
- **pandas** – Data processing and Excel handling
- **openpyxl** – Excel file engine
- **Google Gemini API** – LLM reasoning engine
- **python-dotenv** – Secure API key management

---

## ⚙️ How It Works

1. User uploads an Excel file
2. pandas reads and summarizes the dataset
3. A snippet of the dataset is passed to Gemini
4. Gemini generates a structured analytical response
5. The result is displayed in the UI
