import os
from dotenv import load_dotenv
from openai import OpenAI , OpenAIError


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found")
client = OpenAI(
    api_key=api_key
)
print("OpenAI client created successfully")

def ask_ai(mission_description):

    instructions = """
    You are a satellite systems engineer.

    Your task is to create conceptual satellite designs.

    Analyze:
    - Mission type
    - Objective
    - Orbit selection
    - Payload selection
    - Critical subsystems
    - Engineering trade-offs

    Always explain your reasoning.
    """

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=instructions,
            input=mission_description
        )

        if not response.output_text:
            return "Error: AI returned an empty response"

        return response.output_text

    except OpenAIError as e:
        return f"OpenAI API error: {e}"

    except Exception as e:
        return f"Unexpected error: {e}"

def main():

    mission = """
    I need a satellite to monitor agricultural fields
    in Saudi Arabia.
    """

    answer = ask_ai(mission)

    print(answer)


if __name__ == "__main__":
    main()