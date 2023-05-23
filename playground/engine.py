import chess
import random

class engine():
  def __init__(self, board, ply):
    self.board = board
    self.ply = ply

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
    

    pecas = {chess.PAWN:pawntable, chess.ROOK:rookstable, chess.BISHOP:bishopstable,chess.KNIGHT:knightstable, chess.QUEEN:queenstable, chess.KING:kingstable}
    pecas_indx = {chess.PAWN:0, chess.ROOK:1, chess.BISHOP:2,chess.KNIGHT:3, chess.QUEEN:4, chess.KING:5}
    pecas_w = [0,0,0,0,0,0]
    pecas_b = [0,0,0,0,0,0]

    for peca in pecas:
       for i in self.board.pieces(peca, color):
          pecas_w[pecas_indx[peca]] += pecas[peca][i]
      
    for peca in pecas:
       for i in self.board.pieces(peca, not color):
          pecas_b[pecas_indx[peca]] += pecas[peca][chess.square_mirror(i)]

    score = sum([i + b for i,b in zip(pecas_w,pecas_b)])

    return score
  
  def avaliacao(self,cor):
    score = 0
    pecas = {chess.PAWN:100, chess.ROOK:500, 
    chess.BISHOP:300.15,chess.KNIGHT:300, 
    chess.QUEEN:1000}

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
  
  def quisce(self,alpha,beta,ply):
    if ply == 0:
      return self.avaliacao(self.board.turn)
    
    stand_pat = self.avaliacao(self.board.turn)
    if stand_pat >= beta:
      return beta
    
    delta = 1000

    if alpha < stand_pat:
      alpha = stand_pat
    
    for move in list(self.board.legal_moves):
      if self.board.is_capture(move):
        self.board.push(move)
        score = -self.quisce(-beta, -alpha, ply-1)
        self.board.pop()

        if move.promotion:
            delta+=750
        if stand_pat < alpha-delta:
            return alpha
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    return alpha

          
      
     


  def movement(self, ply):
    best_move = None
    best_value = -1000

    alpha = -1000
    beta = 1000

    
    oppening = ["g7g6","f8g7","g8f6","e8g8","d7d6","c8g4","b8c6","c7c5"]
    oppening_super = ["g7g6","f8g7","g8f6","e8g8"]

    for move in list(self.board.legal_moves):
      self.board.push(move)
      score = -self.negamax(-beta, -alpha, ply)
      self.board.pop()

      if str(move) in oppening:
         score += 150
      if move in oppening_super:
         score +=200
      
      if best_move == None:
          best_move = move
      if best_value < score:
          best_value = score
          best_move = move

    return best_move