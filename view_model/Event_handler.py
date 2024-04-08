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
        elif isinstance(self.game.current_view, self.game.VIEW_STATES[vm.View_state.END_MENU]):
            self.pressed_keys.clear()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.stop()
                self.handle_end_menu_event(event)
            
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
            self.game.change_view(vm.View_state.END_MENU)

        
        if pygame.K_z not in self.pressed_keys and pygame.K_s not in self.pressed_keys and pygame.K_q not in self.pressed_keys and pygame.K_d not in self.pressed_keys:
            self.game.player_ship.timer_decelerate += self.game.clock.tick_busy_loop(60) # bug acceleration de toutes les entités qui s'affichent
            if self.game.player_ship.timer_decelerate >= 100:
                self.game.player_ship.decelerate()
                self.game.player_ship.timer_decelerate -= 100
            
        else:
            self.game.player_ship.accelerate()
        self.game.player_ship.move()
        
    def handle_start_menu_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_view(vm.View_state.MAIN_MENU)
            elif event.key == pygame.K_ESCAPE:
                self.game.stop()
    
    def handle_main_menu_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_view(vm.View_state.GAME)
            elif event.key == pygame.K_ESCAPE:
                self.game.change_view(vm.View_state.START_MENU)
                
    def handle_end_menu_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_view(vm.View_state.MAIN_MENU)
            elif event.key == pygame.K_ESCAPE:
                self.game.stop()

            