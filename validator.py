from llm_functions import run_ai_model_full
from jinja2 import Template

async def validate_listing(listing):
    response_format = {
        "valid": "true/false depending on validity (it should be boolean type not string)",
        "reason": "string explaining why the listing is invalid or empty if valid",
        "valid_elements": "string listing the valid elements of the listing or empty if none",
        "invalid_elements": "string listing the invalid elements of the listing or empty if none",
        "missing_elements": "string listing the missing elements of the listing or empty if none",
        "suggestions": "string with suggestions for improvement or empty if valid"
    }
    
    with open("validation_prompt.txt", "r",encoding="utf-8") as file:
        prompt_template = Template(file.read())

    system_prompt = prompt_template.render(response_format=response_format)

    user_prompt = f'''
    Please validate the following listing for compliance with FCA regulations and provide suggestions for improvement if necessary.
    {listing}
    '''
    response = await run_ai_model_full(system_prompt, user_prompt)
    return response