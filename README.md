<p align="center">
<img src="./llm.jpg" width="400px"/>
</p>

# LLMTag

A simple interface to label clinical data using local large language models (LLMs)

### Features

1. Base code of getting started with LLMs
2. Try LLM's without PHI/PII issues and GPUs
3. Simple interface for several tasks
    - [x] Label Documents
    - [ ]  Fine-tune (upcoming)
    - [ ]  RAG (upcoming)
4. Be in control
   1. Try any of the latest models
   2. Control Context Length
   3. Tailor to your specific need

## Getting Started (Contributors)

1. Clone the llmtag repo
2. Download weights - any llama2 compatible model should work
    - Get [llama-7B-chat weights from HF](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf)
    - Save it under ./models/7B
3. Add the model path to the environment variable `MODEL`
    - create .env file in root directory of repository (e.g. touch .env)
    - copy and paste below or define your own path to the model binary (actual model weights)
    -  `.env`
        ```
        MODEL=./models/7B/llama-2-7b-chat.Q4_K_M.gguf
        ```
4. Initialize the environment with `poetry install` (if new to poetry, please check [this](https://python-poetry.org/))
5. For leveraging  GPUs, please check - [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
   - Follow the instructions for installation as per your machine specifications
   - For simple CPU use case, can resort to not using GPU, but will be very time intensive, orders of magnitude more
   - Ignore this step for now unless you know better

### Post installation
1. Run all tests using `poetry run python -m pytest tests/`
2. Run the default example: `poetry run python -m llmtag`

### Results

Raw Clinical notes
---

|    |   patient_id | notes                                                                        |   label |
|----|--------------|-------------------------------------------------------------------------------|---------|
|  0 |            1 | Patient complains of leg pain and swelling. Ultrasound confirms DVT.         |       1 |
|  1 |            2 | Patient experiences chest pain and shortness of breath. CT scan confirms PE. |       1 |
|  2 |            3 | Patient has a history of DVT. No current symptoms noted.                     |       0 |
|  3 |            4 | No complaints or symptoms related to VTE or PE.                              |       0 |

LLM labeled notes
---

|    |   patient_id | notes                                                                        |   label |   llm_label | llm_reasons              |
|----|--------------|-------------------------------------------------------------------------------|---------|-------------|--------------------------|
|  0 |            1 | Patient complains of leg pain and swelling. Ultrasound confirms DVT.         |       1 |           1 | Ultrasound confirms DVT  |
|  1 |            2 | Patient experiences chest pain and shortness of breath. CT scan confirms PE. |       1 |           1 | CT scan confirms PE      |
|  2 |            3 | Patient has a history of DVT. No current symptoms noted.                     |       0 |           0 | No Symptoms found        |
|  3 |            4 | No complaints or symptoms related to VTE or PE.                              |       0 |           0 | No evidence of VTE or PE |

Metrics on simulated data
---

#### Confusion Matrix

`n = 50`

|  |  | predicted | |
| -- | -- | -- | -- |
| Actual |  | 0 | 1 |
|  | 0 | 27 | 1 |
|  | 1 | 0 | 20 |


| Metric | | 
| -- | -- |
| F1 Score | 0.98 |
| Precision | 0.95 |
| Recall | 1.0 |
| Accuracy | 0.98 |

## Libraries Used

1. [llama.cpp](https://github.com/ggerganov/llama.cpp/tree/master)
2. [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
3. [Model Weights](https://huggingface.co/TheBloke)
4. [poetry](https://python-poetry.org/)
