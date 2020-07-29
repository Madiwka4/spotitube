# Spotitube

Basically, a tool to listen to music using YouTube search results.
# Instalation
FOR ARCH USERS ONLY STEP (SKIP IF OTHER OS):
```shell
cmod +x dependencies.sh
./dependencies.sh
```
This will install the required dependencies (skip next step)

# Prerequisites

The dependencies.sh already handles the dependencies, but if you want to do it manually, then here you go.


This app requires python3, pip3, and youtube-search python module to function properly:

Arch:
```shell
sudo pacman -S python3 python-pip
pip install youtube-search
```
Debian/ubuntu:
```shell
sudo apt install python3 pip3
pip3 install youtube-search
```

# Usage

All you have to do is launch spotitube.sh and give it a string argument with the song name!

```shell
./spotitube.sh "Song name"
```

Enjoy your music!