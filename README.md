# WEEK 8 – LOCAL LLM INFERENCE

## Project Title
Running Large Language Models Locally Using Ollama

## 1. Introduction

Large Language Models (LLMs) are AI systems that can understand prompts and generate text. Ollama allows users to run supported LLMs locally on their computers.

This project uses Ollama and Python to generate responses for prompts from different domains. The responses are saved in CSV files and compared to understand the performance of different local language models.

## 2. Objectives

- To understand local LLM inference.
- To install and configure Ollama.
- To interact with local LLMs using Python.
- To generate responses for ten prompts.
- To compare responses from different models.
- To save conversations for future chatbot development.

## 3. Technologies Used

- Python
- Ollama
- Llama 3.2
- Gemma 2B
- Pandas
- Jupyter Notebook
- Visual Studio Code

## 4. Software Requirements

- Windows operating system
- Python
- Ollama
- Visual Studio Code
- Jupyter Notebook
- Sufficient RAM and storage for the selected models

## 5. Installation

Install Ollama and verify the installation using:

```bash
ollama --version
ollama list
```

Install the required Python packages:

```bash
python -m pip install ollama pandas notebook ipykernel
```

## 6. Downloading Models

Download Llama 3.2:

```bash
ollama pull llama3.2
```

Download Gemma 2B:

```bash
ollama pull gemma2:2b
```

Check the installed models:

```bash
ollama list
```

## 7. Project Execution

Open the project folder in Visual Studio Code.

Run the Python program:

```bash
python local_llm.py
```

The program reads prompts from the dataset, generates responses using Ollama, and saves the results.

Open the Jupyter Notebook to view the practical steps, generated outputs, and model analysis.

## 8. Dataset Description

### prompts.csv
Contains ten prompts from education, healthcare, coding, travel, business, environment, technology, science, problem solving, and creative writing.

### llm_responses.csv
Stores prompts, generated responses, model names, response word counts, and execution status.

### response_comparison.csv
Stores responses from Llama 3.2 and Gemma 2B for comparison.

### conversation_history.txt
Stores the prompts and generated responses in readable text format.

## 9. Model Comparison

Llama 3.2 and Gemma 2B are evaluated using the same prompts.

The evaluation considers response quality, relevance, word count, and accuracy. Accuracy is checked against suitable reference information.

The final comparison is based on the actual responses generated during project execution.

## 10. Conclusion

This project demonstrates how to run Large Language Models locally using Ollama and Python. It covers prompt processing, response generation, CSV data handling, and model comparison.

