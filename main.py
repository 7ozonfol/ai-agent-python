
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt


def main():
    load_dotenv()
    api_key= os.environ.get("GEMINI_API_KEY")
    if(api_key is None):
        raise RuntimeError("api key not found")
    client = genai.Client(api_key= api_key)

    parser =argparse.ArgumentParser(description = "Chatbot")
    parser.add_argument("user_prompt", type=str, help = "User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    contents = args.user_prompt

    messages = [types.Content(role="user", parts=[types.Part(text = contents)])]

    response = client.models.generate_content(model='gemini-2.5-flash', contents = messages, config = types.GenerateContentConfig(system_instruction=system_prompt))
    if(response.usage_metadata is None):
        raise RuntimeError("metadata not found")
    
    if(args.verbose):
        print("Prompt tokens: "+str(response.usage_metadata.prompt_token_count))
        print("Response tokens: "+str(response.usage_metadata.candidates_token_count))
        print("User prompt: ")
        print(messages)
    print("Response: " + response.text)


if __name__ == "__main__":
    main()
