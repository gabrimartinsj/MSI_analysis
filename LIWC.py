import re
import liwc
from collections import Counter
import matplotlib.pyplot as plt

def tokenize(text):
    # você pode querer usar um tokenizador mais inteligente
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)

def read_text_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

parse, category_names = liwc.load_token_parser('LIWC2007_portugues_win.txt')

# Ler os dados de um arquivo CSV
file_path = "youtube_data_messages.csv"
text = read_text_from_csv(file_path)
text = text.lower()  # Transforma o texto em minúsculas

# Tokenize o texto
tokenized_text = tokenize(text)

# Contagem das categorias de LIWC nos textos
text_counts = Counter(category for token in tokenized_text for category in parse(token))

# Dados da contagem das categorias
categorias = list(text_counts.keys())
contagens = list(text_counts.values())

# Criar gráfico de barras
plt.figure(figsize = (10, 6))
plt.bar(categorias, contagens, color = 'skyblue')
plt.xlabel('Categorias')
plt.ylabel('Contagem')
plt.title('Distribuição de Categorias Linguísticas')
plt.xticks(rotation = 90)
plt.show()

