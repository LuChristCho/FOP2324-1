'''import matplotlib.pyplot as plt'''

def create_dict_from_list(numbers):
    if len(numbers) != 3:
        raise ValueError("Invalid Command.")

    return {"A": numbers[0], "B": numbers[1], "C": numbers[2]}

def play_game(player1, player2, health1, health2, damages, rounds):
    score1 = 0
    score2 = 0
    scores1 = []
    scores2 = []

    for i in range(rounds):
        card1, card2 = input().split()

        damage1 = damages[card1]
        damage2 = damages[card2]
        health2 -= damage1
        health1 -= damage2

        if damage1 > damage2:
            score1 += 1
        elif damage2 > damage1:
            score2 += 1
    
        scores1.append(score1)
        scores2.append(score2)

    '''with open('C:/Users/pc/Desktop/maram/result.txt', 'w') as file:
        file.write(f"{player1} -> Score: {score1}, Health: {health1}\n")
        file.write(f"{player2} -> Score: {score2}, Health: {health2}\n")

    
    plt.bar([player1, player2], [score1, score2])
    plt.xlabel('Players')
    plt.ylabel('Scores')
    plt.title('Game Results')
    plt.show()'''
            
    print(f"{player1} -> Score: {score1}, Health: {health1}")
    print(f"{player2} -> Score: {score2}, Health: {health2}")

try:
    player1, player2 = input().split()
    health1, health2 = map(int, input().split())
    damages = create_dict_from_list(list(map(int, input().split())))

    play_game(player1, player2, health1, health2, damages, 3)
except Exception as e:
    print("Invalid Command.")
