# main.py
from fastapi import FastAPI, HTTPException, Request
from multiprocessing import Pool
from models import AdditionRequest, AdditionResponse
from datetime import datetime
import logging
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(pair):
    """
    Function to add two integers in a list.
    Validates that the pair is a list of exactly two integers.
    """
    if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(i, int) for i in pair):
        raise ValueError("Each item in payload should be a list of two integers.")
    return sum(pair)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Custom exception handler for request validation errors.
    Returns a 422 Unprocessable Entity status with the error details.
    """
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

@app.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    """
    Endpoint to add pairs of integers from the request payload.
    Uses multiprocessing to parallelize the addition of pairs.
    """
    started_at = datetime.utcnow()  # Record start time

    try:
        # Use multiprocessing pool to add pairs in parallel
        with Pool() as pool:
            result = pool.map(add, request.payload)
    except Exception as e:
        logger.error(f"Error processing request: {e}")  # Log error
        raise HTTPException(status_code=400, detail=str(e))

    completed_at = datetime.utcnow()  # Record completion time

    # Create response model instance
    response = AdditionResponse(
        batchid=request.batchid,
        response=result,
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )

    return response
