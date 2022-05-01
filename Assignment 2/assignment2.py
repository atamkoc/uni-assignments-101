userin_map=(input("Please enter feeding map as a list:\n")).strip()
userin_map=eval(userin_map)


row_count=0
column_count=0

for item in userin_map:
    row_count=row_count+1
    


for item in userin_map[0]:
    column_count=column_count+1
    


def print_board(input_user_map):
    for item in input_user_map:
        print(*item)


player_points=0
user_in_move_list = (input("Please enter direction of movements as a list:\n")) 
move_list=[]
print("Your board is:")
print_board(userin_map)
for char in user_in_move_list:
    if char!="," and char!="]" and char!="[" and char!=" " and char!="'" and char!='"':
        move_list.append(char)


for direction in move_list:
    current_column=0
    for item in userin_map:
        if '*' in item:
            rabbit_position=item.index("*")
            break
        else:
            current_column=current_column+1
        
    if direction=="U":
        if current_column>0 and userin_map[current_column-1][rabbit_position]!="W":
            if userin_map[current_column-1][rabbit_position]=="P":
                userin_map[current_column-1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                break
                    
            elif userin_map[current_column-1][rabbit_position]=="A":
                userin_map[current_column-1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points+5
                    
            elif userin_map[current_column-1][rabbit_position]=="M":
                userin_map[current_column-1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points-5
                
            elif userin_map[current_column-1][rabbit_position]=="C":
                userin_map[current_column-1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points+10
                
            else:
                userin_map[current_column-1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points+0
        
    if direction=="D":
        if current_column<column_count and userin_map[current_column+1][rabbit_position]!="W":
            if userin_map[current_column+1][rabbit_position]=="P":
                userin_map[current_column+1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                break
                
            elif userin_map[current_column+1][rabbit_position]=="A":
                userin_map[current_column+1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points+5
                    
            elif userin_map[current_column+1][rabbit_position]=="M":
                userin_map[current_column+1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points-5
                    
            elif userin_map[current_column+1][rabbit_position]=="C":
                userin_map[current_column+1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                player_points=player_points+10
            
            else:
                userin_map[current_column+1][rabbit_position] = "*"
                userin_map[current_column][rabbit_position] = "X"
                playe_rpoints=player_points+0
                    
    if direction=="R":
        if rabbit_position<row_count-1 and userin_map[current_column][rabbit_position + 1] != "W":
             if userin_map[current_column][rabbit_position+1]=="P":
                 userin_map[current_column][rabbit_position+1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 break
                
             elif userin_map[current_column][rabbit_position+1]=="A":
                 userin_map[current_column][rabbit_position+1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+5
                    
             elif userin_map[current_column][rabbit_position+1]=="M":
                 userin_map[current_column][rabbit_position+1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points-5
                    
             elif userin_map[current_column][rabbit_position+1]=="C":
                 userin_map[current_column][rabbit_position+1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+10
            
             else:
                 userin_map[current_column][rabbit_position+1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+0  
                    
    if direction=="L":
        if rabbit_position>0  and userin_map[current_column][rabbit_position - 1] != "W":
             if userin_map[current_column][rabbit_position-1]=="P":
                 userin_map[current_column][rabbit_position-1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 break
                
             elif userin_map[current_column][rabbit_position-1]=="A":
                 userin_map[current_column][rabbit_position-1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+5
                    
             elif userin_map[current_column][rabbit_position-1]=="M":
                 userin_map[current_column][rabbit_position-1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points-5
                    
             elif userin_map[current_column][rabbit_position-1]=="C":
                 userin_map[current_column][rabbit_position-1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+10
            
             else:
                 userin_map[current_column][rabbit_position-1] = "*"
                 userin_map[current_column][rabbit_position] = "X"
                 player_points=player_points+0 


print("Your output should be like this:")
print_board(userin_map)
print(f'Your score is: {player_points}')

