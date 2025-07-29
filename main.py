import json
import chess

from PIL import Image

theme = 'stole'
file0 = 'stole1.png'

# Carica il file JSON
with open('themes/'+theme+'/settings.json', 'r') as f:
    dati = json.load(f)

board = chess.Board("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")

larghezza, altezza = dati['size']
board_offset_x, board_offset_y = dati['sprites'][file0]['board']['offset']
board_border_x, board_border_y = dati['sprites'][file0]['board']['border']
board_square_width, board_square_height = dati['sprites'][file0]['board']['square']

immagine = Image.new('RGB', (larghezza, altezza), 'white')

# Carica lo sprite sheet
sprite_sheet = Image.open("themes/"+theme+"/"+ file0)

# Estrai lo sprite di base (sfondo/terreno)
sprite_base = sprite_sheet.crop((board_offset_x, board_offset_y, board_offset_x+larghezza, board_offset_y+altezza))  # Esempio: primo sprite 64x64

# Estrai altri sprite
#personaggio = sprite_sheet.crop((64, 0, 96, 32))  # Sprite personaggio
#oggetto = sprite_sheet.crop((0, 64, 32, 96))      # Altro sprite

# Applica prima lo sprite di base (come sfondo)
immagine.paste(sprite_base, (0, 0))

# Poi aggiungi altri sprite sopra
#immagine.paste(personaggio, (120, 80))
#immagine.paste(oggetto, (200, 150))

for rank in range(8):
    for file in range(8):
        square = chess.square(file, rank)
        piece = board.piece_at(square)
        selector = [0, 0]
        if (rank + file) % 2 == 0:
            selector = [0, 3]
        else:
            selector = [0, 4]

        if piece and piece.piece_type == chess.KING:
            selector = [4, 0]

        square_picture = sprite_sheet.crop((
            board_offset_x + board_border_x + selector[0] * board_square_width,
            board_offset_y + board_border_y + selector[1] * board_square_height,
            board_offset_x + board_border_x + selector[0] * board_square_width + board_square_width,
            board_offset_y + board_border_y + selector[1] * board_square_height + board_square_height
        ))
        if True:
            immagine.paste(square_picture, (
                board_border_x + file * board_square_width,
                board_border_y + rank * board_square_height
            ))


# Salva il risultato
immagine.save("output.png")
