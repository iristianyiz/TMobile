#!/usr/bin/env python3
"""
Test runner script for the QoD SDK.
This script sets up the environment and runs the test suite.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Set up the Python path and environment for testing."""
    # Add the src directory to Python path
    src_path = Path(__file__).parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # Set up test environment variables if not already set
    if not os.getenv("QOD_CLIENT_ID"):
        os.environ["QOD_CLIENT_ID"] = "test_client_id"
    if not os.getenv("QOD_CLIENT_SECRET"):
        os.environ["QOD_CLIENT_SECRET"] = "test_client_secret"
    if not os.getenv("QOD_PRIVATE_KEY_PATH"):
        os.environ["QOD_PRIVATE_KEY_PATH"] = "test_private_key.pem"

def install_test_dependencies():
    """Install test dependencies if not already installed."""
    try:
        import pytest
        print("✓ pytest is already installed")
    except ImportError:
        print("Installing test dependencies...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-e", ".[test]"
        ])

def run_tests():
    """Run the test suite."""
    print("Running QoD SDK tests...")
    print("=" * 50)
    
    # Run pytest with appropriate options
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--strict-markers",
        "--strict-config"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n" + "=" * 50)
        print("✓ All tests passed!")
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Tests failed with exit code {e.returncode}")
        sys.exit(e.returncode)

def main():
    """Main function to run the test suite."""
    print("QoD SDK Test Runner")
    print("=" * 50)
    
    # Set up environment
    setup_environment()
    
    # Install dependencies
    install_test_dependencies()
    
    # Run tests
    run_tests()

if __name__ == "__main__":
    main() 