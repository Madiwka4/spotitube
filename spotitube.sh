echo "Searching for result #${2:-1} in $1..."
va=$(python3 open.py -i "$1" -o "${2:-1}")

echo "Opening $va"
mpv --no-video $va 