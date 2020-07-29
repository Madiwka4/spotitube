echo "Your distro? ( 1)Arch, 2)Debian): "
read distro
if [ $distro -eq 1 ]
then 
    sudo pacman -S python3 python-pip mpv youtube-dl
    pip install youtube-search
    chmod +x spotitube.sh
elif [ $distro -eq 2 ]
then 
    sudo apt remove youtube-dl
    sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl
    youtube-dl -U
    sudo apt install python3 python3-pip mpv
    pip3 install youtube-search 
    chmod +x spotitube.sh 
else 
    echo "You typed in: $distro"
    echo "Wrong input, please type one of the two: (1/2)";
fi