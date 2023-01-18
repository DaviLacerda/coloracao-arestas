# Coloração de Arestas 

## Alunos

* Davi Tobias Lacerda
* Victor Hugo Nunes Alves

## Step by step

### 1º Passo) Instalar o software Máxima

* Acesse o site do [Maxima](https://maxima.sourceforge.io/download.html) e instale o software

### 2º Passo) Criação do grafo com base no arquivo graph.txt

* O arquivo segue o padrão DIMACS:
```
    c graph exported from MAXIMA
    p edge n m
    e ki kj
```

* Legenda:
    * n : número de vértices no grafo
    * m : número de arestas no grafo
    * e : adição de uma aresta (*ki*, *kj*) entre os vértices *ki* e *kj*
    * ki : vértice 1
    * kj : vértice 2

### 3º Passo) Execute o arquivo maxima.txt dentro do Software

* Para executar o arquivo, abre ele e clique no botão indicado pela seta
![Botão de execução no Software](https://github.com/DaviLacerda/coloracao-arestas/blob/main/images/run_file.jpg)

### 4º Passo) Resultados

* Ao executar o código, será mostrado o índice cromático, além de uma imagem do grafo montado, já com as arestas coloridas (respeitando as regras de coloração própria)
![Execução do código](https://github.com/DaviLacerda/coloracao-arestas/blob/main/images/graph_example.png)