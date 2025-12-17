from flask import Flask, request, jsonify
from agent.agent import solve

app = Flask(__name__)

@app.post("/solve")
def solve_endpoint():
    data = request.json
    return jsonify(solve(data["question"]))

app.run(port=8080)
