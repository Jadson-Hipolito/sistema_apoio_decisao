from pulp import LpMaximize, LpProblem, LpVariable, value

# Criar o problema de otimização
model = LpProblem(name="otimizacao-bolos", sense=LpMaximize)

# Variáveis de decisão
x = LpVariable(name="chocolate", lowBound=10, upBound=60, cat='Integer')  # chocolate
y = LpVariable(name="creme", lowBound=0, upBound=40, cat='Integer')       # creme

# Função objetivo: maximizar o lucro
model += 3 * x + 1 * y, "Lucro_total"

# Restrições
model += 2 * x + 3 * y <= 180, "Tempo_maquinario"  # tempo total
model += x + y >= 20, "Producao_minima"               # produção mínima

# Resolver o problema
model.solve()

# Resultados
print(f"Quantidade ideal de bolos de chocolate: {x.value()}")
print(f"Quantidade ideal de bolos de creme: {y.value()}")
print(f"Lucro total: R${value(model.objective)}")
