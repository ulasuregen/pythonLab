def separateSquares(squares):
    total_area = sum([l[2]**2 for l in squares])
    half_area = total_area / 2
    
    up = max([s[1]+s[2] for s in squares])
    down = 0

    # Calculateing the area under the horizontal line 
    # [s[0]*min(y - s[1], s[2]) for s in squares if s[1] < y]
    y = up / 2
    step_size = up / 4
    
    while step_size > 1e-5:
        under_area = sum([s[2]* min(y - s[1], s[2]) for s in squares if s[1] < y])

        if under_area >= half_area:
            y -= step_size
        else:
            y += step_size
        
        step_size /= 2

    return y

squares = [[0,0,2],[1,1,1]]
print( separateSquares(squares) )