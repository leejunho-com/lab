#!/bin/bash
# Full search video files, encdcode them in your path and save Same Path as Source with HandBrake CLI
# By JO HYUK JUN - 2024.04.15
# 
# Usage :
#   'sudo ./hb-c.sh '/root-path''
#
ROOT_PATH=$1
PRESET='./hb-p.json'

while IFS= read -d '' -r ITEM
do
    echo "ITEM: $ITEM"
    FILE=${ITEM##*/}
    echo "FILE: $FILE"
    FILE_PATH=${ITEM%/*}
    echo "FILE_PATH: $FILE_PATH"
    EXT=${ITEM##*.}
    echo "EXT: $EXT"
    EXT=$(echo $EXT | tr "[:upper:]" "[:lower:]")
    OUTPUT="$FILE_PATH/${FILE%}[HB-C].mp4"
    echo "" | HandBrakeCLI -i "$ITEM" -o "$OUTPUT" --preset-import-file $PRESET
# Add extentions to encode < -or -iname '*.ext'>
done < <(find "$ROOT_PATH" \( -iname '*.asf' -or -iname '*.avi' -or -iname '*.flv' -or -iname '*.mkv' -or -iname '*.mov' -or -iname '*.mp4' -or -iname '*.mpeg' -or -iname '*.ts' -or -iname '*.webm' -or -iname '*.webp' -or -iname '*.wmv' -or -iname '*.m4v' -or -iname '*.mpg' -or -iname '*.ts' -or -iname '*.mts' -or -iname '*.m2ts' -or -iname '*.vob' -or -iname '*.evo' \) -print0)