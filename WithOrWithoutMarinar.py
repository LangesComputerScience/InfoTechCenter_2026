# Welcome Branch
# This program simulates a simple operating system boot sequence
# with animated loading text and colored terminal output.

# -------------------------------
# Libraries Imported Here
# -------------------------------
import sys      # Used to write text to the terminal without adding new lines
import time     # Used to add delays (sleep) for animation timing

# -------------------------------
# ANSI Color Codes
# These codes change text color/style in the terminal
# -------------------------------
RESET = "\033[0m"    # Resets text color back to default
BOLD = "\033[1m"     # Makes text bold
CYAN = "\033[36m"    # Cyan text color
YELLOW = "\033[33m"  # Yellow text color
GREEN = "\033[32m"   # Green text color

# -------------------------------
# Program Title / Header
# -------------------------------
print(f"\n{BOLD}{CYAN}Welcome Branch - Developer: Mr. Lange{RESET}")
print(f"\n{BOLD}{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# -------------------------------
# Variables for Boot Animation
# -------------------------------
x = 0            # Controls how long the boot sequence runs
ellipsis = 0     # Controls the number of dots displayed during loading

# -------------------------------
# Boot Sequence Loop
# -------------------------------
# Runs until x reaches 20, simulating a system startup process
while x != 20:
    x += 1

    # Create the animated boot message with increasing dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Write the message on the same line (no new line)
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause briefly to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3 to loop the animation
    if ellipsis == 4:
        ellipsis = 0

    # Final success message when boot sequence completes
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")
