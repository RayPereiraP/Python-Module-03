import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw_input: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as e:
            # Pega a palavra errada que causou o problema e avisa o usuário
            bad_val = [p for p in parts if not p.strip().replace('.', '').isdigit()][0]
            print(f"Error on parameter '{bad_val.strip()}': {e}")


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    p1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist1: float = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist1, 4)}")

    print("\nGet a second set of coordinates")
    p2: tuple[float, float, float] = get_player_pos()

    dist_between: float = math.sqrt(
        (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    ft_coordinate_system()
