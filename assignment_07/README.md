# Assignment 07: Advanced Prompt Engineering Strategies

## Assignment Overview

This assignment focuses on demonstrating and implementing advanced prompt engineering techniques using GPT-3.5 or GPT-4. The tasks include practical examples, failure cases, prompt templates, and implementations across diverse fields.

### Part A: Illustrate Prompt Engineering Techniques

Develop a Colab notebook that demonstrates various prompt engineering techniques discussed in class. For each technique, provide examples of both success and failure cases and show how different prompting strategies address these failures. Techniques to include:  

- **ICL (In-Context Learning)**  
- **CoT (Chain of Thought)**  
- **iCOT (Iterative Chain of Thought)**  
- **TOT (Tree of Thought)**  
- **GOT (Graph of Thought)**  
- **AOT (Agent of Thought)**  
- **RASCEF (Reasoning and Structured Contextual Evidence Framework)**  
- **REACT (Reasoning and Acting Pattern)** ([Learn more](https://til.simonwillison.net/llms/python-react-pattern#:~:text=The%20ReAct%20pattern%20(for%20Reason,results%20back%20into%20the%20LLM.))  
- **Forest of Thoughts (using LangChain)** ([Learn more](https://www.linkedin.com/posts/richard-walker-a18528_forest-of-thoughts-boosting-large-language-activity-7073925128778067968-xAHN/))  
  - [Tree of Thought UI GitHub Repository](https://github.com/mazewoods/tree-of-thought-ui)

Your Colab notebook should clearly demonstrate how these techniques enhance performance, with modular code and explanations.

### Part B: Write 21 Prompt Templates

Create 21 diverse and practical prompt templates, ensuring a mix of success and failure cases. Present these templates both in a Colab notebook and as a slide deck. Templates should illustrate the following prompt patterns, referencing the resources provided:  

- **Input Semantics:** Meta Language Creation  
- **Output Customization:** Output Automater, Persona, Visualization Generator, Recipe, Template  
- **Error Identification:** Fact Check List, Reflection  
- **Prompt Improvement:** Question Refinement, Alternative Approaches, Cognitive Verifier, Refusal Breaker  
- **Interaction:** Flipped Interaction, Game Play, Infinite Generation  
- **Context Control:** Context Manager  

Refer to:

- [Prompting Guide](https://www.promptingguide.ai/papers)
- [Research Paper](https://arxiv.org/pdf/2302.11382.pdf)

### Part C: Create Prompts for Diverse Fields

Select 10 diverse fields (e.g., HR, teaching, finance, etc.) and write three unique and practical prompts for each field. Each prompt should include test cases to verify its usefulness and adaptability. Follow best practices outlined in the [OpenAI API Prompt Engineering Guide](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api).

### Part D: Implement OpenAI Examples with PaLM 2 API

Using the [OpenAI Examples](https://platform.openai.com/examples), adapt and implement these examples with the PaLM 2 API. Provide your implementation in Colab and ensure functionality with relevant test cases.

### Part E: API Function Call Example

Write a Colab notebook showcasing an example of OpenAI API function calls in a practical use case. Include detailed explanations, inputs, and outputs.

### Part F: System Prompt Example

Develop a use case that demonstrates how to effectively use system prompts in OpenAI. Include an example implementation in Colab, highlighting its application and results.

### Deliverables

1. Colab notebooks for all tasks (A-F).
2. A slide deck showcasing the 21 prompt templates (Part B).  
3. Test cases for prompt evaluation (Parts A, C, and E).  
4. Modular and well-documented code for all implementations.  

This structure simplifies the assignment into clear sections, ensuring readability and easier task management.

### References

1. [NanoGPT Original Colab Notebook](https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing)
2. [NanoGPT Tutorial (YouTube)](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=18s)
3. [Class Presentation](https://docs.google.com/presentation/d/1fk8QlODYkBTTH4ftw8M7Sw_tmhJa8KB97s7dYP6s4mI/edit#slide=id.g24535d0c6d4_0_178)
4. [ReAct Pattern Explanation](https://til.simonwillison.net/llms/python-react-pattern#:~:text=The%20ReAct%20pattern%20for%20Reason,results%20back%20into%20the%20LLM.)
5. [Forest of Thoughts Explanation (LinkedIn)](https://www.linkedin.com/posts/richard-walker-a18528_forest-of-thoughts-boosting-large-language-activity-7073925128778067968-xAHN/)
6. [Tree of Thought UI (GitHub)](https://github.com/mazewoods/tree-of-thought-ui)
7. [Prompting Guide](https://www.promptingguide.ai/papers)
8. [Research Paper (Prompt Patterns)](https://arxiv.org/pdf/2302.11382.pdf)
9. [Best Practices for Prompt Engineering with OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
10. [OpenAI Examples](https://platform.openai.com/examples)
