class Opponent:
    def __init__(self, name, health, power, fame_reward):
        self.name = name
        self.health = health
        self.max_health = health
        self.power = power
        self.fame_reward = fame_reward

opponents = [
    Opponent("Jobber", 50, 5, 5),
    Opponent("Tv Title Contender", 75, 10, 10),
    Opponent("US Title Contender", 100, 15, 15),
    Opponent("Main Event", 120, 20, 20),
    Opponent("WCW Heavyweight Champion", 150, 25, 50)
]

jobbers = [
    Opponent("Bobby Eaton", 50, 5, 5),
    Opponent("George South", 45, 4, 4),
    Opponent("Mike Thor", 55, 5, 5),
    Opponent("Mark Starr", 50, 5, 5),
    Opponent("Buddy Lee Parker", 60, 6, 6)
]

tv_title_contenders = [
    Opponent("Alex Wright", 70, 10, 10),
    Opponent("Lord Steven Regal", 75, 12, 12),
    Opponent("Johnny B. Badd", 80, 11, 11),
    Opponent("Disco Inferno", 70, 10, 10),
    Opponent("Diamond Dallas Page", 85, 13, 13)
]

us_title_contenders = [
    Opponent("Eddie Guerrero", 90, 15, 15),
    Opponent("Chris Benoit", 95, 16, 16),
    Opponent("Dean Malenko", 90, 15, 15),
    Opponent("Arn Anderson", 100, 17, 17),
    Opponent("Steve Austin", 100, 18, 18)
]

main_eventers = [
    Opponent("Sting", 120, 20, 25),
    Opponent("Ric Flair", 115, 19, 24),
    Opponent("Vader", 130, 22, 26),
    Opponent("Hulk Hogan", 125, 21, 25),
    Opponent("Randy Savage", 120, 20, 25)
]