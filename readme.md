# Processamento Paralelo com Python

## Objetivo

Este projeto compara o desempenho do processamento sequencial com o processamento paralelo na identificação de números primos.

## Tecnologias utilizadas

- Python 3.8.10
- Biblioteca multiprocessing
- Biblioteca time para medição do tempo
- Biblioteca statistics para cálculo das médias

## Como executar

1. Instale o Python 3.8 ou uma versão compatível.
2. Abra o terminal na pasta do projeto.
3. Execute:

   `py processamento_paralelo.py`

O programa realiza três execuções por configuração e calcula o tempo médio para cada uma.

## Resultados preliminares

O experimento foi realizado com números até 2.000.000.

- Processamento sequencial: 7,087 segundos em média.
- Paralelo com 1 processo: 6,954 segundos.
- Paralelo com 2 processos: 4,517 segundos.
- Paralelo com 4 processos: 3,795 segundos.

Todas as configurações encontraram 148.933 números primos.

Neste experimento, a configuração com quatro processos apresentou o menor tempo médio, com aceleração aproximada de 1,87 vezes em relação ao processamento sequencial.

## Evidências

As capturas de tela dos testes serão armazenadas na pasta `evidencias`.

## Código-fonte

Repositório: https://github.com/emersonsousa0/processamento-paralelo-python.git
