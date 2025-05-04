import pytest
from dotenv import load_dotenv
import os
import sys

# Load environment variables from the .env file
load_dotenv()

# Add PYTHONPATH to sys.path
pythonpath = os.getenv("PYTHONPATH")
if pythonpath and pythonpath not in sys.path:
    sys.path.insert(0, pythonpath)

# Ensure PYTHONPATH is set
@pytest.fixture(scope="session", autouse=True)
def check_pythonpath():
    pythonpath = os.getenv("PYTHONPATH")
    assert pythonpath is not None, "PYTHONPATH is not set. Make sure .env is configured correctly."
    print(f"PYTHONPATH is set to: {pythonpath}")