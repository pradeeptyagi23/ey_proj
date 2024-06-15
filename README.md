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

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd fastapi_multiprocessing

2. **Set up a virtual environment:**
