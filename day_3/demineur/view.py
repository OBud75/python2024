import math

from PIL import Image
import pygame

from board import GameBoard


class Game:
    _BG_BLOCK_IMAGE = "images/block.png"
    _BG_BLOCK_DISCOVERED = "images/discovered.png"
    _FLAG_IMAGE = "images/flag.png"
    _ICON = "images/icon.jpeg"
    _MUSIC = ""
    _TITLE = "Demineur"

    def __init__(self, board: GameBoard) -> None:
        self._board: GameBoard = board

        self._block_size = Image.open(
            fp=self._BG_BLOCK_IMAGE).size[0]

        width_pixels = self._get_pixels_from_block(
            block=self._board.width)
        height_pixels = self._get_pixels_from_block(
            block=self._board.height)

        self._window = pygame.display.set_mode(
            size=(width_pixels, height_pixels))

        pygame.display.set_caption(title=self._TITLE)
        pygame.display.set_icon(
            pygame.image.load(self._ICON))

    def run(self):
        pygame.init()
        self._load_all()
        # pygame.mixer.music.load(self._MUSIC)
        # pygame.mixer.music.play(loops=-1)

        play = True
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_click(event)

            pygame.display.flip()
        pygame.quit()

    def _load_all(self) -> None:
        for node in self._board.nodes:
            self._display_image(
                image=self._BG_BLOCK_IMAGE,
                x_block=node.col, y_block=node.row)

    def _handle_click(self, event) -> None:
        x, y = self._get_block_from_pixels(
            pos=event.pos)

        if event.button == 1:
            self._board.reveal(x=x, y=y)
            if self._board.is_lost:
                self._restart(text="Perdu")

            self._load_discovered()
            if self._board.is_won:
                self._restart(text="Gagné")

        if event.button == 3:
            node = self._board.table[x][y]
            if node.is_flagged:
                node.is_flagged = False
                self._display_image(
                    image=self._BG_BLOCK_IMAGE, x_block=x, y_block=y)
            else:
                node.is_flagged = True
                self._display_image(
                    image=self._FLAG_IMAGE, x_block=x, y_block=y)

    def _load_discovered(self) -> None:
        for x, row in enumerate(iterable=self._board.to_print):
            for y, char in enumerate(iterable=row):
                if char.isnumeric():
                    self._display_image(
                        image=self._BG_BLOCK_DISCOVERED,
                        x_block=x, y_block=y)
                    if char != "0":
                        self._display_text(
                            text=f" {char}",
                            color=self._get_rgb_colors(char=char),
                            x_block=y, y_block=x + 0.1)

    def _restart(self, text) -> None:
        self._display_text(
            text=f"{text} !! ",
            x_block=self._board.width * 0.3,
            y_block=self._board.height * 0.4,
            size=1,
            delay=1000,
            color=self._get_rgb_colors(char=text))
        self._board.start()
        self._load_all()

    def _get_pixels_from_block(self, block):
        return round(number=block * self._block_size)

    def _get_block_from_pixels(self, pos) -> tuple[int, int]:
        x, y = pos
        return (math.floor(y / self._block_size),
                math.floor(x / self._block_size))

    def _display_image(self, image, x_block, y_block) -> None:
        x_pixels = self._get_pixels_from_block(block=x_block)
        y_pixels = self._get_pixels_from_block(block=y_block)
        self._window.blit(
            source=pygame.image.load(image),
            dest=(y_pixels, x_pixels))

    def _display_text(self, text, x_block=0, y_block=0,
                      size=0.75, delay=0, color=(0, 0, 0)) -> None:

        font = pygame.font.Font(
            "freesansbold.ttf",
            self._get_pixels_from_block(block=size))
        text = font.render(
            text, True, color)

        self._window.blit(
            source=text,
            dest=(self._get_pixels_from_block(block=x_block),
                  self._get_pixels_from_block(block=y_block)))

        pygame.display.flip()
        pygame.time.delay(delay)

    def _get_rgb_colors(self, char) -> tuple[int, int, int]:
        colors: dict[str, str] = {
            "1": "blue",
            "2": "red",
            "3": "green",
            "4": "black",
            "5": "grey",
            "6": "brown",
            "7": "purple",
            "8": "yellow",

            "Gagné": "green",
            "Perdu": "red"}

        match colors.get(char):
            case "blue":
                return (0, 0, 255)
            case "red":
                return (255, 0, 0)
            case "green":
                return (0, 255, 0)
            case "black":
                return (0, 0, 0)
            case "grey":
                return (100, 100, 100)
            case "brown":
                return (60, 30, 0)
            case "purple":
                return (125, 0, 255)
            case "yellow":
                return (255, 255, 0)
            case "white":
                return (255, 255, 255)
