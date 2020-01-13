#!bash

FILES=../audio_files/*.mp3

for f in $FILES
do
  file_name=$(basename $f .mp3)
  echo "Processing $file_name file..."
  # take action on each file. $f store current file name
  /Applications/Praat.app/Contents/MacOS/Praat --run  ./Pause_distribution_ca.praat $f ../pause_files_from_audio/$file_name.xlsx
done
