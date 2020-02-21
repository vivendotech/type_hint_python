# Criando os própios tipos.


## Type aliases
```python
AliasType = Union[List[Dict[Tuple[int, str], Set[int]]], Tuple[str, List[str]]]

def f() -> AliasType:
    pass

```

## Segunda forma  de type alias
T 
```
T = TypeVar('T', int, float, complex)
```


## Classes

- https://mypy.readthedocs.io/en/latest/class_basics.html


# Covariance and contravariance
Consider a class Employee with a subclass Manager. Now suppose we have a function with an argument annotated with List[Employee]. Should we be allowed to call this function with a variable of type List[Manager] as its argument? Many people would answer "yes, of course" without even considering the consequences. But unless we know more about the function, a type checker should reject such a call: the function might append an Employee instance to the list, which would violate the variable's type in the caller.

It turns out such an argument acts contravariantly, whereas the intuitive answer (which is correct in case the function doesn't mutate its argument!) requires the argument to act covariantly. A longer introduction to these concepts can be found on Wikipedia [wiki-variance] and in PEP 483; here we just show how to control a type checker's behavior


# Referencia

- https://mypy.readthedocs.io/en/latest/kinds_of_types.html
