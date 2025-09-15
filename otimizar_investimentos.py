from pulp import LpMaximize, LpProblem, LpVariable, value

# Criar o problema de otimização
model = LpProblem(name="otimizacao-investimentos", sense=LpMaximize)

# Variáveis de decisão
x = LpVariable(name="cowboy americano", lowBound=0, upBound=5000, cat='Integer')  # CA
y = LpVariable(name="sertanejo brasileiro", lowBound=0, upBound=5000, cat='Integer')  # SB

# Função objetivo: maximizar o lucro
model += 0.05 * x + 0.08 * y, "Lucro_total"

# Restrições
model += x + y <= 5000, "Dinheiro_maximo"  # Dinheiro disponivel
model += x >= 1250, "Polpansa_minima_total"  # polpansa minima
model += y <= 2500, "Maximo_ações"  # maximo ações
model += x >= y/2, "Polpansa_minima_investimento"  # polpansa minima em relação ao investimento

# Resolver o problema
model.solve()

# Resultados
print(f"Dinheiro na poupansa: {x.value()}")
print(f"Dinheiro em Investimentos: {y.value()}")
print(f"Lucro total: R${value(model.objective)}")
