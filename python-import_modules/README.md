# Python Script Overview with Modules and Command-Line Arguments

This README explains how Python scripts commonly use **modules** and **command-line arguments**, with clear examples — all in one place.

---

## 📦 Modules

Here are some standard Python modules often used in command-line scripts:

| Module     | Purpose                                                                 |
|------------|-------------------------------------------------------------------------|
| `argparse` | Parse command-line arguments in a structured and user-friendly way.     |
| `sys`      | Access arguments (`sys.argv`) and system-related information.           |
| `os`       | Interact with the operating system (e.g. environment, paths, files).    |
| `pathlib`  | Handle file paths in an object-oriented and cross-platform way.         |
| `logging`  | Add structured logs for debugging and monitoring.                       |

---

## ⚙️ Command-Line Arguments (via `argparse`)

Arguments allow users to customize a script’s behavior without changing the code.

### Example: Expected Arguments

| Argument     | Description                                | Type    | Required | Example              |
|--------------|--------------------------------------------|---------|----------|----------------------|
| `--input`    | Path to the input file                     | `str`   | ✅ Yes   | `--input data.txt`   |
| `--verbose`  | Enable detailed output (flag, no value)     | `bool`  | ❌ No    | `--verbose`          |
| `--limit`    | Maximum number of items to process         | `int`   | ❌ No    | `--limit 100`        |
| `--mode`     | Mode of operation (e.g., fast, safe)       | `str`   | ❌ No    | `--mode fast`        |

### Minimal Example Using `argparse`

```python
import argparse

parser = argparse.ArgumentParser(description="Process some input file.")
parser.add_argument('--input', type=str, required=True, help="Input file path")
parser.add_argument('--verbose', action='store_true', help="Enable verbose output")
parser.add_argument('--limit', type=int, default=50, help="Limit the number of items")
parser.add_argument('--mode', choices=['fast', 'safe'], default='safe', help="Mode to run the script")

args = parser.parse_args()
