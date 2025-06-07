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

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cryo

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

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
