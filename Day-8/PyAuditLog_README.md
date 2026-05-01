# PyAuditLog - Professional Auditing Library

PyAuditLog is a comprehensive Python library designed to provide automated, non-intrusive auditing for functions and methods. By utilizing Python decorators, it allows for high-granularity logging of performance metrics, input arguments, and execution outcomes.

# The Problem in the Tech World
In professional software, every time a sensitive action happens (a user changes a password, a transaction is made, an API is called), developers have to manually write logging code. It’s often messy, inconsistent, and hard to read.

# The Solution: PyAuditLog
We have build a simple, lightweight library that a developer can "drop" into any project to automatically track execution time, function inputs, and success/failure rates with zero boilerplate code.

# The Core Concept: Decorators
To make this effective, we will use Python Decorators. This allows a developer to simply put @audit above any function to instantly get professional logging

```python
#importing some necessary libraries
import time
import datetime
import json
import functools
```

```python
class LogHandler:
    """Base class for all log handlers."""
    def emit(self, entry):
        raise NotImplementedError("Subclasses must implement emit method")

class FileLogHandler(LogHandler):
    """Writes log entries to a specified file."""
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            # Ensure the log file is created or truncated if it's new for this session
            with open(self.file_path, "w") as f:
                f.write('') # Clear file on init, or change to 'a' if logs should persist across sessions
        except Exception as e:
            print(f"Error initializing log file {self.file_path}: {e}")

    def emit(self, entry):
        try:
            with open(self.file_path, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"File logging failed for {self.file_path}: {e}")

class ConsoleLogHandler(LogHandler):
    """Prints log entries to the console."""
    def emit(self, entry):
        print(f"[CONSOLE LOG] {json.dumps(entry)}")

class PyAuditLog:
    """
    A lightweight auditing library to track function performance and behavior.
    """
    def __init__(self, handlers=None):
        self.handlers = handlers if handlers is not None else [FileLogHandler("audit_log.json")]

    def audit(self, func=None, log_args=True, exclude_args=None, log_return_value=False):
        """A decorator that logs function execution details."""
        if exclude_args is None:
            exclude_args = []

        def decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                timestamp = datetime.datetime.now().isoformat()

                function_args = {}
                if log_args:
                    # Log positional arguments
                    for i, arg in enumerate(args):
                        arg_name = f'arg_{i}' # Default name for positional args
                        if f.__code__.co_varnames and i < len(f.__code__.co_varnames):
                            arg_name = f.__code__.co_varnames[i]
                        if arg_name not in exclude_args:
                            function_args[arg_name] = str(arg)
                    # Log keyword arguments
                    for k, v in kwargs.items():
                        if k not in exclude_args:
                            function_args[k] = str(v)

                try:
                    # Execute the actual function
                    result = f(*args, **kwargs)
                    status = "SUCCESS"
                    error = None
                    return_value = str(result) if log_return_value else None
                except Exception as e:
                    result = None
                    status = "FAILED"
                    error = str(e)
                    return_value = None

                end_time = time.time()
                duration = end_time - start_time

                # Create the log entry
                log_entry = {
                    "timestamp": timestamp,
                    "function": f.__name__,
                    "status": status,
                    "duration_sec": round(duration, 4),
                    "args": function_args,
                    "error": error
                }
                if log_return_value:
                    log_entry["return_value"] = return_value

                # Write to our 'database' (the JSON file) using handlers
                self._write_to_log(log_entry)

                if error:
                    raise Exception(f"Audited function failed: {error}")
                return result

            return wrapper

        # This handles both @audit and @audit(param=value) usages
        if func is None:
            return decorator
        else:
            return decorator(func)

    def _write_to_log(self, entry):
        """Helper to dispatch log entries to all configured handlers."""
        for handler in self.handlers:
            handler.emit(entry)

    def get_report(self, log_file=None, function_name=None, status=None):
        """Reads the log file from a FileLogHandler and prints a summary with optional filtering and aggregation."""
        target_file = None
        if log_file:
            target_file = log_file
        else:
            # Try to find a FileLogHandler's path if no specific file is given
            for handler in self.handlers:
                if isinstance(handler, FileLogHandler):
                    target_file = handler.file_path
                    break

        if target_file is None:
            print("No file log handler found or log_file specified for report.")
            return

        print(f"\n--- ✏️ Audit Report: {target_file} ---")
        logs = []
        try:
            with open(target_file, "r") as f:
                for line in f:
                    logs.append(json.loads(line))
        except FileNotFoundError:
            print(f"No audit log file found at {target_file}")
            return
        except Exception as e:
            print(f"Error reading log file: {e}")
            return

        # Apply filters
        filtered_logs = []
        for log in logs:
            if function_name and log['function'] != function_name:
                continue
            if status and log['status'] != status:
                continue
            filtered_logs.append(log)

        if not filtered_logs:
            print("No logs found matching the criteria.")
            return

        # Print filtered logs
        print("--- Filtered Logs ---")
        for log in filtered_logs:
            print(f"[{log['timestamp']}] {log['function']} -> {log['status']} ({log['duration_sec']}s)")

        # Aggregation
        total_calls = len(filtered_logs)
        successful_calls = len([l for l in filtered_logs if l['status'] == 'SUCCESS'])
        failed_calls = total_calls - successful_calls
        avg_duration = sum(l['duration_sec'] for l in filtered_logs) / total_calls if total_calls > 0 else 0

        print("\n--- Summary ---")
        print(f"Total Audited Calls: {total_calls}")
        print(f"Successful Calls: {successful_calls}")
        print(f"Failed Calls: {failed_calls}")
        print(f"Average Duration: {avg_duration:.4f}s")
```

```python
# Initialize PyAuditLog with specific handlers
app_file_handler = FileLogHandler("my_app_audit.json")
console_handler = ConsoleLogHandler()
lib = PyAuditLog(handlers=[app_file_handler, console_handler])
audit = lib.audit
```

# How a "User" would use your library

```python
@audit(log_args=True, exclude_args=['password'], log_return_value=True)
def process_payment(amount, password="secret_pwd"):
    print(f"Processing ${amount} with password: {password}...")
    time.sleep(0.5) # Simulate work
    if amount > 1000:
        raise ValueError("Amount too high!")
    return "Paid!"

@audit(log_args=False, log_return_value=False)
def risky_database_query(query_string):
    print(f"Executing risky query: {query_string}")
    raise ValueError("Database connection lost!")

# Execute user code
print("\n--- Running Demos ---")
user_status = process_payment(150, password="mySecureP4ss")
print(f"Payment Status: {user_status}")

try:
    process_payment(1200)
except Exception as e:
    print(f"Caught expected error: {e}")

try:
    risky_database_query("DROP TABLE users;")
except:
    pass

# Generate the audit report
lib.get_report(log_file="my_app_audit.json") # Full report
lib.get_report(log_file="my_app_audit.json", status="FAILED") # Only failed calls
lib.get_report(log_file="my_app_audit.json", function_name="process_payment") # Only process_payment calls
```

---

## Technical Specifications
- **Integration:** Decorator-based (`@audit`)
- **Logging Formats:** JSON, Console, Custom Handlers
- **Security:** Argument masking and exclusion for sensitive data

## Author Information
**Name:** Mayank Gariya  
**Email:** mayankgariya482@gamil.com  
**Project Date:** May 2026
