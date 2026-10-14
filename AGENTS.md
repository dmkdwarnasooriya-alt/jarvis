# Repository Guidelines

## Project Structure

- `jarvis.py` contains the command-line chat loop and OpenAI-compatible API client.
- `data/jarvis` is the Termux launcher installed as the `jarvis` command.
- `termux-package/kennethdevon/build.sh` contains the Termux package recipe.
- `README.md` documents setup and use; `LICENSE` contains the project license.
- There is currently no test suite or separate assets directory.

## Build, Run, and Development

This project uses Python’s standard library and has no build step or third-party Python dependencies. In Termux, install Python if needed with `pkg install python`. Run the source checkout with:

```sh
python3 jarvis.py
python3 jarvis.py "How do I find large files?"
```

The first command starts interactive chat; the second sends one prompt. Set `OPENAI_API_KEY` in the shell before making API requests. `JARVIS_MODEL` and `JARVIS_BASE_URL` optionally select a model and compatible API endpoint.

## Coding Style

Use four spaces for Python indentation, descriptive `snake_case` names for functions and variables, and uppercase names for module constants. Keep the client dependency-free unless a new dependency is justified and documented. The launcher should remain a small POSIX shell script that delegates to the Python entry point. Keep package paths and names consistent with `termux-package/kennethdevon/build.sh`.

## Testing

No automated test framework is configured. For changes to the CLI, manually check help output with `python3 jarvis.py --help`; API behavior requires a valid key and available API credits. Do not commit API keys, `.env` files, or other credentials.

## Commits and Pull Requests

Use short, imperative commit subjects, such as `Add reset command` or `Update Termux package metadata`. Pull requests should explain the user-visible change, list relevant manual checks, link related issues when applicable, and note any changes to API configuration or package installation behavior.

## Security and Configuration

Read API credentials only from environment variables. Never add secrets to source files, logs, examples containing real values, or commits. Jarvis sends chat messages to the configured API endpoint and does not execute terminal commands.
