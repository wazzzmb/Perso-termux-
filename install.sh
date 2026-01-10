#!/bin/bash

echo "[+] Installation du Termux Banner Tool..."

pkg install python -y

mkdir -p ~/.termux

cp banner.py ~/

echo "alias banner='python ~/banner.py'" >> ~/.bashrc

echo "[+] Installation terminée"
echo "➡️ Redémarre Termux puis tape : banner"
