import chess
import random

class engine():
  def __init__(self, board, ply):
    self.board = board
    self.ply = ply
  
  def convert(self,number,p):
    decimal = pow(10,p)
    return number / decimal
    

  def Piece_Square_Table(self, color):
    pawntable = [
        0, 0, 0, 0, 0, 0, 0, 0,
        5, 10, 10, -20, -20, 10, 10, 5,
        5, -5, -10, 0, 0, -10, -5, 5,
        0, 0, 0, 20, 20, 0, 0, 0,
        5, 5, 10, 25, 25, 10, 5, 5,
        10, 10, 20, 30, 30, 20, 10, 10,
        50, 50, 50, 50, 50, 50, 50, 50,
        0, 0, 0, 0, 0, 0, 0, 0]

    knightstable = [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20, 0, 5, 5, 0, -20, -40,
        -30, 5, 10, 15, 15, 10, 5, -30,
        -30, 0, 15, 20, 20, 15, 0, -30,
        -30, 5, 15, 20, 20, 15, 5, -30,
        -30, 0, 10, 15, 15, 10, 0, -30,
        -40, -20, 0, 0, 0, 0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50]

    bishopstable = [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10, 5, 0, 0, 0, 0, 5, -10,
        -10, 10, 10, 10, 10, 10, 10, -10,
        -10, 0, 10, 10, 10, 10, 0, -10,
        -10, 5, 5, 10, 10, 5, 5, -10,
        -10, 0, 5, 10, 10, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20]

    rookstable = [
        0, 0, 0, 5, 5, 0, 0, 0,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        -5, 0, 0, 0, 0, 0, 0, -5,
        5, 10, 10, 10, 10, 10, 10, 5,
        0, 0, 0, 0, 0, 0, 0, 0]

    queenstable = [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -10, 5, 5, 5, 5, 5, 0, -10,
        0, 0, 5, 5, 5, 5, 0, -5,
        -5, 0, 5, 5, 5, 5, 0, -5,
        -10, 0, 5, 5, 5, 5, 0, -10,
        -10, 0, 0, 0, 0, 0, 0, -10,
        -20, -10, -10, -5, -5, -10, -10, -20]

    kingstable = [
        20, 30, 10, 0, 0, 10, 30, 20,
        20, 20, 0, 0, 0, 0, 20, 20,
        -10, -20, -20, -20, -20, -20, -20, -10,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30]
      
    pawntable = [self.convert(i,2) for i in pawntable]
    knightstable = [self.convert(i,2) for i in knightstable]
    bishopstable = [self.convert(i,2) for i in bishopstable]
    rookstable = [self.convert(i,2) for i in rookstable]
    queenstable = [self.convert(i,2) for i in queenstable]
    kingstable = [self.convert(i,2) for i in kingstable]
    pawn = 0
    knight = 0
    rook = 0
    queen = 0
    king = 0
    bishop = 0

    pawnO = 0
    knightO = 0
    rookO = 0
    queenO = 0
    kingO = 0
    bishopO = 0

    for i in self.board.pieces(chess.PAWN, color):
      pawn+= pawntable[i]
    for i in self.board.pieces(chess.KNIGHT, color):
      knight+= pawntable[i]
    for i in self.board.pieces(chess.ROOK, color):
      rook+= pawntable[i]
    for i in self.board.pieces(chess.QUEEN, color):
      queen+= pawntable[i]
    for i in self.board.pieces(chess.KING, color):
      king+= pawntable[i]
    for i in self.board.pieces(chess.BISHOP, color):
      bishop+= pawntable[i]
    for i in self.board.pieces(chess.PAWN, not color):
      pawnO-= pawntable[chess.square_mirror(i)]
    for i in self.board.pieces(chess.KNIGHT, not color):
      knightO-= pawntable[chess.square_mirror(i)]
    for i in self.board.pieces(chess.ROOK, not color):
      rookO-= pawntable[chess.square_mirror(i)]
    for i in self.board.pieces(chess.QUEEN, not color):
      queenO-= pawntable[chess.square_mirror(i)]
    for i in self.board.pieces(chess.KING, not color):
      kingO-= pawntable[chess.square_mirror(i)]
    for i in self.board.pieces(chess.BISHOP, not color):
      bishopO-= pawntable[chess.square_mirror(i)]

    score = (pawn + pawnO) + (knight + knightO) + (rook + rookO) + (queen + queenO) + (king + kingO) + (bishop + bishopO)

    return score
  
  def avaliacao(self,cor):
    score = 0
    pecas = {chess.PAWN:1, chess.ROOK:5, chess.BISHOP:3.15,chess.KNIGHT:3, chess.QUEEN:10}

    for peca, valor in pecas.items():
      score += len(self.board.pieces(peca,cor)) * valor
      score -= len(self.board.pieces(peca, not cor)) * valor
    
    score += self.Piece_Square_Table(self.board.turn)
    
    if self.board.is_checkmate():
      if cor:
        return +9999
      else:
        return -9999
    elif self.board.is_stalemate():
          return 0
    elif self.board.is_fivefold_repetition():
          return 0
    elif self.board.is_insufficient_material():
          return 0
    elif self.board.can_claim_draw():
          return 0
    return score
  
  def negamax(self, alpha, beta, ply):
    if ply == 0:
      return self.avaliacao(self.board.turn)
    
    score = 0
    best_value = -1000

    for move in list(self.board.legal_moves):
      self.board.push(move)
      score = -self.negamax(-beta, -alpha, ply-1)
      self.board.pop()

      if best_value < score:
        best_value = score
      
      if score >= beta:
        return beta
      
      alpha = max(score, alpha)

    return best_value


  def movement(self, ply):

    queens_gambit = ["d2d4","c1f4","e2e3","f1c4","b1c3","g1f3","e1g1"]
    ruy_lopes = ["e2e4","b1c3","d2d3","c1f4","","g1f3","f1b5", "d1d2","e1c1"]
    speed_dragon = ["c7c5","g7g6","f8g7","d7d6","g8f6","e8g8","c8d6","b7b6","c8b7","b8c6"]
    counter_d4 = ["d7d5","e7e6","g8f6","c7c5","b8c6","f8e7","e8g8","b7b6","c8b7"]

    white = [queens_gambit, ruy_lopes]
    black = [speed_dragon,counter_d4]
    lm = list(self.board.legal_moves)

    if self.board.turn == True:
        oppening = random.choice(white)
    else:
        oppening = speed_dragon

    best_move = None
    best_value = -1000

    alpha = -1000
    beta = 1000

    if self.board.turn == True:
        oppening = random.choice(white)
    else:
        oppening = random.choice(black)

    for move in list(self.board.legal_moves):
      self.board.push(move)
      score = -self.negamax(-beta, -alpha, ply)
      self.board.pop()

      if str(move) in oppening:
            score+=0.5
            
      if str(move) in oppening:
            score+=0.5

      if best_move == None:
          best_move = move
      if best_value < score:
          best_value = score
          best_move = move

    return best_move