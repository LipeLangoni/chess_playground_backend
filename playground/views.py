from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import engine as p1
import chess

board = chess.Board()

@api_view(['POST'])
def make_move(request):
    move = request.data.get('uci_move')
    board.push_san(move)
    engine = p1.engine(board,4)
    engine_move = engine.movement(4)

    if engine_move is not None:
        board.push(engine_move)
    else:
        board.reset()

    if board.is_game_over():
        board.reset()

    return Response({'engine_move': engine_move.uci(), 'fen': board.fen()})

@api_view(['POST'])
def reset_board(request):
    board.reset()
    return Response({'message': 'Board reset successfully'})