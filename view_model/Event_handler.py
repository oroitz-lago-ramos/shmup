import view_model as vm
import pygame

class Event_handler:
    def __init__(self, game):
        self.game = game
        self.pressed_keys = set()
         
    def handle_event(self):
        if isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.START_MENU]):
            self.pressed_keys.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_start_menu_event(event)
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.MAIN_MENU]):
            self.pressed_keys.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_main_menu_event(event)
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.GAME]):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_key_event(event)
            self.handle_game_event()
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.HALL_OF_FAME]):
            self.pressed_keys.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_hall_of_fame_event(event)
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.CHOOSE_BONUS]):
            self.pressed_keys.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_choose_bonus_event(event)
            
            
    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.pressed_keys.add(event.key)
        elif event.type == pygame.KEYUP:    
            if event.key in self.pressed_keys:
                self.pressed_keys.remove(event.key)

    def handle_game_event(self):
        if pygame.K_z in self.pressed_keys:
            self.game.player_ship.move_up()
        if pygame.K_s in self.pressed_keys:
            self.game.player_ship.move_down()
        if pygame.K_q in self.pressed_keys:
            self.game.player_ship.move_left()
        if pygame.K_d in self.pressed_keys:
            self.game.player_ship.move_right()

        if pygame.K_SPACE in self.pressed_keys:
            self.game.player_base.use_bomb(self.game.level.current_ennemy)
        
        if pygame.K_z not in self.pressed_keys and pygame.K_s not in self.pressed_keys and pygame.K_q not in self.pressed_keys and pygame.K_d not in self.pressed_keys:
            self.game.player_ship.timer_decelerate += 1
            if self.game.player_ship.timer_decelerate >= 5:
                self.game.player_ship.decelerate()
                self.game.player_ship.timer_decelerate -= 5
            
        else:
            self.game.player_ship.accelerate()
        self.game.player_ship.move()
        
    def handle_start_menu_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.sound_manager.play_start_sound()
                self.game.change_view(vm.View_state.MAIN_MENU)
            elif event.key == pygame.K_ESCAPE:
                self.game.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            start_text_x = (self.game.screen.get_width() // 2) - 100
            start_text_y = self.game.screen.get_height() // 1.37
            start_text_width = 280
            start_text_height = 70
            if start_text_x <= mouse_x <= start_text_x + start_text_width and \
            start_text_y <= mouse_y <= start_text_y + start_text_height:
                self.game.sound_manager.play_start_sound()
                self.game.change_view(vm.View_state.MAIN_MENU)

    def handle_main_menu_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_view(vm.View_state.START_MENU)
            elif event.key == pygame.K_RETURN and (self.game.player_name != "" and self.game.player_name != " "):
                self.game.sound_manager.play_click_sound()
                self.game.reset_game()
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from player_name
                self.game.sound_manager.play_click_sound()
                self.game.player_name = self.game.player_name[:-1]
            elif event.unicode.isalnum() or event.unicode == " ":
                # Append the pressed character to player_name
                if self.game.player_name == "" and event.unicode == " ":
                    return
                self.game.player_name += event.unicode
                self.game.sound_manager.play_click_sound()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            #Button play for the main menu
            button_play_x = self.game.screen.get_width()//2 - 80
            button_play_y = self.game.screen.get_height()//3 + 90
            button_play_width = 200
            button_play_height = 50
            #Button parameter for the main menu
            button_parameter_x = self.game.screen.get_width()//2 - 80
            button_parameter_y = self.game.screen.get_height()//3 + 160
            button_parameter_width = 200
            button_parameter_height = 50
            #If the mouse is on the button play
            if button_play_x <= mouse_x <= button_play_x + button_play_width and \
            button_play_y <= mouse_y <= button_play_y + button_play_height and (self.game.player_name != "" and self.game.player_name != " "):
                self.game.sound_manager.play_click_sound()
                # pygame.time.wait(600)
                self.game.reset_game()
            #If the mouse is on the button parameter
            elif button_parameter_x <= mouse_x <= button_parameter_x + button_parameter_width and \
            button_parameter_y <= mouse_y <= button_parameter_y + button_parameter_height:
                self.game.sound_manager.play_click_sound()
                self.game.change_view(vm.View_state.PARAMETER)

            
                
    def handle_hall_of_fame_event(self, event):
        x_button = self.game.current_view.get_x_button()
        replay_button = self.game.current_view.get_replay_button()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if x_button[0] <= mouse_pos[0] <= x_button[0] + x_button[2] and x_button[1] <= mouse_pos[1] <= x_button[1] + x_button[3]:
                self.game.change_view(vm.View_state.MAIN_MENU)
            elif replay_button[0] <= mouse_pos[0] <= replay_button[0] + replay_button[2] and replay_button[1] <= mouse_pos[1] <= replay_button[1] + replay_button[3]:
                self.game.reset_game()
                
    def handle_choose_bonus_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicked the mouse
            x, y = pygame.mouse.get_pos()  # Get the position of the mouse
            if 100 <= x <= 300 and 250 <= y <= 300:  # If the user clicked on the text for boost 1
                self.game.set_player_bonus(self.game.current_view.boost1)
            elif 500 <= x <= 700 and 250 <= y <= 300:  # If the user clicked on the text for boost 2
                self.game.set_player_bonus(self.game.current_view.boost2)
            