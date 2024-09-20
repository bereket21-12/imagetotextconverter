# FastAPI OCR Project

This project is a FastAPI application that accepts PDF and image files (JPG, PNG), extracts text using OCR tools like Tesseract, and returns the extracted data in JSON format.

## Features

- Upload PDF or image files
- Extract text using Tesseract OCR
- Return extracted text in JSON format

---

## Table of Contents

- [FastAPI OCR Project](#fastapi-ocr-project)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Installation Locally](#installation-locally)
    - [Installation Using Docker](#installation-using-docker)

---

## Installation

### Installation Locally

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bereket21-12/imagetotextconverter
   cd your_repository
2. **Create a Virtual environment**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   pip install -r requirements.txt
4. **Run the application**
   uvicorn app.main:app --reload

### Installation Using Docker

1. **docker build -t your_image_name.**
   docker build -t your_image_name

2. **Run the Docker Container.**
   docker run -d -p 8000:8000 your_image_name

- The app will be accessible at http://127.0.0.1:8000.