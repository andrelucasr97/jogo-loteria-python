#  Jogo de Adivinhação em Python

Este é um projeto simples feito em **Python** onde o usuário precisa adivinhar um número sorteado pelo programa.

O jogo sorteia um número entre **1 e 10**, e o usuário tem **3 tentativas** para acertar.

Durante o jogo, o programa informa se o número digitado é **maior ou menor** que o número sorteado.

---

##  Funcionalidades

* Sorteio de número aleatório usando a biblioteca `random`
* Validação de entrada do usuário
* Tratamento de erros com `try` e `except`
* Sistema de tentativas limitadas
* Dicas para ajudar o usuário (maior ou menor)

---

##  Conceitos de Python utilizados

Este projeto utiliza conceitos importantes da linguagem:

* Funções (`def`)
* Loops (`for` e `while`)
* Condicionais (`if`, `elif`, `else`)
* Tratamento de exceções (`try` e `except`)
* Biblioteca padrão (`random`)
* Validação de entrada do usuário

---

##  Estrutura do Projeto

```
projeto-adivinhacao/
│
├── main.py
└── README.md
```

---

##  Como executar o projeto

1. Clone este repositório:

```
git clone https://github.com/andrelucasr97/jogo-loteria-python.git
```

2. Acesse a pasta do projeto:

```
cd nome-do-repositorio
```

3. Execute o arquivo Python:

```
python main.py
```

---

##  Como jogar

1. O programa sorteia um número entre **1 e 10**.
2. Você deve digitar um número dentro desse intervalo.
3. O jogo informará se o número sorteado é **maior ou menor**.
4. Você tem **3 tentativas** para acertar.

Se acertar, você vence! 
Se errar todas as tentativas, o jogo termina.

---

##  Exemplo de execução

```
Digite um número entre 1 e 10: 7
O número sorteado é menor do que o número digitado.

Digite um número entre 1 e 10: 4
O número sorteado é maior do que o número digitado.

Digite um número entre 1 e 10: 5
Parabéns, você acertou o número!
```

---

## 👨‍💻 Autor

Projeto desenvolvido para prática de **Python e lógica de programação**.
