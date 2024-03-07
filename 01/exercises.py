# Exercicio 01
def max_consecutive_sum(nums):

    soma_atual = 0
    soma_anterior = 0
    
    contas_realizadas = []
    
    for i in range(0, len(nums)):
        soma_atual = 0
        soma_anterior = 0
        for indice in range(i, len(nums)):
            
            print("Iteração ", i+indice)
            
            soma_anterior = soma_atual
            
            soma_atual += nums[indice]
            
            print("Somando: ", soma_anterior, " + ", soma_atual-soma_anterior, " = ", soma_atual)
            
            contas_realizadas.append(soma_atual)
            
            
    print(contas_realizadas)
    
    return max(contas_realizadas)
    

# Testes 01
def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3, '\n')
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, '\n')
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7, '\n')
    print(max_consecutive_sum([1]) == 1, '\n')
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1, '\n')


# Exercício 02
def is_palindrome(word):
    word = word.lower()
    word = word[::-1]
    print("\n",word)
    
    if word == word[::-1]:
        return True
    else:
        return False

# Testes 02
def text_is_palindrome():
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)


# Exercício 03
def count_increasing_subsets(nums):
    
    soma_atual = 0
    for indice1 in range(len(nums)):
        length = 1
        
        for indice2 in range(indice1 + 1, len(nums)):
            if nums[indice2] > nums[indice2 - 1]:
                length += 1
                
            else:
                break
            
        soma_atual += (length * (length + 1)) // 2
    print("\n", "Total de conjuntos: ", soma_atual)
    return soma_atual



# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)



# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
