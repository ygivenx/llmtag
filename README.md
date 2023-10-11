## Getting Started (Contributors)

1. Clone the llmtag repo
2. Download the llama 7B weights[https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q4_K_M.gguf] for 7B no chat model and save it under ./models/7B
3. Initialize the environment with `poetry install` (if new to poetry, please check [this](https://python-poetry.org/))
4. For leveraging  GPUs, please check - [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
  - Follow the instructions for installation as per your machine specifications

After installation please verify
- Make sure the high level API example works (run example.py file)
```
>>> from llama_cpp import Llama
>>> llm = Llama(model_path="./models/7B/llama-model.gguf")
>>> output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
>>> print(output)
```

## Libraries Used

1. [llama.cpp](https://github.com/ggerganov/llama.cpp/tree/master)
2. [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
3. [llama2](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)
4. [poetry](https://python-poetry.org/)