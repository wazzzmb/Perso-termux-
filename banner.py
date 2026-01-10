import os
import time

# Fichier bashrc de Termux
BASHRC = os.path.expanduser("~/.bashrc")

# Ton pseudo
pseudo = input("Ton pseudo pour Termux : ")

# Couleurs ANSI arc-en-ciel (violet, orange, rose, cyan)
colors = [
    "\033[95m", # violet
    "\033[33m", # orange
    "\033[91m", # rouge/rose
    "\033[96m", # cyan
]

# Bannière ASCII simple
banner = [
    "██████╗ ██╗   ██╗███████╗███╗   ███╗███████╗",
    "██╔══██╗██║   ██║██╔════╝████╗ ████║██╔════╝",
    "██████╔╝██║   ██║█████╗  ██╔████╔██║█████╗  ",
    "██╔═══╝ ██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ",
    "██║     ╚██████╔╝███████╗██║ ╚═╝ ██║███████╗",
    "╚═╝      ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝",
]

def write_banner():
    with open(BASHRC, "w") as f:
        f.write("clear\n")
        f.write("echo ''\n")
        # Couleur arc-en-ciel
        for i, line in enumerate(banner):
            color = colors[i % len(colors)]
            # Bash ANSI color
            f.write(f"echo -e '{color}{line}\\033[0m'\n")
        # Message d’accueil avec pseudo
        f.write(f"echo -e '\\033[93mBienvenue {pseudo} dans Termux !\\033[0m'\n")
        f.write("echo ''\n")

write_banner()

print("🔥 Banner appliquée ! Redémarre Termux pour voir le résultat 🔥")
