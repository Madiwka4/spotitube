va=$(python3 open.py -i "$1")
echo $1
echo "Opening $va"
mpv --no-video $va 