# Streamlit LLM Basics

Classroom examples of Streamlit interfaces and local question answering with the open-weight Gemma 2 model through Ollama and LangChain.

**Author:** [faiz-sheikh](https://github.com/faiz-sheikh)

## Examples

| File | What it demonstrates |
|---|---|
| `app.py` | A text question, role-based prompt, `ChatOllama(model="gemma2:2b")`, and a displayed response |
| `streamlit_tutorial.py` | Text, Markdown, widgets, forms, charts, CSV uploads, an image and an embedded video |
| `assets/sample.svg` | Bundled illustration for the tutorial image example |

These are two separate apps. The tutorial does not call an LLM. Its login form is a demonstration of form widgets, not a real sign-in system. The view selector displays placeholder text, and its random chart data is regenerated on reruns. Caching is not implemented in the tutorial.

## LLM workflow

```text
Question → ChatPromptTemplate → Gemma 2 via Ollama → StrOutputParser → Streamlit
```

`prompt | llm | output_parser` connects these steps. The prompt supplies system and user messages; Ollama runs the pretrained model locally; the output parser returns text for display. Each question is independent: conversation history is not maintained.

This project uses an existing open-weight model. It does not train or fine-tune an LLM. Document loading, embeddings, FAISS and retrieval-augmented generation are not included in this version. The document question-answering example is deferred.

## Setup on Windows

Install Python, [Ollama](https://ollama.com/download), and optionally the VS Code Python extension. Open a terminal in this folder.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The requirements reflect the direct imports. Streamlit 1.49 or newer supports the tutorial's `width="content"` image argument. This is not a complete version lock.

For the Gemma example, ensure Ollama is running, then download the exact classroom model:

```powershell
ollama pull gemma2:2b
ollama list
```

The first download requires internet and local disk space. Ollama is a separate installed application, not a Python dependency. No hosted-LLM API key is required by this code. Model usage remains subject to the [Gemma model terms](https://ollama.com/library/gemma2:2b).

## Run an example

From this project folder, run one app at a time:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Or run the widget tutorial:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_tutorial.py
```

Use the local URL printed in the terminal. Stop the server with Ctrl+C. Use `streamlit run` rather than executing these files as ordinary Python scripts.

## Expected behaviour and limitations

- The Gemma app generates an answer after a question is submitted in the text field. Ollama must be reachable and `gemma2:2b` must be installed. Response speed depends on the computer; generated answers may be inaccurate.
- The tutorial greets the entered name, draws random line/bar charts, displays an uploaded CSV, and demonstrates other inputs and conditional sections.
- The login form accepts submitted values without checking credentials. Do not enter real passwords.
- The image is bundled locally. The YouTube video requires internet and may depend on availability outside this project.
- Uploaded CSVs are read as UTF-8 by pandas' default behaviour; malformed files may raise errors. Production error handling is outside this classroom example.
- Uploaded CSVs, credentials, environment folders and model downloads should remain out of Git.

## Learning outcomes

Understand Streamlit's top-to-bottom execution, common widgets, forms and media, and the difference between a UI tutorial and an LLM-backed application. Trace a simple LangChain prompt/model/parser pipeline without introducing document retrieval or additional frameworks.

## References

- [Streamlit documentation](https://docs.streamlit.io/)
- [LangChain Ollama integration](https://docs.langchain.com/oss/python/integrations/chat/ollama)
- [Gemma 2 on Ollama](https://ollama.com/library/gemma2:2b)

## Local verification

Both app screens were checked with Streamlit's AppTest using the existing classroom environment. The tutorial greeting and conditional details passed. The Gemma app was also tested through its full Streamlit/LangChain/Ollama path: the question `Reply with one word: Ready.` produced `Ready.` on screen. This is a functional smoke check, not an accuracy evaluation.

Verified environment: Python 3.13, Streamlit 1.66.1, langchain-core 1.7.0, langchain-ollama 1.1.0, pandas 3.1.0 and NumPy 2.5.4. Other compatible versions may work; requirements are not locked to this machine.

## Hosting the tutorial

For Streamlit Community Cloud, connect this repository, choose the `main` branch, and select `streamlit_tutorial.py` as the entrypoint. Include `assets/sample.svg` in the repository. The included requirements support both examples; the tutorial does not need Ollama.

The standalone Gemma app expects Ollama on the machine running the app. A cloud deployment cannot access a laptop's `localhost`; it needs a separately reachable model service. This project currently demonstrates local Gemma inference.
