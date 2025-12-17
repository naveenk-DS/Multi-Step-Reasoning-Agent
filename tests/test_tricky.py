from agent.agent import solve

def test_meeting_slots():
    res = solve("A meeting needs 60 minutes. Slots: 09:00–09:30, 09:45–10:30, 11:00–12:00.")
    assert res["status"] == "success"
