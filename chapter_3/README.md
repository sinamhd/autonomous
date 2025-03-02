# Autonomous
## Chapter 3: Structured Output and Multimodal Data
This chapter demonstrates how to extract structured data from unstructured data using LLMs. We'll build a receipt processing application that extracts key information from receipt images and returns it in a structured format, ready for further processing or database storage. In doing so, we pursue two goals:

1) Learning how to extract structured outputs from unstructured data using Langchain.
2) Understanding how to pass image data to multimodal LLMs using Langchain.

## Overview
In this chapter, you'll see how to:
* **Extract structured data from image data** using LLMs
* **Build an API** that processes uploaded receipt images
* **Create a simple web interface** for your application

The example application works with:
* **Google's Gemini 2.0 Flash** model
* **OpenAI's GPT-4o-mini** model

Please note that the model you select should support both tool calling and multimodal input.
## Project Files
* **`receipt_processor.py`** - Core functionality for extracting structured data from receipt images
* **`api.py`** - FastAPI implementation that exposes the receipt processor as a web service
* **`test_api.py`** - Test script to verify API functionality with a sample receipt
* **`static/`** - Frontend files:
  * `index.html` - Simple web interface for uploading and viewing processed receipts
  * `styles.css` - Styling for the web interface
## Setup Instructions
1. **Clone the Repository (if you haven't already):**
```
git clone https://github.com/sinamhd/autonomous.git
```
If you already cloned the repository from previous chapters, simply navigate to the repository folder and run:
```
git pull origin main
```
2. **Set Up a Virtual Environment:**
  * On macOS/Linux:
```
python -m venv myenv
source myenv/bin/activate
```
   * On Windows:
```
python -m venv myenv
myenv\Scripts\activate
```
3. **Install Dependencies:**
```
pip install -r requirements.txt
```
4. **Configure Your API Keys:**
  * Create a `.env` file in the project root and add your API keys. For example:
```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```
   * For Google's Gemini API key, get your key from Google AI Studio (It has free tier).
   * For OpenAI's API key, sign up at OpenAI's platform.
5. **Prepare Test Images:**
  * Place sample receipt images in the autonomous directory and **update the file paths in the scripts** to point to your test images.
## How to Run
1. **Test the Receipt Processor Directly:**
```
python3 chapter_3/receipt_processor.py
```
You should see the structured receipt data output in your terminal, including merchant information, transaction details, and itemized list.

2. **Start the API Server:**
```
cd chapter_3
uvicorn api:app --reload --port 1234
```
3. **Test the API with a Script:**

Run the following command:

```
python3 chapter_3/test_api.py
```
Ensure that your API correctly processes the request. You should receive a 200 status code in the API terminal and see the results in the terminal where you executed this script.

4. **Access the Web Interface:**
  * Open your browser and navigate to `http://localhost:1234/static/index.html`
  * Upload a receipt image and see the structured data extraction in action

Check out your API's terminal for errors or successful requests.
If you encounter any issues (for example, missing API keys or dependency errors), please double-check your `.env` file and ensure that all dependencies are installed.
## ⭐ Support the Project
If you found this helpful, please give the repository a star! ⭐ Your support inspires me to create more tutorials and content.

