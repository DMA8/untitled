# ПИШЕМ КРЕСТИКИ-НОЛИКИ
from enum import Enum
import pygame as pg
CELL_SIZE = 50
FPS = 60
class Cell(Enum):
    CROSS = 1
    ZERO = 2
    VOID = 0
class Player:
    '''
    Класс игрока, содержащий тип значков, имя
    '''
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type



class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for i in range(self.height)]


class GameFieldView:

    """
    виджет игрового поля, который отражает его на экране
    """
    def __init__(self, field):
        #загрузить картинки значков клеток
        # отобразить первичное поле \
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True #TODO: self._height учесть

    def get_coords(self,x,y ):
        return (0,0) #TODO: реально вычислить


class GameRoundManager:
    '''
    менеджер игры, запускающий все процессы
    '''
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self,i,j):
        player = self._players[self._current_player]
            #игрок делает клик на поле
        print('click_handled')


class GameWindow:
    '''
    содержит в себе виджет поля, кнопки
    должен вызывать сосбытия, связ. с Roundmanager
    '''
    def __init__(self):
        #инициалищация пайгейма
        pg.init()

        self._width = 800
        self._height = 600
        self._title = 'KRESTIKI-NOOOLIKIY'
        self._screen = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption(self._title)


        player1 = Player('Петя', Cell.CROSS)
        player2 = Player('Вася', Cell.ZERO)
        self._game_manager = GameRoundManager(player1,player2)
        self._field_widget = GameFieldView(self._game_manager.field)




    def main_loop(self):
        finished = False
        clock = pg.time.Clock()
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                elif event.type == pg.MOUSEBUTTONDOWN:
                    x,y = pg.mouse.get_pos()
                    if self._field_widget.check_coords_correct(x,y):
                        i,j = self._field_widget.get_coords(x,y)
                        self._game_manager.handle_click(i,j)
            pg.display.flip()
            clock.tick(FPS)

def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')
if __name__ == '__main__':
    main()





