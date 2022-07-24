from deck import *
from parameters import *
import sys
import time


class Play:
    def __init__(self):
        self.deck = Deck()
        self.pp = Points()
        self.dp = Points()
        self.dealer = Hand()
        self.player = Hand()
        self.player_card = 1
        self.default_x_pos = 150
        self.dealer_y_pos = 100
        self.player_y_pos = 400

    def deal(self):
        for _ in range(2):
            self.dealer.get_card(self.deck.deal())
            self.player.get_card(self.deck.deal())
            
        self.dealer.display_cards()
        self.player.display_cards()
        self.player_card = 1
        
        game_texts("Dealer's hand is:", 170, 50)
        
        card_img = pygame.image.load(
        'img/' + self.dealer.cards[1]['rank'] + self.dealer.cards[1]['suit'] + '.png'
        )
        gameDisplay.blit(card_img, (self.default_x_pos, self.dealer_y_pos))
        gameDisplay.blit(background, (300, self.dealer_y_pos))
        
        game_texts("Player's hand is:", 150, 350)
        
        for card in self.player.cards:
            card_img = pygame.image.load('img/' + card['rank'] + card['suit'] + '.png')
            gameDisplay.blit(card_img, (self.default_x_pos, self.player_y_pos))
            self.default_x_pos += 150

        self.blackjack()
        
    def blackjack(self):
        self.default_x_pos = 150
        self.dealer.calc_hand()
        self.player.calc_hand()

        show_dealer_card = pygame.image.load(
        'img/' + self.dealer.cards[0]['rank'] + self.dealer.cards[0]['suit'] + '.png'
        )
        
        if self.player.value == 21 and self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (300, self.dealer_y_pos))
            black_jack("Both with BlackJack!", 700, 350, grey)
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == 21:
            gameDisplay.blit(show_dealer_card, (300, self.dealer_y_pos))
            black_jack("Player has BlackJack!", 700, 350, green)
            self.pp.point += 1
            time.sleep(4)
            self.play_or_exit()
        elif self.dealer.value == 21:
            gameDisplay.blit(show_dealer_card, (300, self.dealer_y_pos))
            black_jack("Dealer has BlackJack!", 700, 350, red)
            self.dp.point += 1
            time.sleep(4)
            self.play_or_exit()

    def hit(self):
        self.player.get_card(self.deck.deal())
        self.blackjack()
        self.player_card += 1

        if self.player_card == 2:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_3 = pygame.image.load(
            'img/' + self.player.cards[2]['rank'] + self.player.cards[2]['suit'] + '.png'
            )
            gameDisplay.blit(player_card_3, (450, 400))

        if self.player_card == 3:
            self.player.calc_hand()
            self.player.display_cards()
            player_card_4 = pygame.image.load(
            'img/' + self.player.cards[3]['rank'] + self.player.cards[3]['suit'] + '.png'
            )
            gameDisplay.blit(player_card_4, (600, 400))

        if self.player.value > 21:
            show_dealer_card = pygame.image.load(
            'img/' + self.dealer.cards[1]['rank'] + self.dealer.cards[1]['suit'] + '.png'
            )
            gameDisplay.blit(show_dealer_card, (300, 100))
            game_finish("You Busted!", 700, 350, red)
            self.dp.point += 1
            time.sleep(4)
            self.play_or_exit()

        if self.player_card > 4:
            sys.exit()

    def stand(self):
        self.dealer.calc_hand()

        if self.dealer.value <= 14:
            self.dealer.get_card(self.deck.deal())
            self.dealer.display_cards()

            dealer_card_3 = pygame.image.load(
            'img/' + self.dealer.cards[2]['rank'] + self.dealer.cards[2]['suit'] + '.png'
            )
            gameDisplay.blit(dealer_card_3, (450, 100))

        show_dealer_card = pygame.image.load(
            'img/' + self.dealer.cards[0]['rank'] + self.dealer.cards[0]['suit'] + '.png'
        )
        gameDisplay.blit(show_dealer_card, (300, 100))

        self.blackjack()

        if self.dealer.value > 21:
            game_finish("Dealer Busted!", 700, 350, red)
            self.pp.point += 1
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value > self.dealer.value:
            game_finish("Player Wins!", 700, 350, green)
            self.pp.point += 1
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value < self.dealer.value:
            game_finish("Dealer Wins!", 700, 350, red)
            self.dp.point += 1
            time.sleep(4)
            self.play_or_exit()
        elif self.player.value == self.dealer.value:
            game_finish("Draw!", 700, 350, grey)
            time.sleep(4)
            self.play_or_exit()

    @staticmethod
    def exit_game():
        sys.exit()
        
    @staticmethod
    def clear_table():
        game.play_or_exit()

    def play_or_exit(self):
        game_texts("To play again - press Deal!", 550, 50)
        time.sleep(3)
        self.player.value = self.dealer.value = 0
        self.deck = Deck()
        self.dealer = Hand()
        self.player = Hand()
        gameDisplay.blit(table, (0, 0))
        pygame.display.update()


game = Play()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        button("Deal", 50, 650, 150, 50, light_slat, dark_slat, game.deal)
        button("Hit", 250, 650, 150, 50, light_slat, dark_slat, game.hit)
        button("Stand", 450, 650, 150, 50, light_slat, dark_slat, game.stand)
        button("EXIT", 800, 50, 150, 50, light_slat, dark_slat, game.exit_game)
        button("Clear table", 750, 650, 200, 50, light_slat, dark_slat, game.clear_table)
        points(f"Dealer: {game.dp.point}", 775, 125, 200, 50, dark_slat)
        points(f"Player: {game.pp.point}", 775, 200, 200, 50, dark_slat)

    pygame.display.update()
