import sys
input_file=sys.argv[1]
"""
Ali Kemal Tamkoç
b2200356856
"""


chess_board=[]
for item in range(0,9):
    chess_board.append([["  ","  "],["  ",""],["  ",""],["  ",""],["  ",""],["  ",""],["  ",""],["  ",""],["  ",""]])
    
black_pieces=["R1","N1","B1","QU","B2","N2","R2","P1","P2","P3","P4","P5","P6","P7","P8"]
white_pieces=["r1","n1","b1","qu","b2","n2","r2","p1","p2","p3","p4","p5","p6","p7","p8"]


def print_board():
    
    print("-----------------------")
    for number in range(1,9):
        for number2 in range(1,9):
            a=(chess_board[9-number][number2][0])
            print(a,end=" ")
        print("")
    print("-----------------------")

#addding positions to chess_board
for number in range(1,9):
    for number2 in range (1,9):
        if number2==1:            
            chess_board[number][number2][1]=f'a{number}'
        if number2==2:
             chess_board[number][number2][1]=f'b{number}'
        if number2==3:
             chess_board[number][number2][1]=f'c{number}'
        if number2==4:
             chess_board[number][number2][1]=f'd{number}'
        if number2==5:
             chess_board[number][number2][1]=f'e{number}'
        if number2==6:
             chess_board[number][number2][1]=f'f{number}'
        if number2==7:
             chess_board[number][number2][1]=f'g{number}'
        if number2==8:
             chess_board[number][number2][1]=f'h{number}'



def initialize():
    for number in range(1,9):
        for number2 in range(1,9):
            chess_board[number][number2][0]="  "
            
    chess_board[1][1][0]="r1"
    chess_board[1][2][0]="n1"
    chess_board[1][3][0]="b1"
    chess_board[1][4][0]="qu"
    chess_board[1][5][0]="ki"
    chess_board[1][6][0]="b2"
    chess_board[1][7][0]="n2"
    chess_board[1][8][0]="r2"
    chess_board[2][1][0]="p1"
    chess_board[2][2][0]="p2"
    chess_board[2][3][0]="p3"
    chess_board[2][4][0]="p4"
    chess_board[2][5][0]="p5"
    chess_board[2][6][0]="p6"
    chess_board[2][7][0]="p7"
    chess_board[2][8][0]="p8"
    
    
    chess_board[7][1][0]="P1"
    chess_board[7][2][0]="P2"
    chess_board[7][3][0]="P3"
    chess_board[7][4][0]="P4"
    chess_board[7][5][0]="P5"
    chess_board[7][6][0]="P6"
    chess_board[7][7][0]="P7"
    chess_board[7][8][0]="P8"
    chess_board[8][1][0]="R1"
    chess_board[8][2][0]="N1"
    chess_board[8][3][0]="B1"
    chess_board[8][4][0]="QU"
    chess_board[8][5][0]="KI"
    chess_board[8][6][0]="B2"
    chess_board[8][7][0]="N2"
    chess_board[8][8][0]="R2"
    

def piece_row_finder(piece):
    current_row=-1 #since chess_board index=0 is empty

    for item in chess_board:
        current_row=current_row+1
        for item2 in item:
            if piece==item2[0]:
                
                
                return (current_row)

def piece_column_finder(piece):
    for item in chess_board:
        for item2 in item:
            if piece==item2[0]:
                return (item.index(item2))

def position_row_finder(position):
    current_row=-1
    for item in chess_board:
        current_row=current_row+1
        for item2 in item:
            if position==item2[1]:
                return current_row

def position_column_finder(position):
    for item in chess_board:
        for item2 in item:
            if position==item2[1]:
                return (item.index(item2))



def show_moves(piece):
    
    piece_row=(piece_row_finder(piece))
    piece_column=((piece_column_finder(piece)))
    available_moves=[]
    
    
  
    if piece in ["p1","p2","p3","p4","p5","p6","p7","p8"]:
        #our piece is a white pawn and it can move one step forward. if the square is occupied it can eat the black piece.
        
            
        if chess_board[(piece_row)+1][piece_column][0]=="  "or chess_board[(piece_row)+1][piece_column][0] in black_pieces:
            available_moves.append(chess_board[piece_row+1][piece_column][1])
            
    if piece in ["P1","P2","P3","P4","P5","P6","P7","P8"]:
        #our piece is a black pawn and it can move one step downwards. if the square is occupied it can eat the white piece
            
        if chess_board[piece_row-1][piece_column][0]=="  "or chess_board[piece_row-1][piece_column][0] in white_pieces:
            available_moves.append(chess_board[piece_row-1][piece_column][1])
    if piece in ["ki"]:
    #our piece is a white king
    #sol-sağ-solüst-solalt-sağüst-sağalt-üst-alt'a gidebilir
    
    #üstü kontrol etme
        if piece_row+1<=8:
            if chess_board[piece_row+1][piece_column][0]=="  " or chess_board[piece_row+1][piece_column][0] in black_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column][1])
    #altı kontrol etme
        if piece_row-1>=1:
            if chess_board[piece_row-1][piece_column][0]=="  " or chess_board[piece_row-1][piece_column][0] in black_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column][1])
    #sağı kontrol etme
        if piece_column+1<=8:
            if chess_board[piece_row][piece_column+1][0]=="  " or chess_board[piece_row][piece_column+1][0] in black_pieces:
                available_moves.append(chess_board[piece_row][piece_column+1][1])
    #solu kontrol etme
        if piece_column-1>=1:
            if chess_board[piece_row][piece_column-1][0]=="  " or chess_board[piece_row][piece_column-1][0] in black_pieces:
                available_moves.append(chess_board[piece_row][piece_column-1][1])
    #sağ üstü kontrol etme
        if piece_row+1<=8 and piece_column+1<=8:
            if chess_board[piece_row+1][piece_column+1][0]=="  " or chess_board[piece_row+1][piece_column+1][0] in black_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column+1][1])
    
    #sol üstü kontrol etme
        if piece_row+1<=8 and piece_column-1>=1:
            if chess_board[piece_row+1][piece_column-1][0]=="  " or chess_board[piece_row+1][piece_column-1][0] in black_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column-1][1])
    
    #sağ altı kontrol etme
    
        if piece_row-1>=1 and piece_column+1<=8:
            if chess_board[piece_row-1][piece_column+1][0]=="  " or chess_board[piece_row-1][piece_column+1][0] in black_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column+1][1])
    
        if piece_row-1>=1 and piece_column-1>=1:
           if chess_board[piece_row-1][piece_column-1][0]=="  " or chess_board[piece_row-1][piece_column-1][0] in black_pieces:
               available_moves.append(chess_board[piece_row-1][piece_column-1][1])

    if piece in ["KI"]:
        #our piece is a black king
        #sol-sağ-solüst-solalt-sağüst-sağalt-üst-alt'a gidebilir

    
    #üstü kontrol etme
        if piece_row+1<=8:
            if chess_board[piece_row+1][piece_column][0]=="  " or chess_board[piece_row+1][piece_column][0] in white_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column][1])
    #altı kontrol etme
        if piece_row-1>=1:
            if chess_board[piece_row-1][piece_column][0]=="  " or chess_board[piece_row-1][piece_column][0] in white_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column][1])
    #sağı kontrol etme
        if piece_column+1<=8:
            if chess_board[piece_row][piece_column+1][0]=="  " or chess_board[piece_row][piece_column+1][0] in white_pieces:
                available_moves.append(chess_board[piece_row][piece_column+1][1])
    #solu kontrol etme
        if piece_column-1>=1:
            if chess_board[piece_row][piece_column-1][0]=="  " or chess_board[piece_row][piece_column-1][0] in white_pieces:
                available_moves.append(chess_board[piece_row][piece_column-1][1])
    #sağ üstü kontrol etme
        if piece_row+1<=8 and piece_column+1<=8:
            if chess_board[piece_row+1][piece_column+1][0]=="  " or chess_board[piece_row+1][piece_column+1][0] in white_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column+1][1])
    
    #sol üstü kontrol etme
        if piece_row+1<=8 and piece_column-1>=1:
            if chess_board[piece_row+1][piece_column-1][0]=="  " or chess_board[piece_row+1][piece_column-1][0] in white_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column-1][1])
    
    #sağ altı kontrol etme
    
        if piece_row-1>=1 and piece_column+1<=8:
            if chess_board[piece_row-1][piece_column+1][0]=="  " or chess_board[piece_row-1][piece_column+1][0] in white_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column+1][1])
    
        if piece_row-1>=1 and piece_column-1>=1:
            if chess_board[piece_row-1][piece_column-1][0]=="  " or chess_board[piece_row-1][piece_column-1][0] in white_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column-1][1])
    
    
    
    if piece in["r1","r2"]:
    #sağa gitme kontrol
        for number in range (1,8):
            if piece_column+number>8:
                break
            else:
                if chess_board[piece_row][piece_column+(number)][0]=="  " or chess_board[piece_row][piece_column+(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row][piece_column+(number)][1])
                    if chess_board[piece_row][piece_column+(number)][0] in black_pieces:
                        break
                else:
                    break
    #sola gitme kontrol
        for number in range (1,8):
         if piece_column-number<1:
             break
         else:
             if chess_board[piece_row][piece_column-(number)][0]=="  " or chess_board[piece_row][piece_column-(number)][0] in black_pieces:
                available_moves.append(chess_board[piece_row][piece_column-(number)][1])
                if chess_board[piece_row][piece_column-(number)][0] in black_pieces:
                    break
             else:
                break
    #yukarı gitme kontrol
        for number in range(1,8):
            if piece_row+number>8:
                break
            else:
                if chess_board[piece_row+(number)][piece_column][0]=="  " or chess_board[piece_row+(number)][piece_column][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column][1])
                    if chess_board[piece_row+(number)][piece_column][0] in black_pieces:
                        break
                else:
                    break
    #aşağı gitme kontrol
        for number in range(1,8):
            if piece_row-number<1:
                break
            else:
                if chess_board[piece_row-(number)][piece_column][0]=="  " or chess_board[piece_row-(number)][piece_column][0] in black_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column][1])
                    if chess_board[piece_row-(number)][piece_column][0] in black_pieces:
                        break
                else:
                    break

    if piece in["R1","R2"]:
    #sağa gitme kontrol
        for number in range (1,8):
            if piece_column+number>8:
                break
            else:
                if chess_board[piece_row][piece_column+(number)][0]=="  " or chess_board[piece_row][piece_column+(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row][piece_column+(number)][1])
                    if chess_board[piece_row][piece_column+(number)][0] in white_pieces:
                        break
                else:
                    break
    #sola gitme kontrol
        for number in range (1,8):
            if piece_column-number<1:
                break
            else:
                if chess_board[piece_row][piece_column-(number)][0]=="  " or chess_board[piece_row][piece_column-(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row][piece_column-(number)][1])
                    if chess_board[piece_row][piece_column-(number)][0] in white_pieces:
                        break
                else:
                        break
    #yukarı gitme kontrol
        for number in range(1,8):
            if piece_row+number>8:
                break
            else:
                if chess_board[piece_row+(number)][piece_column][0]=="  " or chess_board[piece_row+(number)][piece_column][0] in white_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column][1])
                    if chess_board[piece_row+(number)][piece_column][0] in white_pieces:
                        break
                else:
                        break
    #aşağı gitme kontrol
        for number in range(1,8):
            if piece_row-number<1:
                break
            else:
                if chess_board[piece_row-(number)][piece_column][0]=="  " or chess_board[piece_row-(number)][piece_column][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column][1])
                    if chess_board[piece_row-(number)][piece_column][0] in white_pieces:
                        break
                else:
                    break

    if piece in ["b1","b2"]:
    #our piece is a white bishop
    #sadece ileri gidebiliyor yani sağ çapraz ve sol çaprazı kontrol etmeliyiz
    
    #sağ üst kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column+number<=8:
                if chess_board[piece_row+(number)][piece_column+(number)][0]=="  " or chess_board[piece_row+(number)][piece_column+(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column+(number)][1])
                    if chess_board[piece_row+(number)][piece_column+(number)][0] in black_pieces:
                        break
                else:
                    break
    #sol üst kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column-number>=1:
                if chess_board[piece_row+(number)][piece_column-(number)][0]=="  " or chess_board[piece_row+(number)][piece_column-(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column-(number)][1])
                    if chess_board[piece_row+(number)][piece_column-(number)][0] in black_pieces:
                        break
                else:
                    break
    if piece in ["B1","B2"]:
    #our piece is a black bishop
    #sadece sağ alt çapraza ve sol alt çapraza gidebiliyor
    
    #sağ alt kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column+number<=8:
                if chess_board[piece_row-(number)][piece_column+(number)][0]=="  " or chess_board[piece_row-(number)][piece_column+(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column+(number)][1])
                    if chess_board[piece_row-(number)][piece_column+(number)][0] in white_pieces:
                        break
                else:
                    break
    #sol alt kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column-number>=1:
                if chess_board[piece_row-(number)][piece_column-(number)][0]=="  " or chess_board[piece_row-(number)][piece_column-(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column-(number)][1])
                    if chess_board[piece_row-(number)][piece_column-(number)][0] in white_pieces:
                        break
                else:
                    break

    if piece in ["qu"]:
    #our piece is a white queen
    #sağ üst-sol üst-üst-alt-sol alt-sağ alt hepsine gidebilir
    
    #yukarı kontrol
        for number in range(1,8):
            if piece_row+number<=8:
                if chess_board[piece_row+(number)][piece_column][0]=="  " or chess_board[piece_row+(number)][piece_column][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column][1])
                    if chess_board[piece_row+(number)][piece_column][0] in black_pieces:
                        break
            else:
                break
    #aşağı kontrol        
        for number in range (1,8):
            if piece_row-number>=1:
                if chess_board[piece_row-number][piece_column][0]=="  "or chess_board[piece_row-number][piece_column][0] in black_pieces:
                    available_moves.append(chess_board[piece_row-number][piece_column][1])
                    if chess_board[piece_row-number][piece_column][0] in black_pieces:
                        break
                else:
                    break
    #sağı kontrol
        for number in range(1,8):
            if piece_column+number<=8:
                if chess_board[piece_row][piece_column+number][0]=="  " or chess_board[piece_row][piece_column+number][0] in black_pieces:
                    available_moves.append(chess_board[piece_row][piece_column+number][1])
                    if chess_board[piece_row][piece_column+number][0] in black_pieces:
                        break
                else:
                    break
    
    #solu kontrol
    
        for number in range(1,8):
            if piece_column+number>=1:
                if chess_board[piece_row][piece_column-number][0]=="  " or chess_board[piece_row][piece_column-number][0] in black_pieces:
                    available_moves.append(chess_board[piece_row][piece_column-number][1])
                    if chess_board[piece_row][piece_column-number][0] in black_pieces:
                        break
                else:
                    break
    
    #sağ üstü kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column+number<=8:
                if chess_board[piece_row+(number)][piece_column+(number)][0]=="  " or chess_board[piece_row+(number)][piece_column+(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column+(number)][1])
                    if chess_board[piece_row+(number)][piece_column+(number)][0] in black_pieces:
                        break
                else:
                    break
    #sol üstü kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column-number>=1:
                if chess_board[piece_row+(number)][piece_column-(number)][0]=="  " or chess_board[piece_row+(number)][piece_column-(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column-(number)][1])
                    if chess_board[piece_row+(number)][piece_column-(number)][0] in black_pieces:
                        break
                else:
                    break
    #sağ altı kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column+number<=8:
                if chess_board[piece_row-(number)][piece_column+(number)][0]=="  " or chess_board[piece_row-(number)][piece_column+(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column+(number)][1])
                    if chess_board[piece_row-(number)][piece_column+(number)][0] in black_pieces:
                        break
                else:
                    break
    #sol altı kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column-number>=1:
                if chess_board[piece_row-(number)][piece_column-(number)][0]=="  " or chess_board[piece_row-(number)][piece_column-(number)][0] in black_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column-(number)][1])
                    if chess_board[piece_row-(number)][piece_column-(number)][0] in black_pieces:
                        break
                    else:
                        break

    if piece in ["QU"]:
    #our piece is a black queen
    #sağ üst-sol üst-üst-alt-sol alt-sağ alt hepsine gidebilir
    
    #yukarı kontrol
        for number in range(1,8):
            if piece_row+number<=8:
                if chess_board[piece_row+(number)][piece_column][0]=="  " or chess_board[piece_row+(number)][piece_column][0] in white_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column][1])
                    if chess_board[piece_row+(number)][piece_column][0] in white_pieces:
                        break
            else:
                break
    #aşağı kontrol        
        for number in range (1,8):
            if piece_row-number>=1:
                if chess_board[piece_row-number][piece_column][0]=="  "or chess_board[piece_row-number][piece_column][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-number][piece_column][1])
                    if chess_board[piece_row-number][piece_column][0] in white_pieces:
                        break
                else:
                    break
    #sağı kontrol
        for number in range(1,8):
            if piece_column+number<=8:
                if chess_board[piece_row][piece_column+number][0]=="  " or chess_board[piece_row][piece_column+number][0] in white_pieces:
                    available_moves.append(chess_board[piece_row][piece_column+number][1])
                    if chess_board[piece_row][piece_column+number][0] in white_pieces:
                        break
                else:
                    break
    
    #solu kontrol
    
        for number in range(1,8):
            if piece_column+number>=1:
                if chess_board[piece_row][piece_column-number][0]=="  " or chess_board[piece_row][piece_column-number][0] in white_pieces:
                    available_moves.append(chess_board[piece_row][piece_column-number][1])
                    if chess_board[piece_row][piece_column-number][0] in white_pieces:
                        break
                else:
                    break
    
    #sağ üstü kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column+number<=8:
                if chess_board[piece_row+(number)][piece_column+(number)][0]=="  " or chess_board[piece_row+(number)][piece_column+(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column+(number)][1])
                    if chess_board[piece_row+(number)][piece_column+(number)][0] in white_pieces:
                        break
                else:
                    break
    #sol üstü kontrol
        for number in range(1,8):
            if piece_row+number<=8 and piece_column-number>=1:
                if chess_board[piece_row+(number)][piece_column-(number)][0]=="  " or chess_board[piece_row+(number)][piece_column-(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row+(number)][piece_column-(number)][1])
                    if chess_board[piece_row+(number)][piece_column-(number)][0] in white_pieces:
                        break
                else:
                    break
    #sağ altı kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column+number<=8:
                if chess_board[piece_row-(number)][piece_column+(number)][0]=="  " or chess_board[piece_row-(number)][piece_column+(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column+(number)][1])
                    if chess_board[piece_row-(number)][piece_column+(number)][0] in white_pieces:
                        break
                else:
                    break
    #sol altı kontrol
        for number in range(1,8):
            if piece_row-number>=1 and piece_column-number>=1:
                if chess_board[piece_row-(number)][piece_column-(number)][0]=="  " or chess_board[piece_row-(number)][piece_column-(number)][0] in white_pieces:
                    available_moves.append(chess_board[piece_row-(number)][piece_column-(number)][1])
                    if chess_board[piece_row-(number)][piece_column-(number)][0] in white_pieces:
                        break
                else:
                    break

    if piece in ["n1","n2"]:
    #our piece is a white knight
    
        if piece_row+2<=8 and piece_column+1<=8:
            if chess_board[piece_row+2][piece_column+1][0]=="  " or chess_board[piece_row+2][piece_column+1][0] in black_pieces:
                available_moves.append(chess_board[piece_row+2][piece_column+1][1])
            
    
        if piece_row+2<=8 and piece_column-1>=1:
            if chess_board[piece_row+2][piece_column-1][0]=="  " or chess_board[piece_row+2][piece_column-1][0] in black_pieces:
                available_moves.append(chess_board[piece_row+2][piece_column-1][1])
            
        
        if piece_row+1<=8 and piece_column+2<=8:
            if chess_board[piece_row+1][piece_column+2][0]=="  " or chess_board[piece_row+1][piece_column+2][0] in black_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column+2][1])
        
        
        if piece_row+1<=8 and piece_column-2>=1:
            if chess_board[piece_row+1][piece_column-2][0]=="  " or chess_board[piece_row+1][piece_column-2][0] in black_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column-2][1])
        
    
        if piece_row-2>=1 and piece_column-1>=1:
            if chess_board[piece_row-2][piece_column-1][0]=="  " or chess_board[piece_row-2][piece_column-1][0] in black_pieces:
                available_moves.append(chess_board[piece_row-2][piece_column-1][1])
        
        
        if piece_row-1>=1 and piece_column-2>=1:
            if chess_board[piece_row-1][piece_column-2][0]=="  " or chess_board[piece_row-1][piece_column-2][0] in black_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column-2][1])
        
    
        if piece_row-2>=1 and piece_column+1<=8:
            if chess_board[piece_row-2][piece_column+1][0]=="  " or chess_board[piece_row-2][piece_column+1][0] in black_pieces:
                available_moves.append(chess_board[piece_row-2][piece_column+1][1])
        
    
        if piece_row-1>=1 and piece_column+2<=8:
            if chess_board[piece_row-1][piece_column+2][0]=="  " or chess_board[piece_row-1][piece_column+2][0] in black_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column+2][1])
        
        
        if piece_row+1<=8 and piece_column-1>=1:
        
            if chess_board[piece_row+1][piece_column-1][0]=="  ":
                available_moves.append(chess_board[piece_row+1][piece_column-1][1])
        
        
        if piece_row+1<=8 and piece_column+1<=8:
            if chess_board[piece_row+1][piece_column+1][0]=="  ":
                available_moves.append(chess_board[piece_row+1][piece_column+1][1])
        
    
        if piece_row-1>=1 and piece_column-1>=1:
            if chess_board[piece_row-1][piece_column-1][0]=="  ":
                available_moves.append(chess_board[piece_row-1][piece_column-1][1])
        
        
        if piece_row-1>=1 and piece_column+1<=8:
            if chess_board[piece_row-1][piece_column+1][0]=="  ":
                available_moves.append(chess_board[piece_row-1][piece_column+1][1])
        
    
    
    
        

    if piece in ["N1","N2"]:
    #our piece is a black knight
    
        if piece_row+2<=8 and piece_column+1<=8:
            if chess_board[piece_row+2][piece_column+1][0]=="  " or chess_board[piece_row+2][piece_column+1][0] in white_pieces:
                available_moves.append(chess_board[piece_row+2][piece_column+1][1])
            
    
        if piece_row+2<=8 and piece_column-1>=1:
            if chess_board[piece_row+2][piece_column-1][0]=="  " or chess_board[piece_row+2][piece_column-1][0] in white_pieces:
                available_moves.append(chess_board[piece_row+2][piece_column-1][1])
            
        
        if piece_row+1<=8 and piece_column+2<=8:
            if chess_board[piece_row+1][piece_column+2][0]=="  " or chess_board[piece_row+1][piece_column+2][0] in white_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column+2][1])
        
        
        if piece_row+1<=8 and piece_column-2>=1:
            if chess_board[piece_row+1][piece_column-2][0]=="  " or chess_board[piece_row+1][piece_column-2][0] in white_pieces:
                available_moves.append(chess_board[piece_row+1][piece_column-2][1])
        
    
        if piece_row-2>=1 and piece_column-1>=1:
            if chess_board[piece_row-2][piece_column-1][0]=="  " or chess_board[piece_row-2][piece_column-1][0] in white_pieces:
                available_moves.append(chess_board[piece_row-2][piece_column-1][1])
        
        
        if piece_row-1>=1 and piece_column-2>=1:
            if chess_board[piece_row-1][piece_column-2][0]=="  " or chess_board[piece_row-1][piece_column-2][0] in white_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column-2][1])
        
    
        if piece_row-2>=1 and piece_column+1<=8:
            if chess_board[piece_row-2][piece_column+1][0]=="  " or chess_board[piece_row-2][piece_column+1][0] in white_pieces:
                available_moves.append(chess_board[piece_row-2][piece_column+1][1])
        
    
        if piece_row-1>=1 and piece_column+2<=8:
            if chess_board[piece_row-1][piece_column+2][0]=="  " or chess_board[piece_row-1][piece_column+2][0] in white_pieces:
                available_moves.append(chess_board[piece_row-1][piece_column+2][1])
                
        if piece_row+1<=8 and piece_column-1>=1:
            if chess_board[piece_row+1][piece_column-1][0]=="  ":
                available_moves.append(chess_board[piece_row+1][piece_column-1][1])
        
        
        if piece_row+1<=8 and piece_column+1<=8:
            if chess_board[piece_row+1][piece_column+1][0]=="  ":
                available_moves.append(chess_board[piece_row+1][piece_column+1][1])
        
    
        if piece_row-1>=1 and piece_column-1>=1:
            if chess_board[piece_row-1][piece_column-1][0]=="  ":
                available_moves.append(chess_board[piece_row-1][piece_column-1][1])
        
        
        if piece_row-1>=1 and piece_column+1<=8:
            if chess_board[piece_row-1][piece_column+1][0]=="  ":
                available_moves.append(chess_board[piece_row-1][piece_column+1][1])
        
    

    
    return available_moves

def move(piece,position):
    
    available_moves=show_moves(piece)
    position_row=position_row_finder(position)
    position_column=position_column_finder(position)
    piece_row=piece_row_finder(piece)
    piece_column=piece_column_finder(piece)
    if position in available_moves:
        print("OK")
        chess_board[position_row][position_column][0]=piece
        chess_board[piece_row][piece_column][0]="  "
    else:
        print("FAILED")


initialize()




        
f1=open(sys.argv[1],"r")
userin=(f1.read().splitlines())

for item in userin:
    mylist=item.split()
    
    if mylist[0]=="move":
        print(f'> {mylist[0]} {mylist[1]} {mylist[2]}')
        
        move(mylist[1],mylist[2])
    
    if mylist[0]=="print":
        print("> print")
        print_board()
    
    if mylist[0]=="showmoves":
        print(f"> showmoves {mylist[1]}")
        move_list=show_moves(mylist[1])
        move_list.sort()
        if len(move_list)==0:
            print("FAILED")
        else:
            for item in move_list:
                print(item,end=" ")
        print("")
        
    if mylist[0]=="initialize":
        print("> initialize \nOK ")
        initialize()
        print_board()
    
    if mylist[0]=="exit":
        print("> exit")
        break

f1.close()
        
            
                        

