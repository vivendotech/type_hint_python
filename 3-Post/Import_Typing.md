
Importando o modulo Typing. O modulo Typing permite expandir a capacidade do que se pode anotar no código do python. Adicionando mais tipos.

# Anotando estruturas de dados

## Anotando Listas
```python
from typing import List
def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
greet_all(ages)    # Error due to incompatible types
```

## Anotando Conjunto
```python
from typing import List, Set, Dict, Tuple
x: Set[int] = {6, 7}
```


## Anotando Dicionarios
# For mappings, we need the types of both keys and values
```python
from typing import List, Set, Dict, Tuple

x: Dict[str, float] = {'field': 2.0}
```



## Anotando Tuplas.

Tuplas de tamanhao fixo e de tamanho variavel


### For tuples of fixed size, we specify the types of all the elements

```python
from typing import List, Set, Dict, Tuple, Optional

x: Tuple[int, str, float] = (3, "yes", 7.5)
```


### For tuples of variable size, we use one type and ellipsis

```python
from typing import List, Set, Dict, Tuple, Optional

x: Tuple[int, ...] = (1, 2, 3)
```


## Iterable
Algo que possa ser iterado
```python
from typinmg import Iterable

def f(ints: Iterable[int]) -> List[str]:
    return [str(x) for x in ints]

```



# Outros typing importantes





## Union
Unindo dois tipos, que o parametro pode ser qualquer um dos tipso dentro da union.
```python
from typing import Union
def send_email(address: Union[str, List[str]]) -> None:

```


## Optional

Option é um tipo especial de União (união), sendo que sempre é entre o tipo definido e o tipo None.

```python
from typing import Optional
# Use Optional[] for values that could be None
x: Optional[str] = some_function()
```

## Any
Um caso mais especial é quando é a união entre todos os tipos, geralmente usado quando vc nao sabe que tipo é a variabel.
Para qualquer tipo use Any.


A value with the Any type is dynamically typed. Mypy doesn’t know anything about the possible runtime types of such value. Any operations are permitted on the value, and the operations are only checked at runtime. You can use Any as an “escape hatch” when you can’t use a more precise type for some reason.


```python
from typing import Any
# Use Any if you don't know the type of something or it's too dynamic to write a type for
x: Any = mystery_function()
```



# Anotando Funções como argumentos
O entre colchetes são os parametros da funcao [int, float], significa qu eo primeiro parametro deve ser um inteiro e o segundo parametro um float. Depois da virgula é o que a função retorna
```python
from typing import Callable
# a entrada da funcao é uma variavel itneira e outra float, a saida é um float e ela ta sendo atribuida a funcao f (o = f ).
x: Callable[[int, float], float] = f

# a entrada da funcao deve ser um inteiro ela deve retornar um inteiro
def twice(i: int, next: Callable[[int], int]) -> int:
    return next(next(i))

def add(i: int) -> int:
    return i + 1

print(twice(3, add))   # 5
```
## Funcoes
It is possible to declare the return type of a callable without specifying the call signature by substituting a literal ellipsis (three dots) for the list of arguments:

```python
# os ... significao que nao esta especificado a quantidade ou o tipo de parametro que a funcao deve possuir.
def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    # Body
```




# Criando seus própios tipos.

# Referencia

- https://mypy.readthedocs.io/en/latest/getting_started.html 
- https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html#cheat-sheet-py31
- https://mypy.readthedocs.io/en/latest/kinds_of_types.html