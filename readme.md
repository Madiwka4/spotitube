# Spotitube

Basically, a tool to listen to music using YouTube search results.
# Instalation
This only supports Debian and Arch.
```shell
chmod +x dependencies.sh
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
    sudo apt remove youtube-dl
    sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl
    youtube-dl -U
    sudo apt install python3 python3-pip mpv
    pip3 install youtube-search 
    chmod +x spotitube.sh 
```
The Debian package of youtube-dl is old and doesnt play videos anymore. That is why you should use wget to install it manually. 

# Usage

All you have to do is launch spotitube.sh and give it a string argument with the song name!

```shell
./spotitube.sh "Song name"
```

If you want to get a specific index of a result, just type that index as a second argument:

```shell
./spotitube.sh "Song name" 3
```
This will result in:
```
Searching for result #3 in Song name...
```

Enjoy your music!