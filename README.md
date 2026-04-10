My First API development project using FastAPI. This API allows users to upload images and videos, and also provides endpoints to retrieve the uploaded media. The project is structured to handle different media types and includes error handling for unsupported formats.

Paths:
- GET /posts: Endpoint fetches all the posts.
- POST /upload_post: Endpoint to upload a new post.
- GET /posts/{post_id}: Endpoint to fetch a specific post by its ID.
- GET /posts/search: Endpoint to search for posts based on a query parameter.
- PUT /posts/{post_id}: Endpoint to update an existing post by its ID.
- PATCH /posts/{post_id}: Endpoint to partially update an existing post by its ID.
- DELETE /posts/{post_id}: Endpoint to delete a specific post by its ID.

Used tools and technologies:
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Pydantic: Data validation and settings management using Python type annotations.
- Uvicorn: A lightning-fast ASGI server implementation, using uvloop and httptools.
- Python 3.6+: The programming language used for developing the API.