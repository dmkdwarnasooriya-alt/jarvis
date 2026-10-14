#!/usr/bin/env python3
"""A small OpenAI-compatible terminal chat assistant for Termux."""
import json
import os
import sys
import urllib.error
import urllib.request

SYSTEM_PROMPT = (
    "You are Jarvis, a helpful assistant running in the user's Termux terminal. "
    "Give clear, concise answers. Never claim to run commands or inspect files; "
    "you only chat and suggest commands for the user to run."
)


def ask(messages):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Set it in your shell, then start Jarvis again.")
    base_url = os.environ.get("JARVIS_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("JARVIS_MODEL", "gpt-5.6-luna")
    payload = json.dumps({"model": model, "messages": messages}).encode("utf-8")
    request = urllib.request.Request(
        base_url + "/chat/completions", data=payload,
        headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError("API returned HTTP " + str(exc.code) + ": " + details) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError("Could not connect to the AI service: " + str(exc.reason)) from exc
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        raise RuntimeError("The AI service returned an unexpected response.") from exc


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python ~/jarvis/jarvis.py [question]")
        print("Interactive chat starts when no question is given.")
        print("Configure OPENAI_API_KEY, and optionally JARVIS_MODEL / JARVIS_BASE_URL.")
        return 0
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    if len(sys.argv) > 1:
        history.append({"role": "user", "content": " ".join(sys.argv[1:]).strip()})
        try:
            print(ask(history))
            return 0
        except RuntimeError as exc:
            print("Jarvis: " + str(exc), file=sys.stderr)
            return 1
    print("Jarvis is ready. Type /exit to quit, /reset to clear chat history.")
    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJarvis: See you.")
            return 0
        if not prompt:
            continue
        if prompt.lower() in ("/exit", "/quit"):
            print("Jarvis: See you.")
            return 0
        if prompt.lower() == "/reset":
            history = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("Jarvis: Chat history cleared.")
            continue
        history.append({"role": "user", "content": prompt})
        try:
            answer = ask(history)
            history.append({"role": "assistant", "content": answer})
            print("Jarvis: " + answer)
        except RuntimeError as exc:
            history.pop()
            print("Jarvis: " + str(exc), file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
