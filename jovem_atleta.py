from pulp import LpMaximize, LpProblem, LpVariable, value

# Criar o problema de otimização
model = LpProblem(name="jovem-atleta", sense=LpMaximize)

# Variáveis de decisão
x = LpVariable(name="natação", lowBound=1, upBound=9, cat='Integer')  # chocolate
y = LpVariable(name="ciclismo", lowBound=1, upBound=9, cat='Integer')       # creme

# Função objetivo: maximizar a quantidade de sessões
model += x + y, "sessões_totais"

# Restrições
model += 3 * x + 2 * y <= 70, "Gasto_maximo"  # valor total
model += 2 * x + 2 * y >= 18, "Tempo_maximo"  # tempo disponivel

# Resolver o problema
model.solve()

# Resultados
print(f"Quantidade de sessões de natação: {x.value()}")
print(f"Quantidade de sessões de ciclismo: {y.value()}")
