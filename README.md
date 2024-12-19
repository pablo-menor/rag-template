# Project Setup Guide

This document explains how to set up the development environment for this project.

It is meant to be used with Cohere's models since a free acocunt can be used for it.
Feel free to adapt the code in order to use models from other providers.

## Setup Steps

### 1. Create Virtual Environment

First, create a virtual environment to isolate project dependencies:
```
python -m venv venv
```
### 2. Activate Virtual Environment

Activate the virtual environment:

#### On Windows:
```
venv\Scripts\activate
```
#### On macOS and Linux:
```
source venv/bin/activate
```

### 3. Install Dependencies

With the virtual environment activated, install project dependencies:

```
pip install -r requirements.txt
```

### 4. Add your documents

Inside the /docs folder, drop your own PDFs that will be used to answer your questions.

### 5. Set environment variables

Create a .env file with the following environment variable: `COHERE_SECRET=<your secret API key>`

### Launch streamli app locally

Run the following command:
```
streamlit run app.py
```

## Streamlit Community Cloud deployment
1. Install the following library: pysqlite3-binary.
2. In app.py uncomment the 3 first lines.

