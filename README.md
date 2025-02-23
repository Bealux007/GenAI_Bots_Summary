📌 Project Overview

The GenAI Bots Summary project is an AI model evaluation system designed to compare responses from multiple AI models, rank their effectiveness, and generate a PDF report summarizing the findings. This system enables users to select a "judge model" that evaluates responses from other models, votes on the best responses and assigns scores accordingly.

This project leverages OpenAI models, Gradio for a user-friendly UI, FPDF for PDF generation, and Pydantic for data handling.

Key Features
✅ Compare responses from GPT-4, GPT-4o, GPT-4o-mini, and GPT-3.5 Turbo.
✅ Automatically rank models based on voting and scoring.
✅ Generate a PDF report summarizing evaluation results.
✅ User-friendly Gradio-based UI for easy interaction.
✅ Dynamic querying with the ability to judge model responses.


📂 Project Structure

The project follows a structured directory format, ensuring modularity and maintainability.

📦 GenAI_Bots_Summary
├── bots/                 # AI model handlers
│   ├── gpt_3_5_turbo.py  # GPT-3.5 Turbo response handler
│   ├── gpt_4.py          # GPT-4 response handler
│   ├── gpt_4o.py         # GPT-4o response handler
│   ├── gpt_4o_mini.py    # GPT-4o-mini response handler
├── utils/                # Helper functions
│   ├── query.py          # AI model querying logic
│   ├── pdf_generator.py  # Generates the PDF report
├── app.py                # Main Gradio application
├── index.py              # Data models (Pydantic)
├── chat_summary.pdf      # Sample evaluation report
├── .env                  # API Keys (Not included in repo)
├── requirements.txt      # Dependencies
└── README.md             # Documentation


🛠 Technologies Used
This project integrates several technologies to ensure a seamless and efficient experience.

Technology	Purpose
Python 🐍	Core programming language
OpenAI API 🤖	AI model querying
Gradio 🎨	Web-based UI for model evaluation
FAISS 🚀	Optimized similarity search for response ranking
FPDF 📄	PDF report generation
Pydantic 📊	Data validation and structured response handling


📂 Detailed File Descriptions
1️⃣ app.py (Main Application)

📌 Purpose:
This is the project's main entry point. It launches a Gradio-based UI where users can select a judge model, evaluate responses, and generate a PDF report.

📌 Key Features:
Loads predefined queries.
Sends queries to all AI models.
It uses a judge model to evaluate, vote, and rank responses.
Generates a PDF report with evaluation summaries.

2️⃣ pdf_generator.py (PDF Report Generator)
📌 Purpose:
Generates a PDF report containing:

Model responses.
Voting results.
Scoring summaries.
📌 Key Features:
✅ Removes encoding issues in responses.
✅ Structures report content logically.
✅ Creates a visually appealing PDF.


3️⃣ query.py (Query Handler & Model Evaluation)
📌 Purpose:

Queries multiple AI models.
It uses a judge model to evaluate responses.
📌 Key Features:
✅ Sends queries to all models.
✅ Judges' responses based on votes & scores.


🚀 How to Run the Project

1️⃣ Clone the Repository
Commands:
git clone https://github.com/Bealux007/GenAI_Bots_Summary.git
cd GenAI_Bots_Summary
2️⃣ Install Dependencies
Commands:
pip install -r requirements.txt
3️⃣ Set Up OpenAI API Key
Commands:
echo "OPENAI_API_KEY=your_api_key_here" > .env
4️⃣ Run the Gradio App
