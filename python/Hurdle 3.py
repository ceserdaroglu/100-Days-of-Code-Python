def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
#front_is_clear() or wall_in_front(), at_goal()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
