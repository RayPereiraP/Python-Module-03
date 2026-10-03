import random
import typing

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    # Cria um loop infinito produzindo (nome, acao)
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(lst: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    # Esvazia a lista escolhendo itens de forma aleatória até acabar
    while len(lst) > 0:
        idx: int = random.randrange(len(lst))
        yield lst.pop(idx)


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    # Usamos o _ porque a variável i não é usada dentro do loop
    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    # Cria a lista de 10 chamando next 10 vezes
    event_list: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}\n")

    for ev in consume_event(event_list):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
