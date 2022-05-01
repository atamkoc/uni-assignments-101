import sys



class parameterNumber(Exception):
    pass

class undefinedParameter(Exception):
    pass

class inputFileCouldNotBeRead(Exception):
    pass

class inputFileisEmpty(Exception):
    pass

class invalidCharacterInput(Exception):
    pass

class keyFileCouldNotBeRead(Exception):
    pass

class keyFileisEmpty(Exception):
    pass

class keyFileInvalidChar(Exception):
    pass


try:
    if len(sys.argv)!=5:
        raise parameterNumber               #parameter number error
    if sys.argv[1] not in ["enc","dec"]: 
        raise undefinedParameter            #undefined parameter error
    if sys.argv[3].split(".")[1]!="txt":
        raise inputFileCouldNotBeRead       #input file could not be read error
    
    f1=open(sys.argv[3],"r")
    user_input=f1.read()
    
    if user_input=="":
        raise inputFileisEmpty              #input file is empty error
    
    if sys.argv[1]=="enc":
        for char in user_input:
            if char.upper() not in ["A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]:
                raise invalidCharacterInput    #input invalid character error
        
    if sys.argv[2]=="dec":
        for char in user_input:
            if not char.isnumeric() and char!=",":
                raise invalidCharacterInput
    
    
    if sys.argv[2].split(".")[1]!="txt":
        raise keyFileCouldNotBeRead
    
    f2=open(sys.argv[2],"r")
    user_key=f2.read().splitlines()
    
    
    
    if len(user_key)==0:
        raise keyFileisEmpty
    
 
    for item in user_key:
        for char in item:
            if not char.isnumeric() and char!="," and char!=" ":
                raise keyFileInvalidChar
            
            #if not char.isnumeric() or char!="," or char!=" ":
             #   raise keyFileInvalidChar
               
except parameterNumber:
    print("Parameter number")
    sys.exit()

except undefinedParameter:
    print("Undefined parameter")
    sys.exit()

except inputFileCouldNotBeRead:
    print("Input file could not be read")
    sys.exit()

except inputFileisEmpty:
    print("Input file is empty")
    sys.exit()
    

except invalidCharacterInput:
    print("Invalid character in input file")
    sys.exit()


except keyFileCouldNotBeRead:
    print("Key file could not be read")
    sys.exit()

except keyFileisEmpty:
    print("Key file is empty")
    sys.exit()


except keyFileInvalidChar:
    print("Invalid character in key file")
    sys.exit()


except FileNotFoundError as x:
    
    if (x.filename.split("/")[-1])=="plain_input.txt":
         print("Input file not found")
         sys.exit()
    if (x.filename.split("/")[-1])=="key.txt":
        print("Key file not found")
        sys.exit()
    if (x.filename.split("/")[-1])=="ciphertext.txt":
        print("Input file not found : ciphertext.txt")
         

operation_type=sys.argv[1]
key=[]
for item in user_key:
    temp_list=item.split(",")
    temp_list2=[]
    for item in temp_list:
        temp_list2.append(int(item))
    
    key.append(temp_list2)


def string_splitter(message,n):
    #splits the result for nxn key and fills empty characters with space (as a list)
    result=[]
    for i in range(0, len(message), n):
        result.append(message[i : i + n])
    while len(result[-1])<n:
        result[-1]=result[-1]+" "
    return result

def number_replacer(message):
    #turns splitted strings into arbitrary numbers and creates a matrix
    number_list=[]
    for item in message:
        for char in item:
            if char in ["a","A"]:
                number_list.append([1])
            if char in ["b","B"]:
                number_list.append([2])
            if char in ["c","C"]:
                number_list.append([3])
            if char in ["d","D"]:
                number_list.append([4])
            if char in ["e","E"]:
                number_list.append([5])
            if char in ["f","F"]:
                number_list.append([6])
            if char in ["g","G"]:
                number_list.append([7])
            if char in ["h","H"]:
                number_list.append([8])
            if char in ["i","I","ı","İ"]:
                number_list.append([9])
            if char in ["j","J"]:
                number_list.append([10])
            if char in ["k","K"]:
                number_list.append([11])
            if char in ["l","L"]:
                number_list.append([12])
            if char in ["m","M"]:
                number_list.append([13])
            if char in ["n","N"]:
                number_list.append([14])
            if char in ["o","O"]:
                number_list.append([15])
            if char in ["p","P"]:
                number_list.append([16])
            if char in ["q","Q"]:
                number_list.append([17])
            if char in ["r","R"]:
                number_list.append([18])
            if char in ["s","S"]:
                number_list.append([19])
            if char in ["t","T"]:
                number_list.append([20])
            if char in ["u","U"]:
                number_list.append([21])
            if char in ["v","V"]:
                number_list.append([22])
            if char in ["w","W"]:
                number_list.append([23])
            if char in ["x","X"]:
                number_list.append([24])
            if char in ["y","Y"]:
                number_list.append([25])
            if char in ["z","Z"]:
                number_list.append([26])
            if char in [" "]:
                number_list.append([27])
    return(number_list)

number_matrice=list(map(number_replacer,string_splitter(user_input,len(key))))

def empty_matrice_creator(key,number_matrice):
    #creates an empty matrix
    temp_list=[]
    x=len(key)
    y=len(number_matrice[0])
    
    for number in range(0,x):
        temp_list.append([0]*y)
    return temp_list

def matrice_multiplier(key,number_matrice):
    result=empty_matrice_creator(key, number_matrice)
    for i in range(len(key)):
       for j in range(len(number_matrice[0])):
           for k in range(len(number_matrice)):
               result[i][j] += key[i][k] * number_matrice[k][j]
    return result

#inverse matrix
"""
how to take the inverse of an nxn matrix
main source I have used to create the algorithm to take the inverse: https://www.youtube.com/watch?v=kWorj5BBy9k&list=WL&index=127&ab_channel=ProfessorDaveExplains
https://www.mathsisfun.com/algebra/matrix-inverse.html#:~:text=To%20find%20the%20inverse%20of,determinant%20(ad%2Dbc).
a matrix times its inverse will end up as an identity matrix which has all ones on their diagonal and all the other places are 0.
so the inverse of an any invertible 2x2 matrix([[a,b],[c,d]]) is 1/(determinant)*  ([[d,-b],[-c,a]])


1)to find the inverse of an any inversible matrix we need to generate the matrix of minors first

    for every number in a matrix:
        we block all the numbers in its row and the column and take the other elements determinant
        after that, we place the result we found to the place of the number we blocked

2)we generate the matrix of cofactors by multiplying the minors matrix by matrix of cofactors
        



3)after we find the matrix of minors we take its adjuguate
    to take the adjugate we keep the numbers in the matrix's corners and centers
    and swap every number with number at his diagonal

4) as the last step we divide every number in our matrix with our determinant

    

"""





def matrix_minor_getter(key,x,y):
    #(x,y)th minor of a matrix of size n is a smaller matrix of size n-1 with the x'th row and y'th column deleted.
    return [row[:y] + row[y+1:] for row in (key[:x]+key[x+1:])]




def matrix_determinant_finder(key):

    if len(key) == 2:
        return key[0][0]*key[1][1]-key[0][1]*key[1][0]

    determinant = 0
    for c in range(len(key)):
        determinant += ((-1)**c)*key[0][c]*matrix_determinant_finder(matrix_minor_getter(key,0,c))
    
    return determinant

"""
inverse of a 2x2 matrix [[a,b],[c,d]] is (1/determinant)* [[d,-b],[-c,a]]

daha büyük matrisler için 2x2'ye indirgeyerek işlem yapacağız bunun için de recursion kullanacağız


"""
#köşedekiler ve merkezdeki aynı kalır
#diğerleri çapraz yer değiştirir
def adjugate_getter(key):
    
    adjugate=list(zip(*key))
    adjugate2=[]
    for item in adjugate:
        adjugate2.append(list(item))
    return (adjugate2)


def matrix_inverser(key):
    determinant = matrix_determinant_finder(key)
    

    if len(key) == 2:
        two_by_two_determinant=[]
        two_by_two_determinant.append([key[1][1]/determinant, (-1)*key[0][1]/determinant])
        two_by_two_determinant.append([(-1)*key[1][0]/determinant, key[0][0]/determinant])
        
        return two_by_two_determinant

    #teker teker minorlarını hesaplayıp cofactor + - + dizilimine göre cofactor matrisini oluşturur
    # sıra+satır sayısı çift ise 1 ile çarpar değilse -1 ile çarpar
    temp_list=[]
    for number in range(0,len(key)):
        temp_list2=[]
        for number2 in range(0,len(key)):
            minor=matrix_minor_getter(key, number, number2)
            temp_list2.append(((-1)**(number+number2)) * matrix_determinant_finder(minor))
        
        
        temp_list.append(temp_list2)
     

    
    
    #şimdi adjugateleri almak gerekiyor
    #köşedekiler ve merkezdeki aynı kalır
    #diğerleri çapraz yer değiştirir
    
    #her bir sayıyı determinanta bölüyoruz 
    temp_list=adjugate_getter(temp_list)
    for x in range(len(temp_list)):
        for y in range(len(temp_list)):
            temp_list[x][y] = temp_list[x][y]/determinant
    
    return temp_list
    #sonucu return ediyoruz



#inverse matrix

def decoded_to_text(decoded_result):
    message=""
    for x in decoded_result:
        for y in x:
            for z in y:
                if int (z)==1:
                    message=message+"A"
                if int (z)==2:
                    message=message+"B"
                if int (z)==3:
                    message=message+"C"
                if int (z)==4:
                    message=message+"D"
                if int (z)==5:
                    message=message+"E"
                if int (z)==6:
                    message=message+"F"
                if int (z)==7:
                    message=message+"G"
                if int (z)==8:
                    message=message+"H"
                if int (z)==9:
                    message=message+"I"
                if int (z)==10:
                    message=message+"J"
                if int (z)==11:
                    message=message+"K"
                if int (z)==12:
                    message=message+"L"
                if int (z)==13:
                    message=message+"M"
                if int (z)==14:
                    message=message+"N"
                if int (z)==15:
                    message=message+"O"
                if int (z)==16:
                    message=message+"P"
                if int (z)==17:
                    message=message+"Q"
                if int (z)==18:
                    message=message+"R"
                if int (z)==19:
                    message=message+"S"
                if int (z)==20:
                    message=message+"T"
                if int (z)==21:
                    message=message+"U"
                if int (z)==22:
                    message=message+"V"
                if int (z)==23:
                    message=message+"W"
                if int (z)==24:
                    message=message+"X"
                if int (z)==25:
                    message=message+"Y"
                if int (z)==26:
                    message=message+"Z"
                if int (z)==27:
                    message=message+" "
    return message



if operation_type=="enc":
    enc_file=open(sys.argv[4],"w+")
    number_matrice=list(map(number_replacer,string_splitter(user_input,len(key))))
    encoded_list=[]
    enc_message_str=""

    for item in number_matrice:
        encoded_list.append(matrice_multiplier(key, item))

    for x in encoded_list:
        for y in x:
            for z in y:
                    enc_message_str=enc_message_str+f'{z},'
    
    enc_message_str=enc_message_str[:-1]
    enc_file.write(enc_message_str)
    enc_file.close()

if operation_type=="dec":
    dec_file=open(sys.argv[4],"w+")
    inverse_key=matrix_inverser(key)
    decode_string=user_input+","
    decode_string=decode_string[:-1].split(",")
    decode_string=[[int(x)] for x in decode_string]
    decode_matrix=[decode_string[i:i+len(key)] for i in range(0,len(decode_string), len(key))]
    
    
    decode_result=[]
    
    
    for item in decode_matrix:
        decode_result.append(matrice_multiplier(inverse_key, item))
    


    
    dec_file.write(decoded_to_text(decode_result))
    dec_file.close()
    
  





        


    
