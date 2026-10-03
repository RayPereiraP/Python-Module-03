import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")

    # sys.argv[0] é o nome do programa. Separamos barras caso venha um caminho longo.
    program_name: str = sys.argv[0].split('/')[-1].split('\\')[-1]
    print(f"Program name: {program_name}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
