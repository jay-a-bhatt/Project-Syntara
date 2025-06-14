

init python:

    def create_blocks():
        global block_sprites

        # Reset puzzle first
        for block in block_sprites:
            # Destroy each sprite in the sprites list.
            block.destroy()
        
        block_sprites = [] # Emptying the sprites list.
        block_SM.redraw(0) # Redraw the spritemanager to update it.

        # Create puzzle
        if current_puzzle == 1: # Puzzle 1
            # Row 1
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type = "sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 277
            block_sprites[-1].y = 87
            block_sprites[-1].initial_pos = [277, 87]

            block_sprites.append(block_SM.create(long_h_block))
            block_sprites[-1].type = "lh"
            block_sprites[-1].size = long_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 427
            block_sprites[-1].y = 87
            block_sprites[-1].initial_pos = [427, 87]
            
            # Row 2
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type = "sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 578
            block_sprites[-1].y = 237
            block_sprites[-1].initial_pos = [578, 237]
            
            # Row 3
            block_sprites.append(block_SM.create(move_block))
            block_sprites[-1].type = "red"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 277
            block_sprites[-1].y = 390
            block_sprites[-1].initial_pos = [277, 390]
            
            # Row 4
            block_sprites.append(block_SM.create(short_v_block))
            block_sprites[-1].type = "sv"
            block_sprites[-1].size = short_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 125
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos = [125, 540]

            block_sprites.append(block_SM.create(long_v_block))
            block_sprites[-1].type = "lv"
            block_sprites[-1].size = long_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 427
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos = [427, 540]

            block_sprites.append(block_SM.create(long_v_block))
            block_sprites[-1].type = "lv"
            block_sprites[-1].size = long_v_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 882
            block_sprites[-1].y = 540
            block_sprites[-1].initial_pos = [882, 540]
            
            # Row 5
            block_sprites.append(block_SM.create(short_h_block))
            block_sprites[-1].type = "sh"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 578
            block_sprites[-1].y = 692
            block_sprites[-1].initial_pos = [578, 692]
            
            # Row 6
            block_sprites.append(block_SM.create(short_h_block))
            block_sprites[-1].type = "sh"
            block_sprites[-1].size = short_h_block_size
            block_sprites[-1].drag = False
            block_sprites[-1].x = 125
            block_sprites[-1].y = 843
            block_sprites[-1].initial_pos = [125, 843]
            
            # Goal
            block_sprites.append(block_SM.create(goal))
            block_sprites[-1].type = "goal"
            block_sprites[-1].x = puzzle_frame_pos[0] + puzzle_frame_size[0] - 15
            block_sprites[-1].y = 390
            block_sprites[-1].size = [15, 140]


    def blocks_update(st):
        global current_puzzle
        
        for b1, block in enumerate(block_sprites):
            if hasattr(block, "drag") and block.drag:
                # A small offset value when detecting overlaps between blocks allows for errors in the initial coordinates of the blocks.
                # This is in case some of the blocks in the initial formation are blocking each other when they shouldn't and thus prevents movement of a block that should be able to move.
                offset = 2

                if block.type == "lv" or block.type == "sv":
                    # We're dragging a long vertical or short vertical block.
                    # 'distance' is start drag/click y pos - mouse new drag pos.
                    distance = click_pos[1] - renpy.get_mouse_pos()[1]
                    block.y = block.initial_pos[1] - distance
                    
                    for b2, block2 in enumerate(block_sprites):
                        if b1 != b2:
                            # If above is true, we've made sure that we're checking two different blocks and not the same one.
                            if block2.type != "goal" and (block.x - offset > block2.x and block.x + offset < block2.x + block2.size[0] or block.x + block.size[0] - offset > block2.x and block.x + block.size[0] + offset < block2.x + block2.size[0] or block.x + block.size[0] + offset > block2.x and block.x - offset < block2.x):
                                # Dragged block has an x coordinate that is within another block's x coordinate. That means that another block is either blocking it above or below.
                                if block.y < block2.y + block2.size[1] and block.y > block2.y:
                                    # Dragged block is touching a block above it. Stop the movement.
                                    block.y = block2.y + block2.size[1]
                                    block.initial_pos[1] = block.y
                                    click_pos[1] = renpy.get_mouse_pos()[1]
                                elif block.y + block.size[1] > block2.y and block.y + block.size[1] < block2.y + block2.size[1]:
                                    # Dragged block is touching a block below it. Stop the movement.
                                    block.y = block2.y - block.size[1]
                                    block.initial_pos[1] = block.y
                                    click_pos[1] = renpy.get_mouse_pos()[1]
                    
                    if block.y < puzzle_frame_pos[1] + 15:
                        # Dragged block is touching the top of the containing frame. Stop the movement.
                        block.y = puzzle_frame_pos[1] + 15
                        block.initial_pos[1] = block.y
                        click_pos[1] = renpy.get_mouse_pos()[1]
                        
                    elif block.y + block.size[1] > (puzzle_frame_pos[1] + puzzle_frame_size[1]) - 15:
                        # Dragged block is touching the bottom of the containing frame. Stop the movement.
                        block.y = (puzzle_frame_pos[1] + puzzle_frame_size[1]) - block.size[1] - 15
                        block.initial_pos[1] = block.y
                        click_pos[1] = renpy.get_mouse_pos()[1]
                        
                elif block.type == "lh" or block.type == "sh" or block.type == "red":
                    # We're dragging a long horizontal or short horizontal block.
                    # 'distance' is start drag/click x pos - mouse new drag pos.
                    distance = click_pos[0] - renpy.get_mouse_pos()[0]
                    block.x = block.initial_pos[0] - distance
                    
                    for b2, block2 in enumerate(block_sprites):
                        if b1 != b2:
                            if block2.type != "goal" and (block.y - offset > block2.y and block.y + offset < block2.y + block2.size[1] or block.y + block.size[1] - offset > block2.y and block.y + block.size[1] + offset < block2.y + block2.size[1] or block.y + block.size[1] + offset > block2.y and block.y - offset < block2.y):
                                # Dragged block is overlapping another block up or down.
                                if block.x < block2.x + block2.size[0] and block.x > block2.x:
                                    # Dragged block is touching a block to the left. Stop the movement.
                                    block.x = block2.x + block2.size[0]
                                    block.initial_pos[0] = block.x
                                    click_pos[0] = renpy.get_mouse_pos()[0]
                                elif block.x + block.size[0] > block2.x and block.x + block.size[0] < block2.x + block2.size[0]:
                                    # Dragged block is touching a block to the right. Stop the movement.
                                    block.x = block2.x - block.size[0]
                                    block.initial_pos[0] = block.x
                                    click_pos[0] = renpy.get_mouse_pos()[0]
                    
                    if block.x < puzzle_frame_pos[0] + 15:
                        # Dragged block is touching the left of the containing frame. Stop the movement.
                        block.x = puzzle_frame_pos[0] + 15
                        block.initial_pos[0] = block.x
                        click_pos[0] = renpy.get_mouse_pos()[0]
                    elif block.x + block.size[0] > (puzzle_frame_pos[0] + puzzle_frame_size[0]) - 15:
                        # Dragged block is touching the right of the containing frame. Stop the movement.
                        block.x = (puzzle_frame_pos[0] + puzzle_frame_size[0]) - block.size[0] - 15
                        block.initial_pos[0] = block.x
                        click_pos[0] = renpy.get_mouse_pos()[0]

                if (block.type == "red" and block2.type == "goal") and block.x + block.size[0] >= block2.x:
                    # Player has successfully gotten the red block to the goal.
                    # Next time, the puzzle shown to the player should be puzzle 2, so we make the 'current_puzzle' variable equal to 2.
                    # current_puzzle = 2
                    renpy.jump("solved_puzzle")
                    return None
        
        return 0

    def blocks_events(event, x, y, st):
        global click_pos
        
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONDOWN:
            # Mouse button is down.
            if event.button == 1:
                # The left mouse button is down.
                for block in block_sprites:
                    if block.type != "goal" and block.x < x < block.x + block.size[0] and block.y < y < block.y + block.size[1]:
                        # Mouse is overlapping this block and the button is pressed down.
                        # Drag the block.
                        block.drag = True
                        click_pos = [x, y]
                        block_SM.redraw(0)
                        break
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            for block in block_sprites:
                if hasattr(block, "drag") and block.drag:
                    block.drag = False
                    block.initial_pos = [block.x, block.y]
                    break

screen unblock_puzzle:
    
    image "block_game_img/puzzle-bg.png"
    image "block_game_img/puzzle-frame.png" pos puzzle_frame_pos
    add block_SM

label solved_puzzle:
    "Puzzle completed!"
    jump scene_4
