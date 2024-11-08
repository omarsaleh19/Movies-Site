# Movies Site Project

A Django-based website for movies.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

## Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/omarsaleh19/Movies-Site
   cd Movies-Site
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   
   # Linux/MacOS
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/MacOS
   source venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install -r movies_site/requirements.txt
   ```

5. **Run the development server**
   ```bash
   python movies_site/manage.py runserver
   ```

6. **Access the website**
   - Main site: http://127.0.0.1:8000

## Features
- Movie reviews
- User authentication
- Admin panel for content management

## Project Structure
```
movies_site/
├── manage.py
├── movies_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movies/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── requirements.txt
```

## Technologies Used
- Django
- Python
- HTML/CSS
- JavaScript

## Contributing
If you'd like to contribute, please:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
