
A stub file (see PEP 484) contains only type hints for the public interface of a module, with empty function bodies. Mypy can use a stub file instead of the real implementation to provide type information for the module. They are useful for third-party modules whose authors have not yet added type hints (and when no stubs are available in typeshed) and C extension modules (which mypy can’t directly process).



# Referencias
- https://www.python.org/dev/peps/pep-0561/