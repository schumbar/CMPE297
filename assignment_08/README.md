# Assignment 08: LLM Ops and GenAI Application

## Assignment Overview

This assignment involves showcasing an end-to-end Large Language Model (LLM) Operations (LLM Ops) Generative AI (GenAI) application.
The goal is to build and demonstrate a production-ready LLM system that encapsulates the full lifecycle of a GenAI application.
The system should address key aspects of LLM Ops, including data preparation, model training, deployment, and user interaction,
providing a seamless and operationally robust workflow.

## Deliverables

All deliverables for this assignment are located under the `assignment_08` directory.
Please see below for the list of deliverables for this assignment:

1. `README.md`: README file containing the assignment descriptions and a comprehensive list of deliverables.
2. [Youtube Video Link](youtube.com): Youtube video link to the application walkthrough.
3. `MyApp`: Directory which contains the application code and instructions on how to run and use the application.

### References

1. [An End-to-End Framework for Production-Ready LLM Systems by Building Your LLM Twin](https://www.comet.com/site/blog/an-end-to-end-framework-for-production-ready-llm-systems-by-building-your-llm-twin/)
2. [LLM Twin Course GitHub Repository](https://github.com/decodingml/llm-twin-course)
3. [SLM Innovator Lab LLM Ops Studio](https://azure.github.io/slm-innovator-lab/3_llmops-aistudio/README.html)
4. [End-to-End Generative AI Projects GitHub Repository](https://github.com/GURPREETKAURJETHRA/END-TO-END-GENERATIVE-AI-PROJECTS)
5. [GenAI Examples GitHub Repository](https://github.com/opea-project/GenAIExamples)

### INSTRUCTIONS TO RUN THE APPLICATION

This section outlines how to run the application.
This section assumes that you already have docker desktop installed on your machine and you are able to run docker compose commands successfully.
Please follow the following steps to run the application:

1. Create a `.env` file in the root directory with your OpenAI API key. The file should look like this:

```bash
OPENAI_API_KEY=your_api_key_here
```

2. **Build and run using Docker Compose**

```bash
# Build and start the container
docker-compose up --build   
# To run in detached mode (background)
docker-compose up --build -d
```

3. **Access the Application**
Once the application is running, you can access it by navigating to `http://localhost:8000` in your web browser.
