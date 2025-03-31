# TestLogger.py
import time
from .Config import AppConfig
from functools import wraps

@staticmethod
def log_test_entry(name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if AppConfig.testing_mode:
                fname = name or func.__name__
                print(f"🧪 Entering: {fname}")
                if args:
                    print("   ↳ args:")
                    for i, arg in enumerate(args):
                        print(f"     - arg[{i}]: {prettify(arg)}")
                if kwargs:
                    print("   ↳ kwargs:")
                    for k, v in kwargs.items():
                        print(f"     - {k}: {prettify(v)}")

            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time

            if AppConfig.testing_mode:
                print(f"   ✅ Finished: {func.__name__} → {prettify(result)}")
                print(f"   ⏱️ Duration: {duration:.4f} seconds")
            return result
        return wrapper
    return decorator

@staticmethod
def prettify(value, max_items=3, max_length=80):
    try:
        if isinstance(value, (list, tuple, set)):
            preview = list(value)[:max_items]
            return f"{type(value).__name__}({len(value)} items): {preview}"

        if isinstance(value, dict):
            preview = {k: value[k] for k in list(value)[:max_items]}
            return f"dict({len(value)} keys): {preview}"

        if isinstance(value, str):
            return f"str({len(value)}): '{value[:max_length]}{'...' if len(value) > max_length else ''}'"

        if hasattr(value, 'objectName') and value.objectName():
            return f"<{type(value).__name__} (objectName='{value.objectName()}')>"

        return f"<{type(value).__name__}>"
    except Exception as e:
        return f"<unprintable: {str(e)}>"


