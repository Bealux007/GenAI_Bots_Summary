import gradio as gr
from utils.query import query_all_bots, determine_best_model
from utils.pdf_generator import generate_summary_pdf

# Predefined queries
queries = [
    "What are the benefits of AI in healthcare?",
    "Explain the concept of machine learning.",
    "What is the future of renewable energy?",
    "How does blockchain technology work?",
    "What are the challenges of remote work?"
]

# AI models available for selection
available_models = ["GPT-4", "GPT-4o", "GPT-4o-mini", "GPT-3.5 Turbo"]

def process_chat(judge_model):
    """Handles chat where one model judges responses from others."""
    if not judge_model:
        return "❌ Please select a judge model.", None

    # ✅ Get responses from all models except the judge
    bot_responses = query_all_bots(queries)

    # ✅ Judge votes and models assign scores
    best_model, vote_results, score_results = determine_best_model(bot_responses, judge_model)

    # ✅ Generate PDF summary
    pdf_filename = "chat_summary.pdf"
    pdf_path = generate_summary_pdf(bot_responses, vote_results, score_results, best_model, pdf_filename)

    if pdf_path:
        return f"✅ Judging completed. Best model: {best_model}", pdf_path
    else:
        return "❌ Error generating PDF.", None

def main():
    with gr.Blocks(title="AI Model Comparison & Judging System") as interface:
        gr.Markdown("# 🏆 AI Model Comparison & Judging System")

        judge_selector = gr.Dropdown(
            choices=available_models,
            label="🔍 Select Judge Model",
            value="GPT-4"
        )

        eval_btn = gr.Button("🏁 Run Evaluation")
        result_text = gr.Textbox(label="📊 Evaluation Result", interactive=False)
        pdf_output = gr.File(label="📂 Download PDF Summary")

        eval_btn.click(
            process_chat,
            inputs=[judge_selector],
            outputs=[result_text, pdf_output]
        )

    interface.launch(share=True)

if __name__ == "__main__":
    main()
