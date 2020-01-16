#!bash

find ./audio_files -type f | while read f
#find ./temp_dir_for_del -type f | while read f
do
  echo "Processing $f file..."
  case $f in 
    *.mp3)
	echo "mp3";;
    *.wav)
	echo "wav";;
    *)
	echo "unacceptable format, deleting file"
	rm "$f";;
  esac
done
