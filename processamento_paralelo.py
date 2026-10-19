
import multiprocessing
import time
import math
import statistics


def eh_primo(numero):
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = math.isqrt(numero)

    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False

    return True


def contar_primos(inicio, fim):
    quantidade = 0

    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            quantidade += 1

    return quantidade


def executar_sequencial(limite):
    inicio_tempo = time.perf_counter()

    quantidade = contar_primos(2, limite)

    tempo = time.perf_counter() - inicio_tempo

    return quantidade, tempo


def executar_paralelo(limite, processos):
    total_numeros = limite - 1
    tamanho = (total_numeros + processos - 1) // processos
    tarefas = []

    for i in range(processos):
        inicio = 2 + i * tamanho
        fim = min(limite, inicio + tamanho - 1)

        if inicio <= limite:
            tarefas.append((inicio, fim))

    inicio_tempo = time.perf_counter()

    with multiprocessing.Pool(processes=processos) as pool:
        resultados = pool.starmap(contar_primos, tarefas)

    tempo = time.perf_counter() - inicio_tempo

    return sum(resultados), tempo


if __name__ == "__main__":
    LIMITE = 2_000_000
    REPETICOES = 3
    CONFIGURACOES = [1, 2, 4]

    resultados = {}

    print("=" * 55)
    print(" EXPERIMENTO DE PROCESSAMENTO PARALELO")
    print("=" * 55)
    print(f"Limite: {LIMITE:,}")
    print(f"Repeticoes por configuracao: {REPETICOES}")
    print()

    # Referencia: processamento sequencial
    tempos_seq = []
    quantidade_seq = None

    print("PROCESSAMENTO SEQUENCIAL")

    for tentativa in range(1, REPETICOES + 1):
        quantidade, tempo = executar_sequencial(LIMITE)
        tempos_seq.append(tempo)
        quantidade_seq = quantidade

        print(f"Teste {tentativa}: {tempo:.3f} segundos")

    media_seq = statistics.mean(tempos_seq)
    resultados["Sequencial"] = (quantidade_seq, media_seq)

    print(f"Media sequencial: {media_seq:.3f} segundos")
    print()

    # Testes paralelos com 1, 2 e 4 processos
    for processos in CONFIGURACOES:
        tempos = []
        quantidade_par = None

        print(f"PROCESSAMENTO COM {processos} PROCESSO(S)")

        for tentativa in range(1, REPETICOES + 1):
            quantidade, tempo = executar_paralelo(
                LIMITE, processos
            )

            tempos.append(tempo)
            quantidade_par = quantidade

            print(f"Teste {tentativa}: {tempo:.3f} segundos")

        media = statistics.mean(tempos)
        resultados[f"{processos} processo(s)"] = (
            quantidade_par, media
        )

        print(f"Media: {media:.3f} segundos")
        print()

    # Comparacao final
    print("=" * 55)
    print("RESUMO DOS RESULTADOS")
    print("=" * 55)

    for nome, (quantidade, media) in resultados.items():
        aceleracao = media_seq / media

        print(f"\n{nome}")
        print(f"Numeros primos: {quantidade}")
        print(f"Tempo medio: {media:.3f} segundos")
        print(f"Aceleracao vs. sequencial: {aceleracao:.2f}x")

        if quantidade != quantidade_seq:
            print("ATENCAO: quantidade diferente da referencia!")

    print("\nExperimento concluido.")
