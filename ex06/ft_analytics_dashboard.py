import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")

    initial: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial}\n")

    # Lista 1: Todos com letra maiúscula (mapeamento)
    cap_all: list[str] = [name.capitalize() for name in initial]
    print(f"New list with all names capitalized: {cap_all}\n")

    # Lista 2: Filtrando apenas os que já vieram com letra maiúscula (filtro)
    cap_only: list[str] = [name for name in initial if name[0].isupper()]
    print(f"New list of capitalized names only: {cap_only}\n")

    # Dict 1: Criação de chaves a partir de nomes e valores randômicos para os scores
    scores: dict[str, int] = {name: random.randint(0, 1000) for name in cap_all}
    print(f"Score dict: {scores}\n")

    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    # Dict 2: Filtrando um dicionário a partir de outro usando as chaves e valores (k, v)
    high: dict[str, int] = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high}")


if __name__ == "__main__":
    ft_data_alchemist()
