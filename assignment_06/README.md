# Assignment 06 README

## Assignment Descriptions

### Transformers and finetuning with LLMs

This assignment requires completing two main tasks: implementing NanoGPT from scratch and reproducing the "Textbooks Are All You Need" case study. Both tasks involve creating modular and well-documented code while providing comprehensive artifacts.

#### Part A - Implement NanoGPT

**Description:**  
The first part of the assignment involves implementing NanoGPT from scratch using PyTorch. The code should be modular and developed in Google Colab, ensuring a debugging experience comparable to the original NanoGPT Colab notebook. Resources for guidance include the [NanoGPT Colab](https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing), a [YouTube tutorial](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=18s), and a [class presentation](https://docs.google.com/presentation/d/1fk8QlODYkBTTH4ftw8M7Sw_tmhJa8KB97s7dYP6s4mI/edit#slide=id.g24535d0c6d4_0_178). After building the implementation, you will train the model using a book of your choice, ensuring it differs from Shakespeare’s works, which are used in the original NanoGPT setup. The final submission should include several deliverables: a Colab notebook demonstrating the code, a Medium article that explains each section of the code in depth, the input and output files used in training, and a short, 10-minute presentation that walks through the implementation step by step. Utilizing the GPT-4 Code Interpreter plugin for assistance is encouraged to streamline the coding process and debugging.

#### Part B - Implement the "Textbooks Are All You Need" Case Study

**Description:**  
The second part of the assignment requires recreating the "Textbooks Are All You Need" case study using a smaller dataset. The implementation should be done in Google Colab Pro with an A100 GPU for optimal performance. You will use your own dataset and process a smaller amount of data to simplify the experiment while maintaining the integrity of the methodology. Resources available for this task include a [YouTube video](https://www.youtube.com/watch?v=gmFi6W8DPdM), the [GitHub repository](https://github.com/jina-ai/textbook), the [original Colab notebook](https://colab.research.google.com/drive/1T4IfGfDJ8uxgU8XBPpMZivw_JThzdQim?usp=sharing), and the [research paper PDF](https://arxiv.org/pdf/2306.11644.pdf). The final submission should include a Colab notebook containing the complete implementation, input and output files, and additional artifacts demonstrating your results. Assistance from GPT-4 is recommended to handle complex parts of the implementation and ensure clarity in execution.

## List of Deliverables

All deliverables for this assignment are located under the `assignment_06` directory.

1. `README.md`: README file containing the assignment descriptions and a comprehensive list of deliverables.
2. `ShawnChumbar_Assignment06_PartA.ipynb`: Colab notebook for Part A - NanoGPT.
3. `ShawnChumbar_Assignment06_PartB.ipynb`: Colab notebook for Part B - "Textbooks Are All You Need" Case Study.
4. `input.txt`: Input file for Part A - NanoGPT.
5. `ckpt.pt`: Output file for Part A - NanoGPT.
6. [Medium Article](https://medium.com/@shawn.chumbar/understanding-nanogpt-a-deep-dive-into-transformer-architecture-implementation-9a7167b7d58c): Medium article explaining the implementation of NanoGPT.
7. [Video Presentation Link](https://www.youtube.com): Link to the video presentation explaining the code.

TODO: Add Medium Article Link, Create Video Presentation, and update video link.

## List of References

1. [NanoGPT Colab Notebook](https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing)
2. [YouTube Tutorial](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=18s)
3. [Class Presentation](https://docs.google.com/presentation/d/1fk8QlODYkBTTH4ftw8M7Sw_tmhJa8KB97s7dYP6s4mI/edit#slide=id.g24535d0c6d4_0_178)
4. [YouTube Video](https://www.youtube.com/watch?v=gmFi6W8DPdM)
5. [GitHub Repository](https://github.com/jina-ai/textbook)
6. [Colab Notebook](https://colab.research.google.com/drive/1T4IfGfDJ8uxgU8XBPpMZivw_JThzdQim?usp=sharing)
7. [Research Paper (PDF)](https://arxiv.org/pdf/2306.11644.pdf)
