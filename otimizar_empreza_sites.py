from pulp import LpMaximize, LpProblem, LpVariable, value

# Criar o problema de otimização
model = LpProblem(name="empresa-de-sites", sense=LpMaximize)

# Variáveis de decisão
s1 = LpVariable(name="servico_completo", lowBound=0, cat='Integer')  # S1
s2 = LpVariable(name="reformulacao_site", lowBound=0, cat='Integer')  # S2

# Função objetivo: maximizar a arrecadação
model += 5000 * s1 + 4000 * s2, "Arrecadacao_total"

# Restrições
model += s1 + 2 * s2 <= 6, "Limite_horas_P2"
model += 6 * s1 + 4 * s2 <= 24, "Limite_horas_P1"
model += s2 - s1 <= 1, "Limite_diferenca_S2_S1"
model += s2 <= 2, "Maximo_S2_por_dia"

# Resolver o problema
model.solve()

# Resultados
print(f"Quantidade de serviços completos (S1): {s1.value()}")
print(f"Quantidade de reformulações de site (S2): {s2.value()}")
print(f"Arrecadação total: R${value(model.objective):,.2f}")
