n = int(input())
for i in range(1,n+1):
    count = 0
    top_row = list(map(int,input().split()))
    middle_row = list(map(int,input().split()))
    bottow_row = list(map(int,input().split()))
    middle_row.insert(1,0)
    diff = top_row[0]-top_row[1]
    diff2 = top_row[1]-top_row[2]
    if diff==diff2:
        count+=1
    diff = bottow_row[0]-bottow_row[1]
    diff2 = bottow_row[1]-bottow_row[2]
    if diff==diff2:
        count+=1
    diff = top_row[0]-middle_row[0]
    diff2 = middle_row[0]-bottow_row[0]
    if diff==diff2:
        count+=1
    diff = top_row[2]-middle_row[2]
    diff2 = middle_row[2]-bottow_row[2]
    if diff==diff2:
        count+=1
    array_num = [top_row,middle_row,bottow_row]
    list_of_cord = [(0,0),(1,0),(2,0),(0,1)]
    list_of_cord2 = [(2,2),(1,2),(0,2),(2,1)]
    list_of_possible_num = []
    for j in range(4):
        pos = list_of_cord[j]
        pos2 = list_of_cord2[j]
        diff = int((array_num[pos[0]][pos[1]] - array_num[pos2[0]][pos2[1]])/2)
        if diff > 0:
           list_of_possible_num.append(array_num[pos[0]][pos[1]] - diff)
        else:
            list_of_possible_num.append(array_num[pos[0]][pos[1]] - diff)
    middle_value = 0
    prev_count = 0
    for num in list_of_possible_num:
        if num is not middle_value:
            if prev_count < list_of_possible_num.count(num):
                prev_count = list_of_possible_num.count(num)
                middle_value = num
        else:
            continue
    array_num[1][1] = middle_value
    print(count)
    count+= list_of_possible_num.count(middle_value)
    print(list_of_possible_num)
    print("case #{}".format(i),count)




