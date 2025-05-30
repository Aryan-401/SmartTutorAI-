import logging
logging.basicConfig(level=logging.ERROR)
import re

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
    """Checks if the code contains any disallowed keywords (as whole words)."""
    disallowed_keywords = [
        # "import",
        "exec", "eval", "os", "sys", "open"
    ]
    pattern = r'\b(' + '|'.join(re.escape(kw) for kw in disallowed_keywords) + r')\b'
    return not re.search(pattern, code)



def coder(code: str) -> str:
    """Processes the code, checks for guardrails, and evaluates it."""
    if not guardrail_check(code):
        return "Code contains disallowed libraries."

    result = evaluate_code(code)
    if result["status"] == "error":
        return f"Error: {result['error']['message']} (Type: {result['error']['type']})"
    return result["output"]
