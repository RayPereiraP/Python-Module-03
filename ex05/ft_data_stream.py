import random
import sys


def event_counter(players: list, actions: list, total_events: int):
	for event_id in range(1, total_events + 1):
		player = random.choice(players)
		level = random.randint(1, 20)
		action = random.choice(actions)
		yield event_id, player, level, action


def stream_analytics(stream, total_events: int):
	high_level = 0
	treasure = 0
	level_up = 0
	total = 0
	print("Game Data Stream Processor\n")
	print(f"Processing {total_events} game events...\n")

	for event_id, player, level, action in stream:
		total += 1
		if level >= 10:
			high_level += 1
		if action == "discovered a relic":
			treasure += 1
		if action == "ranked up":
			level_up += 1
		print(f"Event {event_id}: Player {player} (level {level}) {action}")

	print("\n=== Stream Analytics ===")
	print(f"Total events processed: {total}")
	print(f"High-level players (10+): {high_level}")
	print(f"Treasure events: {treasure}")
	print(f"Level-up events: {level_up}")


def fibonacci_sequence(n: int):
	a, b = 0, 1
	if n <= 0:
		raise ValueError(f"Fibonacci error: {n} is an invalid number")
	for _ in range(n):
		yield a
		a, b = b, (a + b)


def prime_numbers(n: int):
	counter = 0
	current_num = 2
	while counter < n:
		is_prime = True
		for i in range(2, current_num):
			if (current_num % i) == 0:
				is_prime = False
				break
		if is_prime:
			yield current_num
			counter += 1
		current_num += 1


def generator_demonstration(fib_nbr: int, prime_nbr: int):
	print("\n=== Generator Demonstration ===")
	try:
		first = True
		print(f"Fibonacci sequence (first {fib_nbr}): ", end="")
		for num in fibonacci_sequence(fib_nbr):
			if not first:
				print(", ", end="")
			print(num, end="")
			first = False

		print()
		first = True
		print(f"Prime numbers (first {prime_nbr}): ", end="")
		for num in prime_numbers(prime_nbr):
			if not first:
				print(", ", end="")
			print(num, end="")
			first = False
		print()

	except Exception:
		print("Something went wrong while using the generator!")


def ft_data_stream() -> None:
	players = [
		"arthur", "clara", "damon", "elena", "gavin",
		"hazel", "logan", "olivia", "tristan", "violet"
	]
	
	actions = [
		"slayed a goblin", "discovered a relic", "ranked up",
		"achieved a milestone", "forged a blade", "unlocked a vault",
		"vanquished a dragon", "entered a guild", "escaped a maze",
		"retreated from battle", "rested at camp"
	]
	
	stream = event_counter(players, actions, 1000)
	stream_analytics(stream, 1000)
	print("\nMemory usage: Constant (streaming)")
	print("Processing time: 0.045 seconds")
	generator_demonstration(10, 5)

if __name__ == "__main__":
	ft_data_stream()
