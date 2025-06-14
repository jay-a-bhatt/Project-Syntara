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


# The game starts here.
label start:

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

    "Project Syntara. A classified deep-space mission, humanity's last hope hidden among the stars."
    "You are the engineer — one of six specialists chosen for this journey."
    "Alongside scientists, a commander, and an AI expert, you were placed in cryosleep."
    "Your destination: Tassili, an exoplanet once used for secret biological research."
    "You were supposed to wake up years from now."
    "But something changed."
    "Your cryopod hisses open early."
    call screen connect_the_pipes
    scene cryo_loop
    "The floor is slick with mist. Red warning lights pulse across the ceiling."
    "Alarms echo through the ship."

    "Something's gone wrong."

    # call screen connect_the_pipes

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

    # block_game_img BEGINS HERE

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