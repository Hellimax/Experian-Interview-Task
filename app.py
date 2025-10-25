from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from validator import validate_listing
import asyncio
import json
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Listing Validator API", version="1.0.0")


class ListingRequest(BaseModel):
    text: str


class ListingResponse(BaseModel):
    valid: bool
    suggestions: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
def read_root():
    # Simple landing page with a link to the Swagger UI docs
    return (
        """
        <html>
            <h1>Listing Validator API</h1>
            <p>This is the <a href="/docs">Docs</a> link</p>
        </html>
        """
    )


@app.post("/validate-listing", response_model=ListingResponse)
async def run_validate_listing(input_txt: ListingRequest) -> ListingResponse:
    logger.info(f"Received request to validate listing...")
    result_path = "listing_results_latest.json"
    text = input_txt.text or ""
    response = await validate_listing(text)
    if os.path.exists(result_path):
        with open(result_path, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append({"listing": text, "validation_result": response})
    with open(result_path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Validation completed.")
    return ListingResponse(**response)


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000)
