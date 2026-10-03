import random


def gen_player_achievements(all_achievs: list[str]) -> set[str]:
    # Pega um tamanho aleatório entre 2 e o máximo de conquistas
    amount: int = random.randint(2, len(all_achievs))
    # Pega 'amount' conquistas aleatórias sem repetir
    chosen: list[str] = random.sample(all_achievs, amount)
    return set(chosen)


def ft_achievement_tracker() -> None:
    all_achievs: list[str] = [
        'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
        'Untouchable', 'Boss Slayer', 'Strategist', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'Unstoppable', 'First Steps', 'Sharp Mind'
    ]

    print("=== Achievement Tracker System ===")

    p1: set[str] = gen_player_achievements(all_achievs)
    p2: set[str] = gen_player_achievements(all_achievs)
    p3: set[str] = gen_player_achievements(all_achievs)
    p4: set[str] = gen_player_achievements(all_achievs)

    print(f"Player Alice: {p1}")
    print(f"Player Bob: {p2}")
    print(f"Player Charlie: {p3}")
    print(f"Player Dylan: {p4}\n")

    # Todos os sets juntos
    all_distinct: set[str] = p1.union(p2).union(p3).union(p4)
    print(f"All distinct achievements: {all_distinct}")

    # O que todos os 4 têm em comum
    common: set[str] = p1.intersection(p2).intersection(p3).intersection(p4)
    print(f"Common achievements: {common}\n")

    # Conquistas que SÓ aquela pessoa tem
    print(f"Only Alice has: {p1.difference(p2.union(p3).union(p4))}")
    print(f"Only Bob has: {p2.difference(p1.union(p3).union(p4))}")
    print(f"Only Charlie has: {p3.difference(p1.union(p2).union(p4))}")
    print(f"Only Dylan has: {p4.difference(p1.union(p2).union(p3))}\n")

    # O que falta para a pessoa ter TUDO
    print(f"Alice is missing: {set(all_achievs).difference(p1)}")
    print(f"Bob is missing: {set(all_achievs).difference(p2)}")
    print(f"Charlie is missing: {set(all_achievs).difference(p3)}")
    print(f"Dylan is missing: {set(all_achievs).difference(p4)}")


if __name__ == "__main__":
    ft_achievement_tracker()
