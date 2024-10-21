# Flask Starter Template

A lightweight Flask template that includes essential libraries and tools for rapid development. This template integrates:

- **Flask**: Web framework for building scalable applications.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Faker**: A library for generating fake data for testing.
- **dotenv**: For managing environment variables.
- **Bootstrap**: Responsive front-end framework for easy UI design.
- **Alpine.js**: Minimal JavaScript framework for adding interactivity to your app.

## Features

- **Flask App Structure**: Organized with Blueprints and modular components.
- **Data Validation**: Pydantic for type-safe and validated data models.
- **Environment Management**: `dotenv` for seamless handling of environment variables.
- **UI Styling**: Bootstrap for responsive and customizable front-end design.
- **Lightweight JS**: Alpine.js for reactive functionality with minimal overhead.
- **Mock Data**: Faker integrated for generating mock data during development.

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd your-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory for your environment variables:

```bash
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

4. Run the app:

```bash
flask run
```

# Usage
- Use Pydantic for defining and validating data models in your app.
- Generate mock data during development using Faker.
- Style your app with Bootstrap and add interactivity using Alpine.js.

# Project Structure

```bash
/app
   /blueprints
   /static
       /css
           custom.css
       /js
           ...
   /templates
       base.html
       index.html
.env
requirements.txt
app.py
README.md
requiremetns.txt
```

