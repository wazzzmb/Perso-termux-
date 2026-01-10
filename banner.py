import os
import time

BASHRC = os.path.expanduser("~/.bashrc")

pseudo = input("Ton pseudo pour Termux : ")

colors = [
    "\033[95m", # violet
    "\033[33m", # orange
    "\033[91m", # rose
    "\033[96m", # cyan
]

banner = [
"________.__",
"\\______   \\__| ____   _______  __ ____   ____  __ __   ____",
" |    |  _/  |/ __ \\ /    \\  \\/ // __ \\ /    \\|  |  \\_/ __ \\",
" |    |   \\  \\  ___/|   |  \\   /\\  ___/|   |  \\  |  /\\  ___/",
" |______  /__|\\___  >___|  /\\_/  \\___  >___|  /____/  \\___  >",
"        \\/        \\/     \\/          \\/     \\/            \\/"
]

def write_banner():
    with open(BASHRC, "w") as f:
        f.write("clear\n")
        f.write("echo ''\n")
        for i, line in enumerate(banner):
            color = colors[i % len(colors)]
            f.write(f"echo -e '{color}{line}\\033[0m'\n")
        f.write(f"echo -e '\\033[93mBienvenue {pseudo} dans Termux !\\033[0m'\n")
        f.write("echo ''\n")

write_banner()

print("🔥 Banner appliquée ! Redémarre Termux pour voir le résultat 🔥")
