from typing import Any

# This is a very complicated module, so for now we mark it as incomplete with
# the `__getattr__` special function.
# See https://github.com/python/typeshed/issues/5

def __getattr__(name: str) -> Any: ...
