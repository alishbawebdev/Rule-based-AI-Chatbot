# Rule-based-AI-Chatbot
DecodeLabs AI Industrial Training Portfolio (Batch 2026). Contains 1 completed milestone of the 4-task series: Task 1 (AI Chatbot)
Project 1: Rule-Based AI Chatbot 🤖
Welcome to the repository for Project 1: Rule-Based AI Chatbot (DecoBot). This project serves as the foundational module of the Artificial Intelligence Engineering Industrial Training track at DecodeLabs (Batch: 2026).

Before diving into complex probabilistic machine learning systems, this project establishes a firm grip on deterministic control flow, string normalization, and strict programmatic logic engines.

🌟 Project Overview
The objective of this project is to construct a Rule-Based AI Chatbot that handles user interactions smoothly using strict conditional structures. It is modeled as a "White Box" system—providing absolute predictability, transparency, and zero risk of hallucination. This design aligns closely with modern industry architectures where deterministic rules are used as security guardrails over large language models.

The IPO Model Layer
The chatbot's code strictly reflects the Input-Process-Output (IPO) engineering blueprint:

Input (Raw Feed): Captures conversational user data via the console.

Process (The Logic Skeleton): Normalizes the raw text (case-insensitivity and whitespace trimming) and runs it through an intent-matching logic gate ecosystem.

Output (Feedback Loop): Delivers a prompt, clear response and sustains the chat ecosystem within a continuous execution environment.

✨ Key Features

Continuous Digital Loop: Runs continuously in the terminal environment until explicitly told to stop.

Input Sanitization: Automatically cleans inputs using .lower() and .strip() string methods to minimize matching errors caused by accidental uppercase letters or trailing spaces.

Deterministic Guardrails: Implements a comprehensive conditional tree checking for multiple human conversational variations.

Predefined Context Vocabulary: Capable of responding to specific greetings, general inquiries about Python/AI, time-of-day phrases, and system state checks.

Graceful Exit Mechanisms: Listens for distinct terminal signals like exit, quit, or bye to cleanly shut down execution.

🛠️ Technical Stack & Skills
Language: Python 3.x

Core Paradigms: Control flow loops (while), structural conditional architecture (if-elif-else), and basic data token standardization.

🚀 How To Run Locally
Prerequisites
Make sure you have Python 3 installed on your machine. You can verify your version by running:

Bash
python --version
Execution Steps
Open your project folder in VS Code.

Open the built-in terminal (Ctrl + \`` or Cmd + ``).

Run the script using Python:

Bash
python main.py
   *(Note: If your file is named something else, like `decobot.py`, run `python decobot.py` instead.)*

---

## 💬 Sample Interaction Guide

When you launch the program, `DecoBot` will initialize with a running confirmation layout:

```text
------------------------------------------
DecoBot is running! Type 'exit' to quit.
------------------------------------------
You: Hello
DecoBot: Hello! How can I help you?

You: what is AI
DecoBot: AI stands for Artificial Intelligence. It means making machines think like humans.

You: tell me a joke
DecoBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: exit
DecoBot: Goodbye! See you next time!
📝 Project Identity & Metadata
Role Path: AI Engineer Intern

Author: Alishba Ghulam Rasool

Organization: DecodeLabs

Batch Track: 2026 Milestone Phase
