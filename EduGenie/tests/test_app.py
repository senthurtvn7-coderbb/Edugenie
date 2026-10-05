import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200


def test_qa_endpoint():
    response = client.post(
        "/qa",
        json={"question": "What is Python?"}
    )
    assert response.status_code in [200, 429, 503]


def test_explain_endpoint():
    response = client.post(
        "/explain",
        json={"topic": "Python"}
    )
    assert response.status_code in [200, 429, 503]


def test_quiz_endpoint():
    response = client.post(
        "/quiz",
        json={"topic": "Python"}
    )
    assert response.status_code in [200, 429, 503]


def test_summarize_endpoint():
    response = client.post(
        "/summarize",
        json={"text": "Python is a programming language."}
    )
    assert response.status_code in [200, 429, 503]


def test_learning_path_endpoint():
    response = client.post(
        "/learn/recommendations",
        json={"topic": "Python"}
    )
    assert response.status_code in [200, 429, 503]