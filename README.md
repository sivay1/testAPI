# testAPI

## Overview

This is a Django Rest Framework (DRF) project that provides an API for managing books. It includes endpoints for creating, reading, updating, deleting and users can add reviews to book entries.

## Features

- **Create:** Add new books to the database.
- **Read:** Retrieve information about books.
- **Update:** Modify existing book entries.
- **Delete:** Remove books & marking active status as false.

## Getting Started

### Prerequisites

- Python
- Django
- Django Rest Framework

### Installation

1. Clone the repository:
     git clone https://github.com/sivay1/testAPI.git
2. Navigate to the project directory:
     cd testAPI
3. Install dependencies:
     pip install -r requirements.txt
4. Apply database migrations:
     python manage.py migrate
5. Run the development server:
     python manage.py runserver
### API Endpoints
- Create new author:
POST :http://127.0.0.1:8000/api/author
- Create a new book:
POST :http://127.0.0.1:8000/api/book/
- Retrieve all books:
GET :http://127.0.0.1:8000/api/view-books/
- Retrieve details of a specific book:
GET :http://127.0.0.1:8000/api/book/{book_id}/
- Update a book:
PUT :http://127.0.0.1:8000/api/update-book/{book_id}
- Delete a book:
DELETE :http://127.0.0.1:8000/api/delete-book/{book_id}
- Add review :http://127.0.0.1:8000/api/reviews
  
