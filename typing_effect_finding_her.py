import sys
import time

# The list of strings (lyrics) to be printed with a typing effect.
lyrics = [
    "Sambhaal ke rakha wo phool mera tu",
    "meri shayari mein zaroor rehta tu",
    "Jo aankhon mein pyaari si duniya basaayi",
    "Wo duniya bhi tha tu, wo lamha bhi tha tu",
    "Haan, lagte  mujhko ye kisse sataane",
    "Deta na dil mera tujhko bhulaane",
    "Adhoore se vaade, adhoori si baatein",
    "Ab hisse mein daakhil mere bas wo yaadein"
]

# A list of delays (in seconds). Each number corresponds to the pause *after* a line of lyrics.
# This allows you to control the rhythm of the song.
delays = [0.7, 0.7, 0.4, 0.5, 0.5, 0.7, 0.7, 1.0]


# --- Main Program ---

# Print a title for the output.
print("Finding Her:\n")
# An initial pause before the lyrics start.
time.sleep(1.2)

# Loop through each line in the lyrics list, getting both the index (i) and the line itself.
for i, line in enumerate(lyrics):
    # Loop through each character in the current line.
    for char in line:
        # Write one character to the console.
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # <<< DELAY 1: THE TYPING DELAY >>>
        # This short pause after every single character creates the typing effect.
        # Make this number smaller for faster typing, or larger for slower typing.
        time.sleep(0.08)
        
    # After a line is fully typed, print a newline.
    print()
    
    # <<< DELAY 2: THE LYRIC/LINE DELAY >>>
    # This pause happens *between* lines of lyrics.
    # We use the index 'i' to get the specific delay for this line from our 'delays' list.
    # This is what makes it feel like a song's rhythm.
    if i < len(delays):
      time.sleep(delays[i])
