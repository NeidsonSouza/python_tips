symbols = 'aeiou'

def my_filter(argument):
    return argument

print(list(map(my_filter, symbols))) # returna a saída exata da função
print(list(filter(my_filter, symbols))) # retorna bool(saida da função)
