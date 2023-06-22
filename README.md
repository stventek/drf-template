# drf-template

This is a template project built with Django Rest Framework (DRF) that can be used as a starting point for new projects.

## Features

- **Automatic Filtering:** A single filter class can be used for all views.
- **Swagger Configuration:** Interactive API documentation powered by Swagger.
- **Pagination Configuration:** Configure pagination settings for your API.
- **Token Authentication with Knox:** Token-based authentication using the Knox library good for SPA.
- **OAuth2 Integration:** Support for OAuth2 authentication.
- **Social Authentication:** Enable social authentication options such as Google, Facebook, etc.
- **Automatic Permission Classes:** Automatically assign permission classes to new and custom views.

## Pending features

- **Email Verification:** Verify user email addresses during registration.
- **Password Recovery:** Allow users to recover their passwords.
- **Soft Deletion:** Implement soft deletion for models, allowing for easy recovery of deleted items.

## Installation and Setup

1. Clone the repository:

```
git clone <repository_url>
```

2. Create a virtual environment and activate it:

```
virtualenv env
source env/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Configure the project settings:

- Rename the `.env.example` file to `.env` and update the settings accordingly.

5. Apply database migrations:

```
python manage.py migrate
```

6. Start the development server:

```
python manage.py runserver
```

7. Access the API documentation at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).


## License

This project is licensed under the [MIT License](LICENSE).
