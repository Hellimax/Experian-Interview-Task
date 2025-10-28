import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL")
client = genai.Client(api_key=api_key)

async def stream_gemini_response(system_prompt,user_prompt):
    """Return an async generator from the SDK; caller will consume fully."""
    return await client.aio.models.generate_content_stream(
        model=model_name,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.5,
            seed=42,
        ),
        contents=user_prompt,
    )

async def run_ai_model_full(system_prompt, user_prompt):
    """
    This function runs the AI model and returns a parsed JSON object (dict/list).
    """
    try:
        
        response = await client.aio.models.generate_content(
            model=model_name, 
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.5,
                seed=42,
                response_mime_type="application/json",
            ),
            contents=user_prompt
        )
        
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()
        
        # Return parsed JSON object
        return json.loads(response_text)
        
    except Exception as e:
        print(f"Error in run_ai_model: {e}")
        return None

