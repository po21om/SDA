class FootballGame:
    def __init__(self, name, city):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append((team))

    def play(self):
        number_of_teams = len(self.teams)
        if number_of_teams != 2:
            return None
        else:
            return self.teams[0]

    def end_game(self):
        print("Gra się skończyła. Można iść do domu!")