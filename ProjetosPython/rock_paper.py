import random

def play():
    user = input("Escolha: 'P para pedra, 'PA' para papel , 'T' for tesoura\n")
    computer = random.choice(['P', 'PA', 'T'])

    if user == computer:
        return 'Deu empate!!'

    # r > s, s > p, p > r

    if is_win(user, computer):
        return 'Você ganhou!'

    if is_win(computer,user):
        return 'Você perdeu!'

def is_win(player, opponent):
    # retorna verdade se o player ganha

    if (player == 'P' and opponent == 'T') or (player == 'T' and opponent == 'PA')\
        or (player == 'PA' and opponent == 'P' ):
        return True

print(play())