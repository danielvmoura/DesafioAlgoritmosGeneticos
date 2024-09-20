import numpy as np
import random

# Função f(x) = x^3 - 6x + 14
def f(x):
    return x**3 - 6*x + 14

# Decodifica o binário para o valor de x, garantindo que esteja entre lower_bound e upper_bound
def decode(binary, lower_bound, upper_bound, num_bits):
    max_value = 2**num_bits - 1  # O maior valor representável com num_bits bits
    decimal_value = int(''.join(str(int(b)) for b in binary), 2)  # Convertendo binário para decimal
    # Escalar o valor decimal para o intervalo [lower_bound, upper_bound]
    return lower_bound + (upper_bound - lower_bound) * decimal_value / max_value

# Gera população inicial
def initialize_population(pop_size, num_bits):
    return [np.random.randint(0, 2, num_bits).tolist() for _ in range(pop_size)]

# Crossover de 1 ou 2 pontos
def crossover(parent1, parent2, num_points=1):
    if num_points == 1:
        point = random.randint(1, len(parent1)-2)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    elif num_points == 2:
        point1, point2 = sorted(random.sample(range(1, len(parent1)-1), 2))
        return (parent1[:point1] + parent2[point1:point2] + parent1[point2:], 
                parent2[:point1] + parent1[point1:point2] + parent2[point2:])

# Mutação
def mutate(individual, mutation_rate):
    return [1 - bit if random.random() < mutation_rate else bit for bit in individual]

# Seleção por torneio
def tournament_selection(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    return max(selected, key=lambda x: x[1])[0]

# Função principal do algoritmo genético que retorna array de arrays
def genetic_algorithm(pop_size=10, num_bits=16, generations=2, crossover_points=1, 
                      mutation_rate=0.01, elitism=False, elite_pct=0.1, lower_bound=-10, upper_bound=10):
    # População inicial
    population = initialize_population(pop_size, num_bits)
    
    # Array de arrays para armazenar resultados (soma dos itens e o array de bits)
    results = []

    for gen in range(generations):
        # Decodificar indivíduos e calcular aptidão (fitness)
        decoded = [decode(ind, lower_bound, upper_bound, num_bits) for ind in population]
        fitnesses = [-f(x) for x in decoded]  # Invertendo para minimizar a função
        
        # Elitismo
        if elitism:
            num_elites = int(elite_pct * pop_size)
            elites = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)[:num_elites]
            elites = [elite[0] for elite in elites]
        
        # Nova população
        new_population = []
        
        while len(new_population) < pop_size:
            # Seleção dos pais
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            
            # Crossover
            offspring1, offspring2 = crossover(parent1, parent2, crossover_points)
            
            # Mutação
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            
            new_population.append(offspring1)
            if len(new_population) < pop_size:
                new_population.append(offspring2)
        
        # Substituir população antiga
        if elitism:
            new_population[:num_elites] = elites
        
        population = new_population
        
        # Salvar os resultados de cada geração no formato: [soma, [array de bits]]
        for ind in population:
            decoded_value = decode(ind, lower_bound, upper_bound, num_bits)
            results.append([f(decoded_value), ind])
        
    # Retornar array de arrays com os resultados
    return results

# Executar algoritmo genético
resultados = genetic_algorithm()

# Exibir resultados
for resultado in resultados:
    print(f"[{resultado[0]:.3f}, {resultado[1]}]")
