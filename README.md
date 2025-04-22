# browser-use

Make websites accessible for AI agents using Playwright and LangChain.

## Features

- Web scraping with Playwright
- Integration with LangChain agents
- Markdown conversion of web content
- AI accessibility layer

## Installation

```bash
pip install browser-use
from browser_use import some_agent_runner

async def main():
    await some_agent_runner.run(
        task="Summarize the latest news from https://example.com"
    )

🧪 Quick Example
from browser_use import some_agent_runner

async def main():
    await some_agent_runner.run(
        task="Summarize the latest news from https://example.com"
    )
🛠 Requirements
Python 3.11+

playwright, httpx, langchain-core, openai, and more.

See full dependencies in pyproject.toml.

🔍 Development Setup
bash
Copy
Edit
git clone https://github.com/browser-use/browser-use.git
cd browser-use

# Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"

🧰 Built With
Playwright

LangChain

Pydantic

FastAPI

📃 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Developed by Gregor Zunic
GitHub: @browser-use

🌍 Repository
📦 https://github.com/browser-use/browser-use

---

Let me know if you'd like to personalize the **example usage**, update author info, or add badges like PyPI version or CI status. Want me to drop this directly into a `README.md` file for you?
