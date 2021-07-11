def isArithmeticSquare(a,b,c):
    return a-b==b-c

def findArithmeticSquare(Arithmetic_array):
    count = 0
    for  i in range(3):
        if isArithmeticSquare(Arithmetic_array[i][0],Arithmetic_array[i][1],Arithmetic_array[i][2]):
            count+=1
        if isArithmeticSquare(Arithmetic_array[0][i],Arithmetic_array[1][i],Arithmetic_array[2][i]):
            count+=1
    if isArithmeticSquare(Arithmetic_array[0][0],Arithmetic_array[1][1],Arithmetic_array[2][2]):
        count+=1
    if isArithmeticSquare(Arithmetic_array[0][2],Arithmetic_array[1][1],Arithmetic_array[2][0]):
        count+=1
    return count


n = int(input())
for i in range(1,n+1):
    top_row = list(map(int,input().split()))
    mid_row = list(map(int,input().split()))
    bot_row = list(map(int,input().split()))
    mid_row.insert(1,0)
    Arithmetic_array = [top_row,mid_row,bot_row]
    list_of_cord1 = [(0,0),(1,0),(2,0),(2,1)]
    list_of_cord2 = [(2,2),(1,2),(0,2),(0,1)]
    possible_mids = []
    for j in range(4):
        pos1x,pos1y = list_of_cord1[j]
        pos2x,pos2y = list_of_cord2[j]
        diff = int((Arithmetic_array[pos1x][pos1y] - Arithmetic_array[pos2x][pos2y])/2)
        mid_value = (Arithmetic_array[pos1x][pos1y]-diff)
        possible_mids.append(mid_value)
    max_mid = 0
    count = 0
    for value in possible_mids:
        current_count = possible_mids.count(value)
        if current_count>count:
            max_mid = value
            count = current_count
    Arithmetic_array[1][1] = max_mid        
    previous = findArithmeticSquare(Arithmetic_array)
    print("Case #{}: ".format(i),previous)
