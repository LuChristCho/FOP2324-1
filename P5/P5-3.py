class Troop:
    troop_ids = []

    def __init__(self, troop_type, troop_id, x, y):
        self.troop_type = troop_type
        self.troop_id = troop_id
        self.health = 100
        self.x = x
        self.y = y
        Troop.troop_ids.append(self.troop_id)

class ArcherTroop(Troop):
    def __init__(self, troop_id, x, y):
        super().__init__("archer", troop_id, x, y)

class MeleeTroop(Troop):
    def __init__(self, troop_id, x, y):
        super().__init__("melee", troop_id, x, y)

class GameBoard:
    def __init__(self, n):
        self.positions = {0: {}, 1: {}}
        self.players = {0: [], 1: []}
        self.current_turn = 0
        self.n = n

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def add_troop(self, troop_type, troop_id, x, y):
        player_ids = [i.troop_id for i in self.players[self.current_turn]]
        if troop_id in player_ids:
            print("duplicate tag")
            return

        if (x, y) not in self.positions[self.current_turn]:
            self.positions[self.current_turn][(x, y)] = []

        if troop_type == "archer":
            troop = ArcherTroop(troop_id, x, y)
        elif troop_type == "melee":
            troop = MeleeTroop(troop_id, x, y)
        else: 
            print("Invalid troop type")
            return

        self.positions[self.current_turn][(x, y)].append(troop)
        self.players[self.current_turn].append(troop)
        self.switch_turn()

    def move_troop(self, troop_id, direction):
        troop = self.find_troop(troop_id)

        if troop is not None:
            old_position = (troop.x, troop.y)

            if direction == "up":
                new_x, new_y = troop.x, troop.y-1
            elif direction == "down":
                new_x, new_y = troop.x, troop.y+1
            elif direction == "left":
                new_x, new_y = troop.x-1, troop.y
            elif direction == "right":
                new_x, new_y = troop.x+1, troop.y 
            else:
                print("Invalid direction")
                return

            if not (0 <= new_x < self.n and 0 <= new_y < self.n):
                print("out of bounds")
                return

            self.positions[self.current_turn][old_position].remove(troop)

            if (new_x, new_y) not in self.positions[self.current_turn]:
                self.positions[self.current_turn][(new_x, new_y)] = []
            self.positions[self.current_turn][(new_x, new_y)].append(troop)

            troop.x = new_x
            troop.y = new_y

            self.switch_turn()
            return
        else:
            print("troop does not exist")
            return
        
    
    def attack(self, attacker_id, target_id):
        attacker = self.find_troop_for_attack(attacker_id, "attacker")
        target = self.find_troop_for_attack(target_id, "defender")

        if attacker is None or target is None:
            return
        if isinstance(attacker, ArcherTroop):
            if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 2:
                 print("the target is too far")
                 return
            target.health -= 10
        elif isinstance(attacker, MeleeTroop):
            if self.calculate_distance(attacker.x, attacker.y, target.x, target.y) > 1:
                 print("the target is too far")
                 return
            target.health -= 20

        if target.health <= 0:
            print("target eliminated")
            target_position = (target.x, target.y)
            if target_position in self.positions[1 - self.current_turn]:
                if target in self.positions[1 - self.current_turn][target_position]:
                    self.positions[1 - self.current_turn][target_position].remove(target)
            if target in self.players[1 - self.current_turn]:
                self.players[1 - self.current_turn].remove(target)
        self.switch_turn()
        return

    def get_info(self, troop_id):
        troop = self.find_troop(troop_id)
        if troop is None:
            print("troop does not exist")
            return

        print(f"health:  {troop.health}")
        print(f"location:  {troop.x}   {troop.y}") 
        self.switch_turn()
        return

    def who_is_in_lead(self):
        score = {0: 0, 1: 0}
        for player, troops in self.players.items():
            for troop in troops:
                score[player] += troop.health

        if score[0] > score[1]:
            print("player 1")
        elif score[0] < score[1]:
            print("player 2")
        else:
            print("draw")

    def find_troop(self, troop_id):
        for troops_list in self.positions[self.current_turn].values():
            for troop in troops_list:
                if troop.troop_id == troop_id:
                    return troop

    def find_troop_for_attack(self, troop_id, whois):
        if whois == "attacker":
            for troops_list in self.positions[self.current_turn].values():
                for troop in troops_list:
                    if troop.troop_id == troop_id:
                        return troop
        else:
            for troops_list in self.positions[1 - self.current_turn].values():
                for troop in troops_list:
                    if troop.troop_id == troop_id:
                        return troop
        print("troop does not exist")
        return None

    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

n = int(input())
game = GameBoard(n)
commands = []
while True:
    try:
        line = input().split(" ")
        if 'end' in line:
            break
        commands.append(line)
    except EOFError:
        break
pointer = 0
while True:
    if pointer == len(commands):
        break
    command = commands[pointer]
    if command[0] == "new":
        game.add_troop(command[1], int(command[2]), int(command[3]), int(command[4]))
    elif command[0] == "move":
        game.move_troop(int(command[1]), command[2])
    elif command[0] == "attack":
        game.attack(int(command[1]), int(command[2]))
    elif command[0] == "info":
        game.get_info(int(command[1]))
    elif command[0] == "who":
        game.who_is_in_lead()
    pointer += 1
