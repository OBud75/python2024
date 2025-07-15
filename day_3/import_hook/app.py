def log(module):
    print(f"[log] imported {module.__name__}")
    return module


@log
import abc

@log
import os as system

print(abc.ABCMeta)
print(system.path)
