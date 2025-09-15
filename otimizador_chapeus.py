from pulp import LpMaximize, LpProblem, LpVariable, value

# Criar o problema de otimização
model = LpProblem(name="otimizacao-bolos", sense=LpMaximize)

# Variáveis de decisão
x = LpVariable(name="cowboy americano", lowBound=0, upBound=150, cat='Integer')  # CA
y = LpVariable(name="sertanejo brasileiro", lowBound=0, upBound=200, cat='Integer')  # SB

# Função objetivo: maximizar o lucro
model += 8 * x + 5 * y, "Lucro_total"

# Restrições
model += 2 * x + 1 * y <= 400, "Mão_de_obra"  # mão de obra disponivel


# Resolver o problema
model.solve()

# Resultados
print(f"Quantidade ideal de chapeus cowboy americano: {x.value()}")
print(f"Quantidade ideal de chapeus sertanejo brasileiro: {y.value()}")
print(f"Lucro total: R${value(model.objective)}")
