from agent.agent import solve

def test_time_difference():
    res = solve("A train leaves at 14:30 and arrives at 18:05. How long?")
    assert res["status"] == "success"
    assert "3 hours 35 minutes" in res["answer"]

def test_apples():
    res = solve("Alice has 3 red apples and twice as many green apples. Total?")
    assert res["status"] == "success"
    assert res["answer"] == "9"
