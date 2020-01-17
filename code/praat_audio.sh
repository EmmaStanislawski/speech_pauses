#!bash

find ../../audio_files -type f | while read f
do
  echo "Processing $f file..."
  #no spaces in file path, just to extract output file name
  fn=$(tr -d ' ' <<< "$f")
  echo $fn
  case $fn in 
    *.mp3)
	echo "mp3"
	file_name=$(basename $fn .mp3);;
    *.wav)
	echo "wav"
	file_name=$(basename $fn .wav);;
    *)
	echo "unacceptable format, continuing to next one"
	continue
  esac
  echo "file_name: "$file_name
  echo "passing $f to praat"
  # take action on each file. f store current file name
  /Applications/Praat.app/Contents/MacOS/Praat --run  ./Pause_distribution_ca.praat "$f" ../../pauses_files_from_audio/$file_name.xls
done
