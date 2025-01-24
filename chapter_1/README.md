# Autonomous
## Chapter 1 — Basics: Function Calling with OpenAI Models

This chapter introduces how to use function calling to extend the capabilities of large language models (LLMs). By integrating Python functions and external APIs, you can enable LLMs to dynamically generate arguments based on user queries, perform tasks, and handle workflows autonomously.

---

### Overview

LLMs are powerful, but their capabilities are limited without access to external tools. Function calling enables models to execute tasks like writing and running code, data retrieval, and integration with APIs. In this chapter, we demonstrate how to:
- Show the limitations of LLMs without external tools.
- Use function calling (tools) to enhance their accuracy and flexibility.

This tutorial uses **gpt-4o-mini**, a cost-effective model sufficient for demonstrating these concepts. For pricing details, visit [OpenAI Pricing](https://openai.com/api/pricing/).

In the next chapter, we will explore one of the Meta Llama models, an open-source model that can be run locally on your laptop for free.

---

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sinamhd/autonomous.git
   cd autonomous
   ```
2. Set Up a Virtual Environment:

On macOS/Linux:
```bash
python -m venv myenv
source myenv/bin/activate
```
On Windows:
```bash
python -m venv myenv
myenv\Scripts\activate
```
3. Install Dependencies:

```bash
pip install -r requirements.txt
```

4. Obtain an OpenAI API Key:

Go to the OpenAI Developer Platform and generate an API key.
Create a .env file in the autonomous folder and add:
```
OPENAI_API_KEY=your_openai_api_key
```

### How to Run

1. This script demonstrates how LLMs behave when handling user queries without external tools (e.g., incorrect multiplication calculation).
```bash
python3 chapter_1/openai_basic_call.py
```
2. Run Function Calling Example: This script shows how function calling enhances the accuracy of LLM responses by utilizing external tools.

```bash
python3 chapter_1/openai_function_call.py
```
If you encounter any issues (e.g., API key errors), double-check your .env file and ensure all dependencies are installed.


### ⭐ Support the Project
If you found this helpful, please give the repository a star! ⭐ Your support inspires me to create more tutorials and content.