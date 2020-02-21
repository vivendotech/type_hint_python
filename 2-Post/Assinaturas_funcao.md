# Assinatura de funções para tipos basicos concretos.
Os tipos básicos primitivos são: int, float, str, bool, complex e o None.

Breve explicação de cada tipo. 

Ele chama de Built-in types
```python
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
# Conferir 
x: None = None
x: complex = 1+1j
```


A assinatura da função que diz quais tipos os parametros deveriam ser.
No exemplo do post1 (colocar o link), o parametro "nome" deveria ser do tipo String (uma palavra) e a função deveria retornar um String (palavra).

```python
    nome_fun(par: tipo_parametro) -> tipo_saida
def greeting(name: str) -> str:

```
Para adicionar uma dica de tipo é colocado o tipo depois do nome da variaver o :. E para adicionar a dica de tipo do que deveria sair da função é posta depois do sinal de "->" na definição da função. Vale lembrar, que os parametros da função são dividos por virgula.


# Adicionando eles na assinatura da função.


## Sintaxe Type Hint junto a um valor padrão

```python
def greeting(name: str = "joão") -> str:
```

## Sintaxe para a assinatura de nenhuma variavel e de retorno None

```Python
def greeting() -> None:
```


# This is how you annotate a function definition
```python
def stringify(num: int) -> str:
    return str(num)
```

# And here's how you specify multiple arguments
```python
def plus(num1: int, num2: int) -> int:
    return num1 + num2
```

# Add default value for an argument after the type annotation
```python
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float
```


# É possivel depois do 3.6 assinar variaveis

A sintaxe para assinar variaveis é bem parecida com as funções mas nelas não se adiciona o que elas retornam.
```
x: int = 2
```

# Proximo
So far, we’ve added type hints that use only basic concrete types like str and float. What if we want to express more complex types, such as “a list of strings” or “an iterable of ints”

# Tipos provenientes da biblioteca adicionada.

- https://mypy.readthedocs.io/en/latest/getting_started.html 