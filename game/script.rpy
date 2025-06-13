# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")

define c = Character("Commander", color="#222844")
image c = "characters/commander.png"

define a = Character("AI Specialist", color="#113839")
image a = "characters/ai_specialist.png"

define b = Character("Biologist", color="#153b25")
image b = "characters/biologist.png"

define m = Character("Medic", color="#551e21")
image m = "characters/medic.png"

define n = Character("Navigator", color="#c0763f")
image n = "characters/navigator.png"

image cryo = "backgrounds/cryo.png"
image cryo_red_alert = "backgrounds/cryo_red_alert.png"
image engine_room = "backgrounds/engine_room.png"
image engine_room_left_lights = "backgrounds/engine_room_left_lights.png"
image engine_room_red_alert = "backgrounds/engine_room_red_alert.png"
image engine_room_right_lights = "backgrounds/engine_room_right_lights.png"
image engine_room_spotlight = "backgrounds/engine_room_spotlight.png"
image hallway = "backgrounds/hallway.png"
image hallway_both_lights = "backgrounds/hallway_both_lights.png"
image hallway_one_light = "backgrounds/hallway_one_light.png"
image galaxy = "backgrounds/galaxy.png"

image cryo_loop = Animation(
    "backgrounds/cryo.png", 0.5,
    "backgrounds/cryo_red_alert.png", 0.5,
    repeat=True
)

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
    image "minigame/puzzle-bg.png"
    image "minigame/puzzle-frame.png" pos puzzle_frame_pos
    add block_SM

label solved_puzzle:
    "Puzzle completed!"
    jump scene_4


# The game starts here.
label start:

    $ block_SM = SpriteManager(update = blocks_update, event = blocks_events)
    $ block_sprites = []
    $ long_h_block = Image("minigame/long-horizontal-block.png")
    $ long_v_block = Image("minigame/long-vertical-block.png")
    $ short_h_block = Image("minigame/short-horizontal-block.png")
    $ short_v_block = Image("minigame/short-vertical-block.png")
    $ move_block = Image("minigame/move-block.png")
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

    scene galaxy

    "Project Syntara. A classified deep-space mission, humanity's last hope hidden among the stars."
    "You are the engineer — one of six specialists chosen for this journey."
    "Alongside scientists, a commander, and an AI expert, you were placed in cryosleep."
    "Your destination: Tassili, an exoplanet once used for secret biological research."
    "You were supposed to wake up years from now."
    "But something changed."
    "Your cryopod hisses open early."
    scene cryo_loop
    "The floor is slick with mist. Red warning lights pulse across the ceiling."
    "Alarms echo through the ship."

    "Something's gone wrong."

    menu:
        "What happened? Why were we woken up early?":
            jump what_happened

        "Check vitals. Stay sharp — someone needs to take the lead.":
            jump check_vitals

        "Someone give me a status update. Immediately.":
            jump status_update

label what_happened:
    "You wake up groggy, rubbing your temples."

    p "Something's off. This wasn't scheduled. We weren't supposed to wake yet..."

    show c
    "The commander puts on his jacket, annoyed."

    c "Exactly. And that's not just an early wakeup — that's a full-system alert. Something hit critical."
    hide c

    show c at left
    show a at right
    "The AI Specialist is on the terminal, fingers flying over the keys"

    a "Ship's core is unresponsive. Emergency batteries are running the life support. Earth is... silent"

    hide c
    hide a
    jump scene_2

label check_vitals:
    p "Vitals first. Commander, what's the situation on the comms?"

    "The commander glances at you, more composed than before."

    show c at left
    c "Smart move. But this isn't just about vitals. We've got a much bigger problem."

    "The Medic scans the crew for their vitals"

    show m at right
    m "Everyone's stable — for now. But oxygen flow's unstable."

    "The AI Specialist speaks without looking up, a look of clear concern on their face"

    hide c
    show a at left
    a "The core's down. We're flying blind."

    hide a
    hide m
    jump scene_2

label status_update:
    "You clear your throat"

    p "Status. Right now. Who's checked the logs?"

    "The commander raises an eyebrow"

    show c at left
    c "Look who's barking orders now. Fine. You want a report?"

    show a at right
    a "Ship's drifting. Core is offline. Earth isn't responding. That enough of a summary?"

    hide c
    show n at left
    n "We're off course. Engines are locked behind a sealed panel."

    hide n
    hide a
    jump scene_2

label scene_2:
    "The lights flicker. One hallway goes dark completely. Somewhere below, the ship lets out a low, grinding noise — like metal crying out."

    "The Syntara is drifting, and it doesn't sound good."

    "For a moment, no one says a word."

    menu:
        "How bad is it?":
            jump how_bad

        "...Tell me that was just the ship settling.":
            jump ship_settling

        "This silence is worse than any alarm.":
            jump silence

label how_bad:
    show a at left
    a "Core's non-responsive. Life support is draining. It's bad."

    "The commander looks grim as he responds"

    show c at right
    c "Real bad. We need a plan, now."
    hide a
    hide c
    jump scene_3

label ship_settling:
    "The navigator looks crestfallen."

    show n at left
    n "I've flown a lot of ships. That wasn't settling."

    "The Medic frowns as they run more vitals"
    
    show m at right
    m "Vitals are stable… but this ship isn’t."
    hide n
    hide m
    jump scene_3

label silence:
    show c at left
    "The commander nods slowly"

    c "Agreed. I've heard emergency klaxons. This is different."

    show a at right
    "The AI Specialist stares at their screen."

    a "System should be reporting diagnostics. It's not."

    hide c
    hide a
    jump scene_3

label scene_3:
    p "We need engine access. Until we know what state the core is in, we're flying blind."

    show a
    a "Access is locked. Manual override only."
    hide a

    show b
    b "Then let's override it."
    hide b

    # TRANSITION: Going inside the engine room
    
    scene hallway_one_light

    "The crew rushes down the flickering hallway."

    "The floor shakes under your feet - like the ship has its own uneven heartbeat."

    scene hallway_both_lights

    "You stop at the sealed engine room door. Next to it, a console blinks with a dull green light."

    "The manual override is open. Wires are frayed and burnt. You kneel down. Your hands are shaking - both from fear and from the cold."

    p "This'll take a few tries. Stay back, just in case it sparks."

    show c
    c "Just don't fry yourself."
    hide c

    # MINIGAME BEGINS HERE

    $ create_blocks()
    call screen unblock_puzzle

label scene_4:

    "Your fingers move fast, trying to make sense of the mess."

    "Sparks fly as you twist the wires into place, one after another."

    scene hallway_one_light

    "The ship lets out a deep groan, like it's fighting you."

    scene hallway

    "The lights fade... then flicker back on, brighter."

    scene hallway_both_lights

    "The door starts to open - slow and shaky."

    scene engine_room_red_alert

    "With a loud, grinding screech, the doors slide open. A wave of hot, metallic air hits your face."

    "Inside, it's a mess - wires hanging down, fuses blown, everything flickering and half-dead. The control panel glows weakly at the far end. You smell burnt plastic."

    "You take a step in. The system starts to boot up... then stops."

    "Something's not right. Really not right."

    "The commander looks tense, with their arms crossed watching the screen flicker"

    show c
    c "What the hell happened while we were asleep? Where's Earth? Why aren't we getting anything?"
    hide c

    "The AI specialist types quickly, eyes narrowing at the console"

    show a
    a "There was something. A signal buried in the logs. It's... damaged. Corrupted maybe."
    hide a

    p "Can you recover it? Anything at all?"

    show a
    a "Bits of audio. No clear origin, no timestamp. Just a few words... and static."
    hide a

    show a at left
    a "It doesn't sound like a distress call. More like... a warning. But I can't be sure."

    show c at right
    c "So we're floating out here with a broken core, no fuel, and a half-message that might mean nothing?"
    hide c

    p "It means something. Someone - or something - tried to reach us. We need to figure out what they were trying to tell us."

    a "I'll keep decoding. But whatever happened back home... it started before we even woke up."
    hide a
    hide c

    "The room goes quiet. Just the sound of static and flickering lights."

    "No one speaks, but the fear is there - heavy and real."

    "Whatever happened to Earth... already started."

    # This ends the game
    return