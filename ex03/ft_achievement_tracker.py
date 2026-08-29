def unique_achievements(player1: set, player2: set, player3: set, player4: set) -> None:
	unique_ach = player1.union(player2, player3, player4)
	print(f"all unique achievements: {unique_ach}")
	total = 0
	for _ in unique_ach:
		total += 1
	print(f"total unique achievements: {total}\n")

def rare_achievements(player1: set, player2: set, player3: set, player4: set) -> None:
	rare_player1 = player1.difference(player2.union(player3))
	rare_player1 = player1.difference(player2.union(player3))
	rare_player1 = player1.difference(player2.union(player3))
	rare_player1 = player1.difference(player2.union(player3))
	rare_ach = rare_player1.union(rare_player2, rare_player3, rare_player4)
	print(f"rare achievements (1 player): {rare_ach}\n")

def ft_achievement_tracker() -> None:
	lia = {'first_kill', 'level_15', 'treasure_hunter', 'speed_demon'}
	mary = {'first_kill', 'level_9', 'boss_slayer', 'collector'}
	ane = {'first_kill', 'level_9', 'boss_slayer', 'collector'}
	mini = {'level_10', 'treasure_hunter', 'boss_slayer',
			   'speed_demon', 'perfectionist'}

	print("Achievement Tracker System\n")
	print(f"Player lia achievements: {lia}")
	print(f"Player mary achievements: {mary}")
	print(f"Player ane achievements: {ane}")
	print(f"Player mini achievements: {mini}\n")

	print("Achievement Analytics")
	unique_achievements(lia, mary, ane, mini)
	print(f"Common to all players: {lia.intersection(mary, ane, mini)}")
	rare_achievements(lia, mary, ane, mini)
	print(f"lia vs Bob ane: {lia.intersection(ane)}")
	print(f"lia unique: {lia.difference(ane)}")
	print(f"ane unique: {ane.difference(lia)}")
	
if __name__ == "__main__":
	ft_achievement_tracker()