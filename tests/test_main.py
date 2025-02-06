import os
import sys

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import main  # Now the main module is available for use

# Dummy responses to simulate ollama.chat behavior
def dummy_chat(model, messages, stream=False):
    if stream:
        return iter([{"message": {"content": "dummy streaming response"}}])
    else:
        return {"message": {"content": "dummy basic response"}}

def test_run_basic(monkeypatch, capsys):
    monkeypatch.setattr(main, "ollama", type("DummyOllamaModule", (), {"chat": dummy_chat}))
    main.run_basic()
    captured = capsys.readouterr().out
    assert "dummy basic response" in captured

def test_run_basic_streaming(monkeypatch, capsys):
    monkeypatch.setattr(main, "ollama", type("DummyOllamaModule", (), {"chat": dummy_chat}))
    main.run_basic_streaming()
    captured = capsys.readouterr().out
    assert "dummy streaming response" in captured
