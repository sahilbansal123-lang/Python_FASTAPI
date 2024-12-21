# FastAPI CRUD Application

A simple CRUD (Create, Read, Update, Delete) application built using [FastAPI](https://fastapi.tiangolo.com/), SQLAlchemy, and a SQLite database. This application demonstrates basic API functionality for managing blog posts.

## Features

- Create a new blog post
- Read all blog posts or a single blog post by ID
- Update an existing blog post
- Delete a blog post by ID
- Password hashing using `bcrypt`
- User authentication using JWT tokens

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.9+
- `pip` (Python package manager)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-crud-app.git
   cd fastapi-crud-app
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API documentation:**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```
fastapi-crud-app/
├── main.py             # Entry point for the application
├── models.py           # SQLAlchemy models for database tables
├── schema.py           # Pydantic models for request/response validation
├── database.py         # Database connection and setup
├── Hashing.py          # Utility for password hashing
├── auth.py             # JWT authentication utilities
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## API Endpoints

### Create a Blog

**POST** `/blog`

- **Request Body:**
  ```json
  {
    "title": "Sample Blog Title",
    "body": "This is the content of the blog post."
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Sample Blog Title",
    "body": "This is the content of the blog post."
  }
  ```

### Get All Blogs

**GET** `/blog`

- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Sample Blog Title",
      "body": "This is the content of the blog post."
    }
  ]
  ```

### Get a Blog by ID

**GET** `/blog/{id}`

- **Response:**
  ```json
  {
    "id": 1,
    "title": "Sample Blog Title",
    "body": "This is the content of the blog post."
  }
  ```

### Update a Blog

**PUT** `/blog/{id}`

- **Request Body:**
  ```json
  {
    "title": "Updated Blog Title",
    "body": "Updated content of the blog post."
  }
  ```
- **Response:**
  ```json
  {
    "detail": "Updated successfully"
  }
  ```

### Delete a Blog

**DELETE** `/blog/{id}`

- **Response:**
  ```json
  {
    "detail": "Blog with id {id} deleted successfully"
  }
  ```

### Authenticate User

**POST** `/login`

- **Request Body:**
  ```json
  {
    "username": "user1",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "<JWT token>",
    "token_type": "bearer"
  }
  ```

## Technologies Used

- **FastAPI:** Framework for building APIs.
- **SQLAlchemy:** ORM for database interactions.
- **SQLite:** Lightweight database for development.
- **Uvicorn:** ASGI server for running the FastAPI app.
- **bcrypt:** Library for secure password hashing.
- **JWT:** Token-based authentication.

## Future Improvements

- Extend to support other database backends like PostgreSQL or MySQL.
- Implement role-based access control (RBAC).
- Add unit tests for API endpoints.
- Add rate limiting for enhanced security.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Acknowledgements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Passlib Documentation](https://passlib.readthedocs.io/)
- [JWT Documentation](https://jwt.io/)

