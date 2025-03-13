# ChatBot

A simple command-line chatbot powered by **OpenAI's GPT-3.5-turbo**. This chatbot interacts with users and generates responses using OpenAI's API.  

## Features  
- Uses **GPT-3.5-turbo** for AI-powered responses.  
- Secure API key handling via **`.env` file**.  
- Simple command-line interface that runs in a loop until exit commands are given.  

## Installation & Setup  

### 1. Download the files from the repository.
### 2. Install Dependencies
Ensure you have Python installed, then install the required packages:
```
pip install openai python-dotenv
```

### 3. Set Up the API Key
Create a .env file in the project directory and add your OpenAI API key:
```
api_key=your-api-key
````
Replace your-api-key with your actual OpenAI API key.

### 4. Run the application
 ```
python chatbot.py
 ```

