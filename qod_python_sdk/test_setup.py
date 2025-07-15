#!/usr/bin/env python3
"""
Simple test setup verification script.
This script checks if the test environment is properly configured.
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python {version.major}.{version.minor} is not supported. Need Python 3.7+")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_dependencies():
    """Check if required dependencies are installed."""
    dependencies = {
        'pytest': 'pytest',
        'requests': 'requests',
        'pyjwt': 'jwt',
        'cryptography': 'cryptography'
    }
    
    missing = []
    for package, import_name in dependencies.items():
        try:
            __import__(import_name)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is not installed")
            missing.append(package)
    
    if missing:
        print(f"\nTo install missing dependencies, run:")
        print(f"pip install {' '.join(missing)}")
        return False
    return True

def check_sdk_imports():
    """Check if SDK modules can be imported."""
    # Add src to path
    src_path = Path(__file__).parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    try:
        from tmode_qod import TmodeQod
        print("✅ TmodeQod can be imported")
    except ImportError as e:
        print(f"❌ Cannot import TmodeQod: {e}")
        return False
    
    try:
        from tmode_qod.net.environment import Environment
        print("✅ Environment can be imported")
    except ImportError as e:
        print(f"❌ Cannot import Environment: {e}")
        return False
    
    return True

def check_test_files():
    """Check if test files exist."""
    test_files = [
        "tests/test_qod_client.py",
        "tests/conftest.py",
        "tests/README.md"
    ]
    
    all_exist = True
    for test_file in test_files:
        if Path(test_file).exists():
            print(f"✅ {test_file} exists")
        else:
            print(f"❌ {test_file} is missing")
            all_exist = False
    
    return all_exist

def main():
    """Main function to run all checks."""
    print("QoD SDK Test Environment Check")
    print("=" * 40)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("SDK Imports", check_sdk_imports),
        ("Test Files", check_test_files),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"❌ Error during {name} check: {e}")
            results.append(False)
    
    print("\n" + "=" * 40)
    if all(results):
        print("✅ All checks passed! Test environment is ready.")
        print("\nTo run tests:")
        print("  pytest tests/")
        print("  python run_tests.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 