default persistent.puzzle1_solved = False
define p = Character("Player", what_color="#FFD700", image="p")
define narrator = Character(None, what_italic=True, what_color="#BEBEBE")

define c = Character("Commander", color="#5c85d6", what_color="#c4d7f5", image="c")
define a = Character("AI Specialist", color="#42f5b9", what_color="#d9fcf1", image="a")
define b = Character("Biologist", color="#61c266", what_color="#d9f2da", image="b")
define m = Character("Medic", color="#de7c7c", what_color="#f5dcdc", image="m")
define n = Character("Navigator", color="#f2a55c", what_color="#fce9d6", image="n")

image c = "characters/commander.png"
image a = "characters/ai_specialist.png"
image b = "characters/biologist.png"
image m = "characters/medic.png"
image n = "characters/navigator.png"

define narrator = Character(None, what_italic=True, what_color="#BEBEBE")

# Transforms for character focus
transform darken:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4a4a4a") * SaturationMatrix(1.0)

transform lighten:
    linear 0.5 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)


# The game starts here.
label start:
    $ persistent.puzzle1_solved = False
    $ block_SM = SpriteManager(update = blocks_update, event = blocks_events)
    $ block_sprites = []
    $ long_h_block = Image("block_game_img/long-horizontal-block.png")
    $ long_v_block = Image("block_game_img/long-vertical-block.png")
    $ short_h_block = Image("block_game_img/short-horizontal-block.png")
    $ short_v_block = Image("block_game_img/short-vertical-block.png")
    $ move_block = Image("block_game_img/move-block.png")
    $ goal = Image("block_game_img/goal-vertical.png")
    $ long_v_block_size = (140, 452)
    $ long_h_block_size = (452, 140)
    $ short_v_block_size = (140, 302)
    $ short_h_block_size = (302, 140)
    $ puzzle_frame_size = (938, 938)
    $ puzzle_frame_pos = (110, 71)
    $ current_puzzle = 1
    $ click_pos = [0, 0]

    $ setup_pipe_game()


    jump scene_1

    # This ends the game
    return

label scene_1:

    scene galaxy

    narrator "Project Syntara. A classified deep-space mission, humanity's last hope hidden among the stars."
    narrator "You are the engineer — one of six specialists chosen for this journey."
    narrator "Alongside scientists, a commander, and an AI expert, you were placed in cryosleep."
    narrator "Your destination: Tassili, an exoplanet once used for secret biological research."
    narrator "You were supposed to wake up years from now."
    narrator "But something changed."
    narrator "Your cryopod hisses open early."

    scene cryo_loop
    narrator "The floor is slick with mist. Red warning lights pulse across the ceiling."
    narrator "Alarms echo through the ship."

    narrator "Something's gone wrong."

    menu:
        "What happened? Why were we woken up early?":
            jump what_happened

        "Check vitals. Stay sharp — someone needs to take the lead.":
            jump check_vitals

        "Someone give me a status update. Immediately.":
            jump status_update

label what_happened:
    narrator "You wake up groggy, rubbing your temples."

    p "Something's off. This wasn't scheduled. We weren't supposed to wake yet..."
    call screen connect_the_pipes # this can be changed to anywhere in the code
    show c
    narrator "The commander puts on his jacket, annoyed."

    c "Exactly. And that's not just an early wakeup — that's a full-system alert. Something hit critical."
    hide c

    show c at left, darken
    show a at right
    narrator "The AI Specialist is on the terminal, fingers flying over the keys"

    a "Ship's core is unresponsive. Emergency batteries are running the life support. Earth is... silent"

    hide c
    hide a
    jump scene_2

label check_vitals:
    p "Vitals first. Commander, what's the situation on the comms?"

    narrator "The commander glances at you, more composed than before."

    show c at left
    c "Smart move. But this isn't just about vitals. We've got a much bigger problem."

    narrator "The Medic scans the crew for their vitals"

    show c at left, darken
    show m at right
    m "Everyone's stable — for now. But oxygen flow's unstable."

    narrator "The AI Specialist speaks without looking up, a look of clear concern on their face"

    hide c
    show m at right, darken
    show a at left
    a "The core's down. We're flying blind."

    hide a
    hide m
    jump scene_2

label status_update:
    narrator "You clear your throat"

    p "Status. Right now. Who's checked the logs?"

    narrator "The commander raises an eyebrow"

    show c at left
    c "Look who's barking orders now. Fine. You want a report?"

    show c at left, darken
    show a at right
    a "Ship's drifting. Core is offline. Earth isn't responding. That enough of a summary?"

    hide c
    show a at right, darken
    show n at left
    n "We're off course. Engines are locked behind a sealed panel."

    hide n
    hide a
    jump scene_2

label scene_2:
    narrator "The lights flicker. One hallway goes dark completely. Somewhere below, the ship lets out a low, grinding noise — like metal crying out."

    narrator "The Syntara is drifting, and it doesn't sound good."

    narrator "For a moment, no one says a word."

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

    narrator "The commander looks grim as he responds"

    show a at left, darken
    show c at right
    c "Real bad. We need a plan, now."
    hide a
    hide c
    jump scene_3

label ship_settling:
    narrator "The navigator looks crestfallen."

    show n at left
    n "I've flown a lot of ships. That wasn't settling."

    narrator "The Medic frowns as they run more vitals"

    show n at left, darken
    show m at right
    m "Vitals are stable… but this ship isn’t."
    hide n
    hide m
    jump scene_3

label silence:
    show c at left
    narrator "The commander nods slowly"

    c "Agreed. I've heard emergency klaxons. This is different."

    narrator "The AI Specialist stares at their screen."

    show c at left, darken
    show a at right
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

    scene hallway_one_light

    narrator "The crew rushes down the flickering hallway."

    narrator "The floor shakes under your feet - like the ship has its own uneven heartbeat."

    scene hallway_both_lights

    narrator "You stop at the sealed engine room door. Next to it, a console blinks with a dull green light."

    narrator "The manual override is open. Wires are frayed and burnt. You kneel down. Your hands are shaking - both from fear and from the cold."

    p "This'll take a few tries. Stay back, just in case it sparks."

    show c
    c "Just don't fry yourself."
    hide c

    # Check if the puzzle was already solved.
    if persistent.puzzle1_solved:
        narrator "The wiring looks familiar. You quickly bypass the lock."
        jump scene_4
    else:
        $ quick_menu = False
        # If not solved, create the blocks and call the puzzle screen.
        $ create_blocks()
        call screen unblock_puzzle

label scene_4:

    narrator "Your fingers move fast, trying to make sense of the mess."

    narrator "Sparks fly as you twist the wires into place, one after another."

    scene hallway_one_light

    narrator "The ship lets out a deep groan, like it's fighting you."

    scene hallway

    narrator "The lights fade... then flicker back on, brighter."

    scene hallway_both_lights

    narrator "The door starts to open - slow and shaky."

    scene engine_room_red_alert

    narrator "With a loud, grinding screech, the doors slide open. A wave of hot, metallic air hits your face."

    narrator "Inside, it's a mess - wires hanging down, fuses blown, everything flickering and half-dead. The control panel glows weakly at the far end. You smell burnt plastic."

    narrator "You take a step in. The system starts to boot up... then stops."

    narrator "Something's not right. Really not right."

    narrator "The commander looks tense, with their arms crossed watching the screen flicker"

    show c
    c "What the hell happened while we were asleep? Where's Earth? Why aren't we getting anything?"
    hide c

    narrator "The AI specialist types quickly, eyes narrowing at the console"

    show a
    a "There was something. A signal buried in the logs. It's... damaged. Corrupted maybe."
    hide a

    p "Can you recover it? Anything at all?"

    show a
    a "Bits of audio. No clear origin, no timestamp. Just a few words... and static."
    hide a

    show a at left
    a "It doesn't sound like a distress call. More like... a warning. But I can't be sure."

    show a at left, darken
    show c at right
    c "So we're floating out here with a broken core, no fuel, and a half-message that might mean nothing?"

    show c at right, darken
    p "It means something. Someone - or something - tried to reach us. We need to figure out what they were trying to tell us."

    show a at left, lighten
    a "I'll keep decoding. But whatever happened back home... it started before we even woke up."
    hide a
    hide c

    narrator "The room goes quiet. Just the sound of static and flickering lights."

    narrator "No one speaks, but the fear is there - heavy and real."

    narrator "Whatever happened to Earth... already started."

    return