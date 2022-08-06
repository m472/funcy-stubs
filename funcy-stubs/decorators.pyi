from contextlib import ContextDecorator as ContextDecorator
from contextlib import contextmanager as contextmanager
from inspect import unwrap as unwrap
from typing import Any, Callable, Dict, Tuple

class Call:
    def __call__(self, *a, **kw): ...
    def __init__(
        self,
        func: Callable,
        args: Tuple[Any, ...],
        kwargs: Dict[str, Any],
    ) -> None: ...

def arggetter(func: Callable, _cache: Dict[Callable, Callable] = ...) -> Callable: ...
def decorator(deco: Callable) -> Callable: ...
def get_argnames(func: Callable) -> Tuple[str, ...]: ...
def has_1pos_and_kwonly(func: Callable) -> bool: ...
def has_single_arg(func: Callable) -> bool: ...
def make_decorator(
    deco: Callable,
    dargs: Tuple[Any, ...] = ...,
    dkwargs: Dict[str, Any] = ...,
) -> Callable: ...
def update_wrapper(
    wrapper: Callable, wrapped: Callable, assigned=..., updated=...
) -> Callable: ...
def wraps(wrapped: Callable, assigned=..., updated=...) -> Callable: ...