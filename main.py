import random

from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Config.set('graphics', 'width', '400')
Config.set('graphics', 'width', '900')

from kivy import platform
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color, Line, Quad, Triangle
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty


Builder.load_file("menu.kv")


class MainWidget(RelativeLayout):
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import on_keyboard_up, on_keyboard_down, keyboard_closed, on_touch_down, on_touch_up

    menu_widget = ObjectProperty()
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = .4
    vertical_lines = []

    H_NB_LINES = 8
    H_LINES_SPACING = .15
    horizontal_lines = []

    SPEED = .9
    current_offset_y = 0
    current_y_loop = 0

    SPEED_X = 3.0
    current_offset_x = 0
    current_speed_x = 0

    NB_TILES = 16
    tiles = []
    tiles_coordinates = []

    SHIP_WIDTH = .1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship = None
    ship_coordinates = [(0,0), (0,0), (0,0)]

    state_game_over = False
    state_game_has_started = False

    menu_title = StringProperty("S P A C E    O D Y S S E Y")
    menu_button_title = StringProperty("S T A R T")
    score_txt = StringProperty()

    sound_begin = None
    sound_space_odyssey = None
    sound_bip = None
    sound_game_over = None
    sound_music1 = None
    sound_restart = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_audio()
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()
        self.init_ship()
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()

        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down= self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

        self.sound_space_odyssey.play()

    def init_audio(self):
        self.sound_begin = SoundLoader.load('audio/begin.wav')
        self.sound_space_odyssey = SoundLoader.load('audio/space odyssey.wav')
        self.sound_bip = SoundLoader.load('audio/bip.wav')
        self.sound_game_over = SoundLoader.load('audio/game over.wav')
        self.sound_music1 = SoundLoader.load('audio/faded.wav')
        self.sound_restart = SoundLoader.load('audio/restart.wav')

        self.sound_music1.volume = .6
        self.sound_begin.volume = .50
        self.sound_space_odyssey.volume = .50
        self.sound_bip.volume = .60
        self.sound_game_over.volume = .50
        self.sound_restart.volume = .50

    def reset_game(self):
        self.current_offset_y = 0
        self.current_y_loop = 0
        self.current_offset_x = 0
        self.current_speed_x = 0
        self.tiles_coordinates = []
        self.score_txt = f"SCRORE: {self.current_y_loop}"
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()
        self.state_game_over = False

    def is_desktop(self): # détecte si c'est un ordinateur linux, macos, linux
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def init_ship(self): # initialisation vaisseau -> couleur, forme
        with self.canvas:
            Color(0.5, 0.3, 0.7)
            self.ship = Triangle()

    def update_ship(self): # actualisation vaisseau -> position, taille, coordoner, longeur, largeur, hauteur
        center_x = self.width / 2
        base_y = self.SHIP_BASE_Y * self.height
        half_width = self.SHIP_WIDTH * self.width / 2
        ship_height = self.SHIP_HEIGHT * self.height

        self.ship_coordinates[0] = (center_x - half_width, base_y)
        self.ship_coordinates[1] = (center_x, base_y + ship_height)
        self.ship_coordinates[2] = (center_x + half_width, base_y)

        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2= self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])
        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collisions(self): # collision -> boucle pour le tiles quand le vaisseau arrive à l ala fin du tiles
        for i in range(0, len(self.tiles_coordinates)):
            ti_x, ti_y = self.tiles_coordinates[i]
            if ti_y > self.current_y_loop + 1:
                return False
            if self.check_ship_collision_with_tiles(ti_x, ti_y):
                return True
        return False

    def check_ship_collision_with_tiles(self, ti_x, ti_y): #avec tiles
        xmin, ymin = self.get_tile_coordinates(ti_x, ti_y)
        xmax, ymax = self.get_tile_coordinates(ti_x+1, ti_y+1)
        for i in range(0, 3):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
                return True
        return False

    def init_tiles(self): # initialisation tuile: nombre tuiles, couleur,
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_TILES):
                self.tiles.append(Quad())

    def pre_fill_tiles_coordinates(self): # ajouter tuiles par incrémentation
        for i in range (0, 10):
            self.tiles_coordinates.append((0, i))

    def generate_tiles_coordinates(self): # génération coordiner tuiles
        last_x = 0
        last_y = 0
        for i in range(len(self.tiles_coordinates)-1, -1, -1):
            if self.tiles_coordinates[i][1] < self.current_y_loop:
                del self.tiles_coordinates[i]

        if len(self.tiles_coordinates) > 0:
            last_coordinate = self.tiles_coordinates[-1]
            last_x = last_coordinate[0]
            last_y = last_coordinate[1] + 1

        for i in range(len(self.tiles_coordinates), self.NB_TILES):
            r = random.randint(0, 2)
            start_index = -int(self.V_NB_LINES / 2) + 1
            end_index = start_index + self.V_NB_LINES - 2
            if last_x <= start_index:
                r = 1
            elif last_x >= end_index:
                r = 2
            self.tiles_coordinates.append((last_x, last_y))
            if r == 1:
                last_x += 1
                self.tiles_coordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_coordinates.append((last_x, last_y))
            elif r == 2:
                last_x -= 1
                self.tiles_coordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_coordinates.append((last_x, last_y))
            last_y += 1

    def init_vertical_lines(self): # initialisation chemin, couleur,
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index-0.5
        line_x = central_line_x + offset*spacing + self.current_offset_x
        return line_x

    def get_line_y_from_index(self, index):
        spacing_y = self.H_LINES_SPACING * self.height
        line_y = index * spacing_y - self.current_offset_y
        return line_y

    def get_tile_coordinates(self, ti_x, ti_y):
        ti_y = ti_y - self.current_y_loop
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile = self.tiles[i]
            tile_coordinates = self.tiles_coordinates[i]
            xmin, ymin = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_tile_coordinates(tile_coordinates[0]+1, tile_coordinates[1]+1)

            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)
            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def update_vertical_lines(self):
        start_index = -int(self.V_NB_LINES/2)+1
        for i in range(start_index, start_index+self.V_NB_LINES):
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES/2)+1
        end_index = start_index + self.V_NB_LINES-1

        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        # spacing_y = self.H_LINES_SPACING*self.height
        for i in range(0, self.H_NB_LINES):
            line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt):
        time_factor = dt*60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.update_ship()

        if not self.state_game_over and self.state_game_has_started:
            speed_y = self.SPEED * self.height / 100
            self.current_offset_y += speed_y*time_factor

            spacing_y = self.H_LINES_SPACING * self.height
            while self.current_offset_y >= spacing_y:
                self.current_offset_y -= spacing_y
                self.current_y_loop += 1
                self.score_txt = f"SCRORE: {self.current_y_loop}"
                self.generate_tiles_coordinates()
            speed_x = self.current_speed_x * self.width / 100
            self.current_offset_x += speed_x*time_factor

        if not self.check_ship_collisions() and not self.state_game_over:
            self.state_game_over = True
            self.menu_title = "G  A  M  E    O  V  E  R"
            self.menu_button_title = "R E S T A R T"
            self.menu_widget.opacity = 1
            self.sound_music1.stop()
            self.sound_bip.play()
            Clock.schedule_once(self.play_voice_game_over, 1)

    def play_voice_game_over(self, dt): #
        if self.state_game_over:
            self.sound_game_over.play()

    def on_menu_button_pressed(self): # gestion bouton
        if self.state_game_over:
            self.sound_restart.play()
        else:
            self.sound_begin.play()
        
        self.sound_music1.play()
        self.reset_game()
        self.state_game_has_started = True
        self.menu_widget.opacity = 0


class Space_OdysseyApp(App):
    pass


Space_OdysseyApp().run()
