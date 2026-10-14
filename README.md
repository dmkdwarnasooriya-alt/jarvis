# Jarvis for Termux

Jarvis is a lightweight chat assistant that runs as a command inside Termux. It uses Python's standard library and an OpenAI-compatible Chat Completions API. It does not execute terminal commands.

## Configure

Set an API key in your Termux shell (use a replacement key if an earlier key was exposed):

```sh
export OPENAI_API_KEY='your-api-key'
```

The API account needs available credits. ChatGPT subscriptions and API billing are separate.

## Run from this source checkout

```sh
python ~/jarvis/jarvis.py
```

Ask one question:

```sh
python ~/jarvis/jarvis.py "How do I find large files?"
```

Interactive chat accepts `/reset` to clear history and `/exit` to quit.

## Configuration

- `OPENAI_API_KEY` is required.
- `JARVIS_MODEL` changes the model (default: `gpt-5.6-luna`).
- `JARVIS_BASE_URL` changes the API root (default: `https://api.openai.com/v1`) for an OpenAI-compatible provider.

## Termux package

The package recipe is in `termux-package/kennethdevon/build.sh`. It is intended for submission to the official Termux package repository. Once accepted and released there, installation will be:

```sh
pkg update
apt install kennethdevon
```

The recipe must be reviewed and published by the Termux package maintainers before this command is available from the default repositories.
