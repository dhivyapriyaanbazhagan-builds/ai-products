# helpers.py
import pandas as pd
import os
from dotenv import load_dotenv

# Google GenAI client
from google import genai

load_dotenv()

def summarize_df(df: pd.DataFrame, n_top=5):
  summary = {
   "rows": int(df.shape[0]),
   "columns": int(df.shape[1]),
   "dtypes": df.dtypes.astype(str).to_dict(),
   "missing_values": df.isnull().sum().to_dict(),
   "top_values": {}
  }
  for col in df.columns:
   try:
    top = df[col].value_counts(dropna=False).head(n_top).to_dict()
   except Exception:
    top = {}
   summary["top_values"][col] = top
  return summary

def df_to_snippet(df: pd.DataFrame, max_rows: int = 50):
 # Make a small CSV-like snippet for model context
 small = df.head(max_rows).copy()
 return small.to_csv(index=False)

def build_prompt(snippet: str, user_question: str):
 prompt = f"""
You are a senior data analyst. Use the dataset snippet (CSV-format) below to answer the user's question thoroughly.
- Show concise computations (counts, means) where useful.
- Suggest short pandas code snippets if helpful.
- If something is ambiguous, say what additional info you'd need.

Dataset snippet (first rows):
{snippet}

User question:
{user_question}

Answer:
"""
 return prompt

def ask_model(df: pd.DataFrame, user_question: str, api_key: str = None, model_name: str = "gemini-3-flash-preview"):
 """
 Sends a prompt + snippet to Gemini via the google-genai client.
 Returns model text or an error message.
 """
 if api_key is None:
  api_key = os.getenv("GEMINI_API_KEY")

 if not api_key:
  return "No GEMINI_API_KEY set. Put your key in the .env file or set the GEMINI_API_KEY environment variable."

 # initialize client (client reads GEMINI_API_KEY from env automatically if not passed)
 client = genai.Client(api_key=api_key)

 snippet = df_to_snippet(df, max_rows=100)
 prompt = build_prompt(snippet, user_question)

 try:
    # The quickstart uses models.generate_content (contents can be a string)
    response = client.models.generate_content(
    model=model_name,
    contents=prompt,
    )
    # response.text contains the flattened generated text in many examples
    text = getattr(response, "text", None)
    if text:
     return text
    # fallback to checking Candidates or other shapes
    try:
     return response.candidates[0].content[0].text
    except Exception:
     return str(response)
 except Exception as e:
  return f"Error calling Gemini API: {e}"