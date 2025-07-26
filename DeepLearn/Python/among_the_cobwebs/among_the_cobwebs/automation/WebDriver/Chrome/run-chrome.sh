SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
"$SCRIPT_DIR/chrome-installation/opt/google/chrome/google-chrome" \
--user-data-dir="$SCRIPT_DIR/chrome-data" \
--disk-cache-dir="$SCRIPT_DIR/chrome-cache" \
--no-default-browser-check \
--disable-extensions \
--disable-sync \
--disable-background-networking \
"$@"
