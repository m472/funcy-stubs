from typing import Callable

def all_fn(*fs) -> Callable: ...
def any_fn(*fs) -> Callable: ...
def none_fn(*fs) -> Callable: ...
def one_fn(*fs) -> Callable: ...
def some_fn(*fs) -> Callable: ...