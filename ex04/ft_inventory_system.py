import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    inv: dict[str, int] = {}

    for i in range(1, len(sys.argv)):
        arg: str = sys.argv[i]
        parts: list[str] = arg.split(':')

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name: str = parts[0]
        if name in inv:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty: int = int(parts[1])
            inv.update({name: qty})
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    if not inv:
        return

    print(f"Got inventory: {inv}")
    item_list: list[str] = list(inv.keys())
    print(f"Item list: {item_list}")

    total: int = sum(inv.values())
    print(f"Total quantity of the {len(item_list)} items: {total}")

    for key, val in inv.items():
        pct: float = (val / total) * 100 if total > 0 else 0.0
        print(f"Item {key} represents {round(pct, 1)}%")

    most_abundant_item: str = max(inv, key=inv.get)  # type: ignore
    least_abundant_item: str = min(inv, key=inv.get) # type: ignore

    print(f"Item most abundant: {most_abundant_item} with quantity {inv[most_abundant_item]}")
    print(f"Item least abundant: {least_abundant_item} with quantity {inv[least_abundant_item]}")

    inv.update({'magic_item': 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    ft_inventory_system()
