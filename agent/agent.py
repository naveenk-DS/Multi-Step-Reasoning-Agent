from agent.planner import run_planner
from agent.executor import run_executor
from agent.verifier import run_verifier

MAX_RETRIES = 2

def solve(question: str):
    retries = 0
    checks = []

    while retries <= MAX_RETRIES:

        # 1. PLAN
        plan = run_planner(question)

        # 2. EXECUTE
        execution = run_executor(question, plan)

        # 3. VERIFY
        verification = run_verifier(
            question,
            execution["intermediate_solution"],
            execution["final_answer"]
        )

        checks.append({
            "check_name": "independent_verification",
            "passed": verification["passed"],
            "details": verification.get("issues", "")
        })

        if verification["passed"]:
            return {
                "answer": execution["final_answer"],
                "status": "success",
                "reasoning_visible_to_user": f"The result is {execution['final_answer']}.",
                "metadata": {
                    "plan": plan,
                    "checks": checks,
                    "retries": retries
                }
            }

        retries += 1

    return {
        "answer": None,
        "status": "failed",
        "reasoning_visible_to_user": "The system could not verify the solution.",
        "metadata": {
            "plan": plan,
            "checks": checks,
            "retries": retries
        }
    }
