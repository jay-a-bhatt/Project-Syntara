# This code creates a classic pipe connecting minigame in Ren'Py.
# The player must rotate pipe pieces to form a continuous path from a start point to an end point.

# --- Global Variables ---
# These variables define the structure and state of the game.

default pipe_rows = 4 # How many rows the pipes should be divided into.
default pipe_columns = 4 # How many columns the pipes should be divided into.
default amount_of_pipes = pipe_rows * pipe_columns # Total amount of pipes to show in the mini-game.
default grid_path = [] # A list that will be filled with cells of the grid which forms a path from start to end.
default pipes = [] # A list that will be filled with list items containing information about each pipe in the game.
default pipe_types = {"straight" : ("top", "bottom"), "curved" : ("right", "bottom"), "t" : ("top", "bottom", "left"), "cross": ("top", "bottom", "left", "right")} # Dictionary containing information about each pipe-type and in which directions their end-points go initially.
default connected_pipes = [] # Keeps a track of the pipes that have been strung together.


# --- Python Functions ---
# This block contains all the logic for setting up, running, and checking the minigame.
init python:
    def setup_pipe_game():
        # Function which sets up the pipe mini-game.
        # You call this function whenever you want to setup a new game.
        global pipes
        global connected_pipes
        
        # Reset the pipes and connected_pipes list to empty lists, so we can fill them with new pipes.
        pipes = []
        connected_pipes = []
        
        # Generate a grid path from start to end.
        generate_grid_path()
        
        # Now we fill the pipes list with pipes. Needs to happen after we have generated a grid path.
        create_pipes()

    def create_pipe(type, cell):
        # Function that creates information about an individual pipe.
        pipe_image = "pipe_game_img/%s-pipe.png" % type # Create the image-path to the pipe. # Create the image-path to the pipe.
        pipe_end_points = list(pipe_types[type]) # Get all the end-points the pipe type has.
        final_pipe = [pipe_image, type, pipe_end_points, cell, 0] # 1: image, 2: type of pipe, 3: its end-points, 4: which cell, 5: rotation
        pipes.append(final_pipe) # Add the list "final_pipe" into the "pipes" list.

    def generate_grid_path():
        global grid_path
        # Function to generate a path of cells in the grid from start to end where the path might lead: right or down.
        # This path will be ONE valid way of connecting the pipes, but there might be more depending on what random pipes were generated.
        # We need to generate at least one correct path in case the random pipes does not allow for a valid path to be made.
        
        grid_path = [1] # We start with adding the first cell to the path, as this is where it starts.
        
        for i in range(pipe_columns + pipe_rows - 2):
            if grid_path[-1] % pipe_columns == 0 and grid_path[-1] <= amount_of_pipes - pipe_columns:
                # The previous cell in the path list is in the last column, but not in the last row.
                # The following cell can only be below.
                grid_path.append(grid_path[-1] + pipe_columns)
            
            elif grid_path[-1] % pipe_columns != 0 and grid_path[-1] <= amount_of_pipes - pipe_columns:
                # The previous cell is before the last column, and not in the last row.
                # This cell can be followed by a cell to the right or below.
                potential_cells = ["right", "down"]
                random_pick = renpy.random.choice(potential_cells)
                
                if random_pick == "right":
                    grid_path.append(grid_path[-1] + 1)
                elif random_pick == "down":
                    grid_path.append(grid_path[-1] + pipe_columns)
            
            elif grid_path[-1] > amount_of_pipes - pipe_columns:
                # The previous cell is in the last row.
                # The following cell can only be to the right.
                grid_path.append(grid_path[-1] + 1)

    def create_pipes():
        # Function to fill the pipes list with different types of pipes, according to the generated path.
        # Where there isn't a cell in the path, a random pipe will be generated instead.
        for i in range(1, amount_of_pipes + 1):
            if i == 1:
                # We'll create the first pipe in the grid first.
                if grid_path[0] + 1 == grid_path[1]:
                    # The next cell in the path is to the right.
                    # This cell needs a straight pipe.
                    create_pipe(type = "straight", cell = i)
                elif grid_path[0] + pipe_columns == grid_path[1]:
                    # The next cell in the path is below.
                    # This cell needs a curved pipe.
                    create_pipe(type = "curved", cell = i)
            
            elif i > 1 and i < amount_of_pipes:
                # This is the second or more iteration of the loop, but not the last.
                if i in grid_path:
                    # "i" is a cell in the grid_path list, which means we need a specific pipe-type in this cell to form a path.
                    current_cell_index = grid_path.index(i)
                    next_cell_index = current_cell_index + 1
                    prev_cell_index = current_cell_index - 1
                    
                    if grid_path[current_cell_index] % pipe_columns == 1:
                        # This cell is the first in its row, but not the first in the grid. That means that the previous cell must have been above.
                        if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                            # The next cell in the path is to the right.
                            create_pipe(type = "curved", cell = grid_path[current_cell_index])
                        elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                            # Next cell in the path is below.
                            create_pipe(type = "straight", cell = grid_path[current_cell_index])
                    
                    elif grid_path[current_cell_index] % pipe_columns == 0 and grid_path[current_cell_index] <= pipe_columns:
                        # This cell is the last cell in row 1. That means the previous cell was to the right and the next cell is below.
                        create_pipe(type = "curved", cell = grid_path[current_cell_index])
                    
                    elif grid_path[current_cell_index] % pipe_columns == 0 and grid_path[current_cell_index] > pipe_columns:
                        # This cell is the last cell in any row below 1 but above the last row.
                        if grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:
                            # The previous cell in the path is above.
                            create_pipe(type = "straight", cell = grid_path[current_cell_index])
                        elif grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:
                            # The previous cell was to the left.
                            create_pipe(type = "curved", cell = grid_path[current_cell_index])
                    
                    else:
                        # This cell is between the first and last cell in it's row.
                        if grid_path[current_cell_index] <= pipe_rows:
                            # This cell is in the first row, which means the previous cell was to the left.
                            if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                # The next cell in the path is to the right.
                                create_pipe(type = "straight", cell = grid_path[current_cell_index])
                            elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                # Next cell in the path is below.
                                create_pipe(type = "curved", cell = grid_path[current_cell_index])
                        
                        elif grid_path[current_cell_index] > amount_of_pipes - pipe_columns:
                            # This cell is in the last row, which means the next cell is to the right.
                            if grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:
                                # The previous cell was above, which means this cell needs a curved pipe.
                                create_pipe(type = "curved", cell = grid_path[current_cell_index])
                            elif grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:
                                # The previous cell was to the left, which means this cell needs a straight pipe.
                                create_pipe(type = "straight", cell = grid_path[current_cell_index])
                        
                        else:
                            # This cell is between the first and last row, after the first cell and before the last cell in its row.
                            if grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:
                                # The previous cell was to the left
                                if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                    # The next cell is to the right.
                                    create_pipe(type = "straight", cell = grid_path[current_cell_index])
                                elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                    # The next cell is below.
                                    create_pipe(type = "curved", cell = grid_path[current_cell_index])
                            
                            elif grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:
                                # The previous cell was above.
                                if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                    # The next cell is to the right.
                                    create_pipe(type = "curved", cell = grid_path[current_cell_index])
                                elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                    # The next cell is below.
                                    create_pipe(type = "straight", cell = grid_path[current_cell_index])
                else:
                    # "i" does NOT exist in the grid_path list.
                    # We create a random pipe in the cell.
                    random_type = renpy.random.choice(list(pipe_types.keys()))
                    create_pipe(type = random_type, cell = i)
            
            elif i == amount_of_pipes:
                # Last run of the loop.
                # We add the last pipe into the last cell of the grid.
                current_cell_index = grid_path.index(i)
                if grid_path[current_cell_index] - 1 == grid_path[-2]:
                    # The previous cell was to the left.
                    # This cell needs a straight pipe.
                    create_pipe(type = "straight", cell = grid_path[current_cell_index])
                else:
                    # The previous cell was above.
                    # This cell needs a curved pipe.
                    create_pipe(type="curved", cell = grid_path[current_cell_index])

    def update_pipe_endpoints(cell):
        # After a pipe has been rotated, we need to update its endpoint values to reflect the change.
        for pipe in pipes:
            if pipe[3] == cell:
                for endpoint in pipe[2]:
                    # Loop through its endpoints.
                    if endpoint == "top":
                        # The current endpoint is "top", so we change it to "right".
                        endpoint_index = pipe[2].index("top")
                        pipe[2][endpoint_index] = "right"
                    elif endpoint == "right":
                        # The current endpoint is "right", so we change it to "bottom".
                        endpoint_index = pipe[2].index("right")
                        pipe[2][endpoint_index] = "bottom"
                    elif endpoint == "bottom":
                        # The current endpoint is "bottom", so we change it to "left".
                        endpoint_index = pipe[2].index("bottom")
                        pipe[2][endpoint_index] = "left"
                    elif endpoint == "left":
                        # The current endpoint is "left", so we change it to "top".
                        endpoint_index = pipe[2].index("left")
                        pipe[2][endpoint_index] = "top"
                break

    def rotate_pipe(cell):
        # function that changes the rotation of a pipe in the pipes list, according to it's position/cell.
        # We're NOT actually rotating a pipe imagebutton here, we're just setting a value in the pipes list that holds the current rotation.
        if pipes[cell -1][4] == 360:
            pipes[cell - 1][4] = 90
        else:
            pipes[cell - 1][4] += 90
            
        update_pipe_endpoints(cell)
        check_pipe_connections()

    def check_pipe_connections():
        # Function that checks if there's a path with aligned pipes from the starting point to the ending point in the grid.
        global connected_pipes
        
        connected_pipes = []
        
        if "left" in pipes[0][2] and pipes[0] not in connected_pipes:
            # The first pipe in the grid is connected to its starting point so we add it to the connected_pipes list.
            connected_pipes.append(pipes[0])
        
        if len(connected_pipes) > 0 and connected_pipes[0][3] == 1:
            # The connected_pipes list contains the first pipe in the grid.
            # That means we can now check if the first pipe has an endpoint that aligns with another pipe.
            for pipe in connected_pipes:
                pipe_to_add = None
                if pipe[3] % pipe_columns == 1 and pipe[3] != 1 and "left" in pipe[2]:
                    # Current pipe in the loop is the first one in its row but not the first in the grid.
                    # It has a loose left endpoint where liquid could pour out, so we break the loop.
                    break
                
                if pipe[3] % pipe_columns != 0:
                    # Current pipe in the loop is not the last one in its row.
                    if "right" in pipe[2]:
                        if "left" in pipes[pipe[3]][2]:
                            # This pipe aligns with a pipe to the left of it.
                            if pipes[pipe[3]] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3]]
                        else:
                            # The pipe has a loose right endpoint and can't be used.
                            break
                
                if pipe[3] <= amount_of_pipes - pipe_columns:
                    # Current pipe in the loop is not in the last row.
                    if "bottom" in pipe[2]:
                        if "top" in pipes[pipe[3] - 1 + pipe_columns][2]:
                            # This pipe aligns with a pipe below it.
                            if pipes[pipe[3] - 1 + pipe_columns] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 1 + pipe_columns]
                        else:
                            break
                
                elif pipe[3] > amount_of_pipes - pipe_columns and "bottom" in pipe[2]:
                    #Current pipe in the loop is in the last row and it has a loose bottom endpoint.
                    break
                
                if pipe[3] > pipe_columns:
                    # Current pipe in the loop is not in the first row.
                    if "top" in pipe[2]:
                        if "bottom" in pipes[pipe[3] - 1 - pipe_columns][2]:
                            # The pipe aligns with the pipe above it.
                            if pipes[pipe[3] - 1 - pipe_columns] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 1 - pipe_columns]
                        else:
                            break
                
                elif pipe[3] <= pipe_columns and "top" in pipe[2]:
                    # Current pipe in the loop is in the first row and it has a loose top endpoint.
                    break
                
                if pipe[3] % pipe_columns != 1 and pipe[3] != 1:
                    # Current pipe in the loop is not the first in its row and is not the first one in the grid.
                    if "left" in pipe[2]:
                        if "right" in pipes[pipe[3] - 2][2]:
                            # The pipe aligns with the pipe to the left of it.
                            if pipes[pipe[3] - 2] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 2]
                        else:
                            break
                
                if pipe_to_add != None:
                    # The current iteration of the loop was not interrupted, which means the current pipe has no loose endpoints.
                    # We'll therefore add it to the connected_pipes list.
                    connected_pipes.append(pipe_to_add)
        
        if len(connected_pipes) > 0:
            if amount_of_pipes == connected_pipes[-1][3]:
                if "right" not in connected_pipes[-1][2]:
                    # The last pipe in the connected_pipes list is the last one in the grid, but it doesn't connect to its end.
                    # We remove it from the list.
                    connected_pipes.pop(-1)
                else:
                    # The last pipe in the grid exists in the connected_pipes list and it's connected to its endpoint to the right.
                    # Now we can take an appropriate action as the player has made a complete valid path from start to end.
                    # In this case, we show a custom screen named "pipe_game_success".
                    renpy.show_screen("pipe_game_success")

# Screen to show when the player successfully connects the pipes.
screen pipe_game_success:
    modal True
    frame:
        background "#00000088"
        xfill True
        yfill True
    frame:
        xsize 450
        ysize 200
        padding(20, 15)
        align(0.5, 0.5)
        
        text "Success! Play again?" color "#FFFFFF" size 30 align(0.5, 0.2)
        
        grid 2 1:
            spacing 100
            align(0.5, 0.9)
            
            textbutton "Yes" text_color "#FFFFFF" text_size 30 xalign 0.5 action [Function(setup_pipe_game), Hide("pipe_game_success")]
            textbutton "No" text_color "#FFFFFF" text_size 30 xalign 0.5 action [Hide("pipe_game_success"), Return()]

# The main screen for the pipe connecting minigame.
screen connect_the_pipes:
    # Add your background image here
    image "pipe_game_img/background.png" 
    
    grid pipe_columns pipe_rows:
        spacing 0
        pos(640, 140) # Adjust position as needed
        anchor(0.0, 0.0)
        
        for pipe in pipes:
            # To be able to rotate the pipe when we click it, we need to make the imagebutton use a Transform displayable as its child, where the 'rotate' property is set to a variable
            # of the pipe (pipe[4]). We can't apply a transform to the imagebutton (ex: at pipe_transform) for the rotation, because the transform won't re-evaluate each
            # run, and therefore it will always be stuck at it's initial rotation.
            # We use a function as the action (rotate_pipe), where we modify the rotation value of the pipe which the transform displayable child will detect
            if pipe in connected_pipes:
                imagebutton idle Transform("pipe_game_img/" + pipe[1] + "-pipe-connected.png", rotate = pipe[4], rotate_pad = False) action Function(rotate_pipe, cell = pipe[3])
            else:
                imagebutton idle Transform(pipe[0], rotate = pipe[4], rotate_pad = False) action Function(rotate_pipe, cell = pipe[3])