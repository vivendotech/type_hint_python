# o nome tem que ser do tipo String (Str) a saida tem que ser uma Str
def greeting(name: str) -> str:
    return 'Hello ' + str(name)

# Sucesso
print(greeting("Joao"))


# Causando uma falha no mypy
# print(greeting(10))


