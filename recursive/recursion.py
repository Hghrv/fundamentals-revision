def ghost_buster(ghosts):
    ghost_counter = 0
    for ghost in ghosts:
        if type(ghost) == dict and (ghost['is_ghost']):
            ghost_counter += 1
        elif type(ghost) == list:
            #recursion until base case
            ghost_counter += ghost_buster(ghost)    
    return ghost_counter

    r