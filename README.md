# Mock-bit-interview
### What is MockBit?
MockBit, the cutting-edge website that aims to revolutionize the interview preparation experience for students and professionals alike. Our project is built on the foundation of Artificial Intelligence (AI), specifically integrating Large Language Models (LLM) fine-tuned with a carefully curated dataset. The result is a platform that offers a contextualized and effective mock interview experience.

## Technology used:
* Artificial Intelligence
* Langchain
* LLM(Large language model)
* Nextjs
* Tailwindcss
* FastAPI

## Working:
### Project Overview:
The project aims to create an interactive web-based platform for practicing data science interview questions. It provides a simulated interview environment where users can receive questions, submit answers, and receive evaluations.

### Architecture:
The project follows a client-server architecture. The frontend is built using Nextjs, a popular JavaScript library for building user interfaces, while the backend is implemented using Python.

The frontend consists of several components designed to provide a seamless user experience. It includes a navbar for navigation, a main page for displaying interview questions, and an input area for submitting answers. The frontend communicates with the backend to fetch interview questions, submit answers, and receive evaluations.

The backend serves as the core of the application, handling data processing, authentication, and authorization. It is implemented using FastAPI, which provides automatic validation, serialization, and documentation of API endpoints. The backend exposes RESTful APIs for fetching interview questions, evaluating answers, and managing user sessions. FastAPI's asynchronous capabilities ensure high performance and scalability, making it suitable for handling concurrent requests efficiently.

### User flow
1. Fetching Questions: Upon loading the application, the frontend sends a request to the backend API implemented in FastAPI to fetch a data science interview question.
2. Submitting Answers: Users input their answers in the provided text area and submit them using the designated button. The frontend sends the user's answer to the backend API for evaluation.
3. Evaluation: The backend API receives the user's answer, processes it, and provides an evaluation based on predefined criteria. The evaluation result is sent back to the frontend for display.
4. User Interaction: Users can interact with the application by navigating through different pages, submitting answers, and viewing evaluation results. The frontend dynamically updates based on user actions and backend API responses.
5. Security consideration: HTTPS: All communication between the client and server is encrypted using HTTPS to prevent data interception and tampering.
