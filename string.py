example = "Топинамбуры" #
print(example[0]) # 1й символ
print(example[-1]) # последний символ
#####
print(len(example)) # длина строки
dlinna_str = len(example) //2 # половина строки чтобы без остатка
print(dlinna_str)
print(example[0:dlinna_str]) # первая половина
print(example[dlinna_str:]) # вторая половина
#####
print(example[len(example)//2:]) # вторая половина
#####
print(example[5:]) # вторая половина
print(example[::-1]) # слово наоборот
 # если с индекса[0] то всегда с 1го символа будет начитать Т
## Пример: 'Топинамбур'->'оиабр' здесь не берется 1й символ
print(example[1::2]) # каждый 2й (значит начал со 2го символа с индекса[1]) Т пропустит
