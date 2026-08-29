import sys

def ft_command_quest() -> None:
	print("command quest")
	program_name = sys.argv[0].split("/")[-1].split("\\")[-1]
	if len(sys.argv) == 1:
		print("No arguments provided")
		print(f"Program name: {program_name}")
	else:
		print(f"program name: {program_name}")
		print(f"arguments received: {len(sys.argv) -1}")
	i = 1
	while i < len(sys.argv)
		print(f"argument {i}: {sys.argv} - 1")
		i += 1
	print(f"total arguments: {len(sys.argv)}")

if __name__ == "__main__":
	ft_command_quest()