import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")
import sys
import io

def evaluate_code(code: str) -> dict:
    """Runs the provided code and returns the printed output."""
    buffer = io.StringIO()
    sys_stdout = sys.stdout  # Save the original stdout

    try:
        sys.stdout = buffer
        exec(code)
        sys.stdout = sys_stdout

        printed_output = buffer.getvalue().strip()

        return {
            "status": "success",
            "output": printed_output if printed_output else None
        }

    except Exception as e:
        sys.stdout = sys_stdout
        return {
            "status": "error",
            "error": {
                "message": str(e),
                "type": type(e).__name__
            }
        }

def guardrail_check(code: str) -> bool:
    """Checks if the code contains any disallowed keywords."""
    disallowed_keywords = [
        # "import",
        "exec", "eval", "os", "sys", "open"
    ]
    return not any(keyword in code for keyword in disallowed_keywords)


def coder(code: str) -> str:
    print(code)
    """Processes the code, checks for guardrails, and evaluates it."""
    if not guardrail_check(code):
        return "Code contains disallowed libraries."

    result = evaluate_code(code)
    if result["status"] == "error":
        return f"Error: {result['error']['message']} (Type: {result['error']['type']})"
    return result["output"]
