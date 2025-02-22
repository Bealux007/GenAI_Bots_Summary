from fpdf import FPDF
import os

def clean_text(text):
    """Removes unsupported characters to prevent encoding errors."""
    return text.encode("latin-1", "ignore").decode("utf-8")

def generate_summary_pdf(bot_responses, vote_results, score_results, best_model, filename="chat_summary.pdf"):
    """Generates a PDF summary of responses, votes, and scores."""

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    try:
        pdf.set_font("Arial", "", 12)
    except:
        pdf.set_font("Courier", "", 12)  # Fallback if Arial fails

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(200, 10, "AI Model Evaluation Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Helvetica", "", 12)

    # ✅ Ensure we have responses
    if not bot_responses:
        pdf.cell(200, 10, "No responses were recorded.", ln=True)
    else:
        for query, responses in bot_responses.items():
            pdf.cell(200, 10, clean_text(f"Query: {query}"), ln=True)
            pdf.ln(5)

            for model, response in responses.items():
                safe_response = clean_text(response)
                pdf.multi_cell(0, 10, f"{model}: {safe_response}")
                pdf.ln(5)

            pdf.cell(0, 10, "", ln=True)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(200, 10, "Voting Results", ln=True)
    pdf.ln(5)

    # ✅ Ensure vote results exist
    if not vote_results:
        pdf.cell(200, 10, "No votes recorded.", ln=True)
    else:
        for model, votes in vote_results.items():
            pdf.cell(200, 10, f"{model}: {votes} votes", ln=True)
            pdf.ln(5)

    pdf.cell(0, 10, "", ln=True)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(200, 10, "Scoring Results", ln=True)
    pdf.ln(5)

    if not score_results:
        pdf.cell(200, 10, "No scores recorded.", ln=True)
    else:
        for model, score in score_results.items():
            pdf.cell(200, 10, f"{model}: {score} total score", ln=True)
            pdf.ln(5)

    # ✅ Display best model if available
    if best_model and best_model != "No clear winner":
        pdf.cell(200, 10, f"🏆 Best Model: {best_model}", ln=True, align="C")
    else:
        pdf.cell(200, 10, "No best model determined.", ln=True, align="C")

    pdf.ln(10)

    # ✅ Ensure the directory exists before saving
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, filename)

    try:
        pdf.output(file_path, "F")  # ✅ Ensure file mode "F" to force save
        print(f"✅ PDF successfully saved at: {file_path}")
        return file_path
    except Exception as e:
        print(f"❌ Error saving PDF: {e}")
        return None
