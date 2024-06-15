# FastAPI Multiprocessing Example

This project demonstrates how to set up a FastAPI application with request and response validation using Pydantic models. The application includes an endpoint that performs addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging. The project follows the MVC (Model-View-Controller) structure and includes unit tests for all edge cases and scenarios.

## Project Structure

fastapi_multiprocessing/
│
├── main.py
├── models.py
├── tests/
│ ├── init.py
│ └── test_main.py
└── venv/


- `main.py`: Contains the FastAPI application and the endpoint logic.
- `models.py`: Contains the Pydantic models for request and response validation.
- `tests/`: Contains unit tests for the FastAPI application.

## Setup

1. ***Clone the repository:***

```sh
   git clone <repository-url>
   cd fastapi_multiprocessing
```  

2. ***Set up a virtual environment:***
```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install fastapi uvicorn pydantic pytest
```

3. ***Install the necessary packages:***
```sh
    pip install fastapi uvicorn pydantic pytest
```

4. ***Start the FastAPI application using Uvicorn:***
```sh
    uvicorn main:app --reload
```

5. ***Access the API documentation:***
Open your browser and go to http://127.0.0.1:8000/docs to see the interactive API documentation (Swagger UI).

6. ***Run the tests using pytest:***
```sh
    Run the tests using pytest:
```

7. **API Endpoint**
    ***POST /add***
    Endpoint to add pairs of integers from the request payload. Uses multiprocessing to parallelize the addition of pairs.

    Request Format json
```sh
    {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
```
    Response Format json
```sh
    {
        "batchid": "id0101",
        "response": [3, 7],
        "status": "complete",
        "started_at": "<timestamp>",
        "completed_at": "<timestamp>"
    }
```

8. ***Error Handling***
    If the payload contains invalid data (e.g., non-list item or list with more than or fewer than two integers), the API will return a 422 Unprocessable Entity status with an error message.
    If there is an internal error during processing, the API will return a 400 Bad Request status with an error message.

9. ***logging***
Errors and exceptions are logged using Python's logging module.