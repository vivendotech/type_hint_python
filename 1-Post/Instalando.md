# Instalando o Type Hint
Para poder usar o Type Hint é necessário ter a versão do Python igual ou maior a 3.5. E é necessáiro instalar o modulo do [Mypy](https://mypy.readthedocs.io/en/latest/)

```powershell
python -m pip install mypy
```

# Rodando o Mypy

Para rodar o mypy baixe o documento e execute a linha de comando no powershell do windows. (Falar como abrir o powershell do windows na pasta destino.)

```bash
mypy programa_baixado.py
# Success: no issues found in 1 source file
```
Caso teja instalado com sucesso ira aparecer a mensagem:"Success: no issues found in 1 source file" 

## Rodando o código no Python

# Adicionando erro para o TypeChecer
```python
greeting(10)
```
## Rodando o codigo, funciona normalente
```
py programa_baixado.py
Hello João
Hello 10
```
## Rodando o Mypy

```bash
mypy programa_baixado.py
# Found 1 error in 1 file (checked 1 source file)
```


## Programa continua executando mas o checker ve que tem um problema.

You can teach mypy to detect these kinds of bugs by adding type annotations (also known as type hints). For example, you can teach mypy that greeting both accepts and returns a string like so:

This function is now statically typed: mypy can use the provided type hints to detect incorrect usages of the greeting function. For example, it will reject the following calls since the arguments have invalid types:


## deixando a mensagem de erro mais verbosa


# Referencias

- https://mypy.readthedocs.io/en/latest/getting_started.html 