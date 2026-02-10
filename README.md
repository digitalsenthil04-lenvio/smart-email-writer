Smart Email Writer – GenAI Application

An AI-powered email generation tool built using Streamlit, LangChain, and OpenAI.

This application helps users quickly create well-structured, professional emails based on their requirements like recipient, subject, purpose, and tone.

🚀 Features

Generate complete emails in seconds

Multiple tone options (professional, friendly, request, etc.)

Simple and clean UI

Prompt-based AI generation

Secure API key handling using .env

Error handling for missing inputs

🧠 Tech Stack

Python

Streamlit

LangChain

OpenAI LLM

python-dotenv

📂 Project Structure
smart_email_writer/
│── app.py
│── .env
│── .gitignore
│── README.md

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/smart-email-writer.git
cd smart-email-writer

2️⃣ Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install streamlit langchain langchain-openai python-dotenv

🔐 Setup API Key

Create a file named .env in the root folder.

OPENAI_API_KEY=your_api_key_here


⚠️ Do not share or upload this file to GitHub.

▶️ Run the Application
streamlit run app.py

🖥️ How It Works

User enters recipient, subject, purpose, and tone.

Prompt template formats the request.

LangChain sends it to the OpenAI model.

AI returns a ready-to-send email.

🎯 Example Use Cases

Leave request

Follow-up email

Apology mail

Sales communication

HR communication

🌟 Future Improvements

Copy to clipboard

Download as PDF/DOCX

Email history

Multi-language support

Gmail/Outlook integration

One-click send

👨‍💻 Author

Senthilkumar
Building practical GenAI & SaaS tools for businesses.# smart-email-writer
