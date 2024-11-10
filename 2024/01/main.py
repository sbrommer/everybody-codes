def chunked(xs, n):
    return [xs[i:i+n] for i in range(0, len(xs), n)]


def fight(team):
    potions = {'A': 0, 'B': 1, 'C': 3, 'D': 5}

    team = team.replace('x', '')

    total = sum(map(potions.get, team))
    teambonus = {0: 0, 1: 0, 2: 2, 3: 6}[len(team)]

    return total + teambonus


def fight_teams(teams, len_team):
    return sum(map(fight, chunked(teams, len_team)))


teams = input()

for part in [1, 2, 3]:
    print(f'Part {part}: {fight_teams(teams, part)}')
