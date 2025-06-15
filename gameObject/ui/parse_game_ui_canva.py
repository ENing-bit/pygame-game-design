from .ui_canvas import UICanvas
from pygame.math import Vector2
from typing import Union
import pygame_gui
import pygame
from game import LifeCycle, Game

class ParseGameUICanvas(UICanvas):
    def __init__(self,screen_size: Union[tuple, Vector2] = (1600, 900), theme_path: str = "theme.json", game_map_manager = None):
        super().__init__(screen_size, theme_path)

        self.game_map_manager = game_map_manager

        self.restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((500, 500), (600, 50)),
            text="Press To Restart",
            manager=self.ui_manager,
            object_id="#restart_button",
        )

        self.parse_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((500, 600), (600, 50)),
            text="Parse Game",
            manager=self.ui_manager,
            object_id="#parse_label",
        )

        self.restart_button.hide()
        self.parse_label.hide()

    def init(self, sender, **kwargs):
        super().init(sender, **kwargs)
    
    def update(self, sender, **kwargs):
        super().update(sender, **kwargs)
    
    def event(self, sender, **kwargs):
        super().event(sender, **kwargs)
        event = kwargs.get("event", None)
        if event is None:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Game._instance.game_pause(self)
        # 监听按钮点击事件
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.restart_button:
                Game._instance.game_resume(self)

        
    def draw(self, sender, **kwargs):
        super().draw(sender, **kwargs)
    
    def on_game_start(self, sender):
        self.parse_label.hide()
        self.restart_button.hide()

    def on_game_pause(self, sender):
        self.parse_label.show()
        self.restart_button.show()

    def on_game_resume(self, sender):
        self.parse_label.hide()
        self.restart_button.hide()
        