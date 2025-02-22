import os
from openai import OpenAI
from bots import gpt_4, gpt_4o, gpt_4o_mini, gpt_3_5_turbo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define AI models
models = {
    "GPT-4": gpt_4.generate_response,
    "GPT-4o": gpt_4o.generate_response,
    "GPT-4o-mini": gpt_4o_mini.generate_response,
    "GPT-3.5 Turbo": gpt_3_5_turbo.generate_response
}

def query(user_input, model_name):
    """Queries a model with user input."""
    return models[model_name](user_input)

def query_all_bots(queries):
    """Queries all bots with predefined queries and collects their responses."""
    responses = {}
    for query_text in queries:
        responses[query_text] = {}
        for model_name, model_func in models.items():
            responses[query_text][model_name] = model_func(query_text)
    return responses

def determine_best_model(bot_responses, judge_model):
    """
    Each AI model (except itself) selects the best response and scores others.
    The model with the highest votes is selected as the best.
    """

    # ✅ Initialize vote count and score dictionary
    vote_counts = {bot: 0 for bot in bot_responses[next(iter(bot_responses))]}
    score_totals = {bot: 0 for bot in bot_responses[next(iter(bot_responses))]}
    
    for query_text, responses in bot_responses.items():
        for voter_model in vote_counts.keys():  
            if voter_model == judge_model:
                continue  # The judge votes separately

            # ✅ Construct voting prompt
            voting_prompt = f"Evaluate the responses for the question: '{query_text}'.\n"
            voting_prompt += "Pick the best response (excluding yourself) and assign scores (1-10) to others:\n"

            available_choices = {m: r for m, r in responses.items() if m != voter_model}

            if not available_choices:
                continue  # Skip if no valid choices to vote

            try:
                # ✅ Get the model's selected best response
                best_choice = query(voting_prompt, voter_model).strip()

                # ✅ Ensure the vote is counted correctly
                if best_choice in vote_counts and best_choice != voter_model:
                    vote_counts[best_choice] += 1

                # ✅ Get scores for all models except itself
                score_prompt = f"Rate each response (except yours) on a scale of 1-10 for the question: '{query_text}'.\n"
                score_prompt += "Provide scores in this format: Model: Score\n"

                score_response = query(score_prompt, voter_model).strip().split("\n")
                
                for line in score_response:
                    try:
                        model, score = line.split(":")
                        model, score = model.strip(), int(score.strip())
                        if model in score_totals and model != voter_model:
                            score_totals[model] += score
                    except:
                        continue  # Ignore invalid responses

            except Exception as e:
                print(f"⚠️ Error during voting by {voter_model}: {e}")

    # ✅ Judge Model Votes Separately
    judge_prompt = f"Judge, select the best response for the question: '{query_text}'.\n"
    judge_prompt += "Pick the best response:\n"

    for model_name, response in responses.items():
        judge_prompt += f"\n{model_name}: {response}"

    try:
        judge_vote = query(judge_prompt, judge_model).strip()
        if judge_vote in vote_counts and judge_vote != judge_model:
            vote_counts[judge_vote] += 1
    except Exception as e:
        print(f"⚠️ Error during judging by {judge_model}: {e}")

    # ✅ Determine the best model based on highest votes and scores
    highest_votes = max(vote_counts.values(), default=0)
    highest_score = max(score_totals.values(), default=0)

    best_model = "No clear winner"
    if highest_votes > 0:
        best_model = max(vote_counts, key=vote_counts.get)

    return best_model, vote_counts, score_totals
