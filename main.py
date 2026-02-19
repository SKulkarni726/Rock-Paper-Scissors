from random import choice

player_victory_ascii = r"""
            .oo.
          oGGGGGGo
         GGGGGGGGGG
  .mMMMMMMGGGGGGEEEE=
 MMMMMMMMMMMGGEEEEEEEE
MMMMMMMMMMMNICKEEEEEEEE
MMMMMMMMMMMMMEEEEEEEEEE
!MMMMMMMMMMMOOEEEEEEEE
 MMM!MMMMMMOOOOOOE!=
  MM!!!!!!!!!!!!!!!
   MM!!!!!!!!!!!!!'
   !M!!!!!!!!!!!!!
    MM!!!!!!!!!!!'
    MM!!!!!!!!!!!
    ! `!!!!!!!!!'
    .  !!!!!!!!!
       `!!!!!!!'
        !!!!!!!
        `!!!!!'
         !!!!!
         `!!!'
          !!!
          `!'
           !           (c) by Nick 30.09.96
"""

computer_victory_ascii = r"""
   _______________                        |*\_/*|________
  |  ___________  |     .-.     .-.      ||_/-\_|______  |
  | |           | |    .****. .****.     | |           | |
  | |   0   0   | |    .*****.*****.     | |   0   0   | |
  | |     -     | |     .*********.      | |     -     | |
  | |   \___/   | |      .*******.       | |   \___/   | |
  | |___     ___| |       .*****.        | |___________| |
  |_____|\_/|_____|        .***.         |_______________|
    _|__|/ \|_|_.............*.............._|________|_
   / ********** \                          / ********** \
 /  ************  \                      /  ************  \
--------------------                    --------------------
"""

########################## BEGIN FUNCTION DEFINITIONS ######################

def display_scoreboard(player_wins, computer_wins, num_games_played):
    num_ties = num_games_played - (player_wins - computer_wins)
    scoreboard = f"""
    PLAYER WINS:       {player_wins}
    COMPUTER WINS:     {computer_wins}
    # of TIES:         {num_ties}
    # of GAMES PLAYED: {num_games_played}
"""
def display_choices(player_choice, computer_choice):
    print(f"Player chooses: {valid_choices[player_choice]}")
    print(f"Computer chooses: {valid_choices[computer_choice]}")


def display_game_winner(player_wins, computer_wins):
    if player_wins > computer_wins:
        print("Player wins the series!")
        print(player_victory_ascii)
    elif computer_wins > player_wins:
        print("Computer wins the series!")
        print(computer_victory_ascii)
    else:
        print("The series tied!")


def find_round_winner(player_choice, computer_choice):
    global num_games_played
    if player_choice not in valid_choices:
        return "Try again"
    elif (
        player_choice == "rock"
        and computer_choice == "scissors"
        or player_choice == "paper"
        and computer_choice == "rock"
        or player_choice == "scissors"
        and computer_choice == "paper"
    ):
        return "Player"
    elif player_choice == computer_choice:
        return "Tie"
    else:
        return "Computer"
    num_games_played = num_games_played + 1
    display_scoreboard(player_wins, computer_wins, num_games_played)


########################## END FUNCTION DEFINITIONS ######################


player_wins = 0
computer_wins = 0
valid_choices = {
    "rock": "🪨",
    "paper": "📜",
    "scissors": "✂️"
}

winning_message = {
    "rock": "Rock crushes scissors",
    "paper": "Paper covers rock",
    "scissors": "Scissors cut paper",
}

print("Welcome to Rock, Paper, Scissors!")
print("Your valid choices are:")

for valid_choice, emoji in valid_choices.items():
    print(f"{valid_choices}: {emoji}")


while True:
    player_choice = input("rock, paper, or scissors? ")
    computer_choice = choice(list(valid_choices))
    display_choices(player_choice, computer_choice)

    round_winner = find_round_winner(player_choice, computer_choice)

    if round_winner == "Player":
        print("Player wins this round!")
        print(winning_message[player_choice])
        player_wins += 1
    elif round_winner == "Computer":
        print("Computer wins this round!")
        print(winning_message[computer_choice])
        computer_wins += 1
    elif round_winner == "Try again":
        print("That was an invalid choice! Try again!")
    else:
        print("This round is a tie!")

    keep_playing = input("Keep playing (y/n)? ")

    if keep_playing != "y":
        break


display_game_winner(player_wins, computer_wins)
