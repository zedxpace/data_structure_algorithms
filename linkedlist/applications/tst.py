##denotes the height of ith building from LEFT
height_of_building = [ 4,3 ,4 ,1 ,2 ,1]

##it needs to be assumed that am standing b/w Kth and (K+1)th position
K = 0

curr_visible = 0
curr_K = 0

visible = 0
K = 0
position_to_remove = []

position = []
for i in range(len(height_of_building)-1):
    J = i
    position_to_remove = []
    visible = 0
    prev_building = -1
    K = 0

    ##iterate forward 
    '''
    iterate frontwards in order check howmany buildings are visible 
    and save the position of buildings can be removed which are blocking 
    the visiblity for other building
    '''
    while J < len(height_of_building)-1:  
        if height_of_building[i] >= height_of_building[J+1] and height_of_building[J+1] >= prev_building:
            visible += 1
            K = i
        else:
            position_to_remove.append(J)
        prev_building = height_of_building[J+1]
        J+=1

    #iterate BACKWARDS
    '''
    iterate towards 0th position of array in order to identify how many current building are visisble 
    backwards of array from current ith position 
    '''
    J = i
    prev_building = -1
    while J > 0:
        if height_of_building[i] >= height_of_building[J-1] and height_of_building[J-1] >= prev_building:
            visible += 1
            K = i
        else:
            position_to_remove.append(J)
        prev_building = height_of_building[J-1]

        J-=1
    
    #verify for the current building if it needs to be removed or not 
    '''
    if height of current (ith) building is greater then (i-1) building or (i+1) building
    then it means it is blocking the person to view rest of the building 
    so remove it .
    '''
    if i != 0 and i != len(height_of_building) -1:
        if height_of_building[i] > height_of_building[i-1] or height_of_building[i] > height_of_building[i+1]:
            position_to_remove.append(i)
    
    if visible > curr_visible:
        curr_visible = visible
        curr_K = i
        tmp = height_of_building
        for i in position_to_remove:
            tmp[i] = '*'
        #print(tmp)
    print(str(i) +"th loops ends here")

print("person should stand between %d : " ,(curr_K , curr_K+1))
print("visible : " ,curr_visible)
print(tmp)
#print("person should stand at building with value : %d"%height_of_building[curr_K]) 
        
