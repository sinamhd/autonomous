# Autonomous
## Chapter 2 — Basics: LangChain Integration for Function Calling

This chapter demonstrates how to use LangChain to integrate with different LLM providers in a straightforward way. In Chapter 1, we used direct API calls to interact with OpenAI's API. Here, we use LangChain to bind custom tools to various models and handle function calling uniformly across different APIs.

---

### Overview

In this chapter, you'll see examples of how to use LangChain with:

- **OpenAI**  
  - `langchain_openai_basic.py` and `langchain_openai_tools.py`  
  *Note: These two OpenAI integration examples are the exact LangChain reproductions of the corresponding files from Chapter 1 (`chapter_1/openai_basic_call.py` and `chapter_1/openai_function_call.py`), where we used direct API calls.*
- **Meta Llama (via Ollama)** (`langchain_llama_tools.py`)
- **Google's Gemini API** (`langchain_gemini_tools.py`)
- **Anthropic's Claude API** (`langchain_anthropic_tools.py`)

**Note**: As of the writing of this tutorial, the deepseek models are not included in these examples because their current Function Calling capability is unstable, which may result in looped calls or empty responses. Deepseek is actively working on a fix, which is expected to be resolved in the next version.


---
### Setup Instructions

1. **Clone the Repository (if you haven't already):**
   ```bash
   git clone https://github.com/sinamhd/autonomous.git
   ```
   If you already cloned the repository from Chapter 1, simply navigate to the repository folder and run:
   ```bash
   git pull origin main
   ```

2. **Set Up a Virtual Environment:**

   - On macOS/Linux:
     ```bash
     python -m venv myenv
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv myenv
     myenv\Scripts\activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Your API Keys:**

   - Create a `.env` file in the project root and add your API keys. For example:
     ```
     OPENAI_API_KEY=your_openai_api_key
     GOOGLE_API_KEY=your_google_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```
   - For Anthropic's API key, refer to the [Anthropic API Key](https://console.anthropic.com/settings/keys).
   - For Google's Gemini API key, get your key from [Google AI Studio](https://aistudio.google.com/apikey). Gemini 2.0 Flash has a free tier with usage limits—please check online for the latest pricing details.

5. **Install Ollama for Meta Llama:**

   - Download and install Ollama from [Ollama Download](https://ollama.com/download). Follow the instructions for your operating system.
   - Once Ollama is installed, you can download an open-source model using:
     ```bash
     ollama pull {model_name}
     ```
   - Browse available models and their details (such as size and tool calling support) at [Ollama Search](https://ollama.com/search).
   - In this tutorial, we use `llama3.1:latest 8b`, which is about 4.9 GB. Note that this model is Q4_K_M (4-bit quantized), so some quality loss is expected compared to higher-precision models. If you need a larger, higher-precision Llama model, you'll either need to have at least a few GPUs or use an API provider such as `together.ai` and pay fees similar to those for providers like OpenAI and Anthropic.

---

### How to Run

This chapter includes several scripts demonstrating LangChain integration with different providers. Run the desired script:

1. **Basic OpenAI Integration via LangChain:**
   ```bash
   python3 chapter_2/langchain_openai_basic.py
   ```

2. **Function Calling with OpenAI via Langchain:**
   ```bash
   python3 chapter_2/langchain_openai_tools.py
   ```

3. **Function Calling with Meta Llama via Langchain and Ollama:**
   ```bash
   python3 chapter_2/langchain_llama_tools.py
   ```

4. **Function Calling with Google's Gemini API via Langchain:**
   ```bash
   python3 chapter_2/langchain_gemini_tools.py
   ```

5. **Function Calling with Anthropic's Claude API via Langchain:**
   ```bash
   python3 chapter_2/langchain_anthropic_tools.py
   ```

If you encounter any issues (for example, missing API keys or dependency errors), please double-check your `.env` file and ensure that all dependencies are installed.

---

### ⭐ Support the Project

If you found this helpful, please give the repository a star! ⭐ Your support inspires me to create more tutorials and content.

