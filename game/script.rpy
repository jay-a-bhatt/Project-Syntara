# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define p = Character("Player")

define c = Character("Commander")

define a = Character("AI Specialist")

define b = Character("Biologist")

define m = Character("Medic")

define n = Character("Navigator")


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
            block_sprites.append(block_SM.create(red_block))
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
    image "minigame/puzzle-bg.png"
    image "minigame/puzzle-frame.png" pos puzzle_frame_pos
    add block_SM

label solved_puzzle:
    scene cryo
    "Puzzle completed!"
    jump scene_2


# The game starts here.
label start:

    $ block_SM = SpriteManager(update = blocks_update, event = blocks_events)
    $ block_sprites = []
    $ long_h_block = Image("minigame/long-horizontal-block.png")
    $ long_v_block = Image("minigame/long-vertical-block.png")
    $ short_h_block = Image("minigame/short-horizontal-block.png")
    $ short_v_block = Image("minigame/short-vertical-block.png")
    $ red_block = Image("minigame/red-block.png")
    $ goal = Image("minigame/goal-vertical.png")
    $ long_v_block_size = (140, 452)
    $ long_h_block_size = (452, 140)
    $ short_v_block_size = (140, 302)
    $ short_h_block_size = (302, 140)
    $ puzzle_frame_size = (938, 938)
    $ puzzle_frame_pos = (110, 71)
    $ current_puzzle = 1
    $ click_pos = [0, 0]

    jump scene_1

    # This ends the game
    return

label scene_1:

    scene cryo

    "A deep red light flashes through the ship, slow and steady. One by one, the cryo pods hiss open. Cold mist spills out and spreads across the floor."
    "You suck in a breath - sharp and shaky. It's the first time you've breathed in months. Around you, the others are waking too, groggy and confused."
    "Something's not right."

    # (groggy, scanning control panel)
    p "Why did the system wake us? This isn't scheduled."

    # (pulls on jacket, annoyed)
    c "That's not just an early wakeup... That's a full-system alert. Something hit critical."

    # (frantically at terminal)
    a "Ship's core is unresponsive. Emergency batteries are powering life support and nothing else. Earth is... silent."

    # (looking around, tense)
    b "Was it radiation? Collision? Something triggered an override."

    n "We're off course. Drifting. Engines are unresponsive and locked behind a sealed panel."

    # (running quick vitals on the crew)
    m "Everyone's stable - for now. But oxygen isn't circulating correctly. We need to act fast."

    "The lights flicker. One hallway goes dark completely. Somewhere below, the ship lets out a low, grinding noise - like metal crying out."

    "The Syntara is drifting, and it doesn't sound good."

    "For a moment, no one says a word."

    c "Engineer. Talk to me. What can we do?"

    p "We need engine access. Until we know what state the core is in, we're flying blind."

    a "Access is locked. Manual override only."

    b "Then let's override it."

    # TRANSITION: Going inside the engine room

    "The crew rushes down the flickering hallway."

    "The floor shakes under your feet - like the ship has its own uneven heartbeat."

    "You stop at the sealed engine room door. Next to it, a console blinks with a dull green light."

    "The manual override is open. Wires are frayed and burnt. You kneel down. Your hands are shaking - both from fear and from the cold."

    # (focused)
    p "This'll take a few tries. Stay back, just in case it sparks."

    # (low voice)
    c "Just don't fry yourself."

    # MINIGAME BEGINS HERE

    $ create_blocks()
    call screen unblock_puzzle

label scene_2:

    "Your fingers move fast, trying to make sense of the mess."

    "Sparks fly as you twist the wires into place, one after another."

    "The ship lets out a deep groan, like it's fighting you."

    "The lights fade... then flicker back on, brighter."

    "The door starts to open - slow and shaky."

    # [Narration: Engine room is open]

    "With a loud, grinding screech, the doors slide open. A wave of hot, metallic air hits your face."

    "Inside, it's a mess - wires hanging down, fuses blown, everything flickering and half-dead. The control panel glows weakly at the far end. You smell burnt plastic."

    "You take a step in. The system starts to boot up... then stops."

    "Something's not right. Really not right."

    # (tense, arms crossed, watching the screen flicker)
    c "What the hell happened while we were asleep? Where's Earth? Why aren't we getting anything?"

    # (typing quickly, eyes narrowing at the console)
    a "There was something. A signal buried in the logs. It's... damaged. Corrupted maybe."

    # (stepping closer)
    p "Can you recover it? Anything at all?"

    a "Bits of audio. No clear origin, no timestamp. Just a few words... and static."
    # (beat)
    a "It doesn't sound like a distress call. More like... a warning. But I can't be sure."

    # (gritting teeth, pacing)
    c "So we're floating out here with a broken core, no fuel, and a half-message that might mean nothing?"

    # (quiet but firm)
    p "It means something. Someone - or something - tried to reach us. We need to figure out what they were trying to tell us."

    a "I'll keep decoding. But whatever happened back home... it started before we even woke up."

    "The room goes quiet. Just the sound of static and flickering lights."

    "No one speaks, but the fear is there - heavy and real."

    "Whatever happened to Earth... already started."

    # This ends the game
    return