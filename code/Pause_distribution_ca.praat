
form Variables
    sentence filename
    sentence txtfile
endform

appendInfoLine: filename$

Read from file... 'filename$'

To TextGrid (silences)... 75 0 -20 0.1 0.1 silent sounding
List: "no", 2, "yes", "no"

fappendinfo 'txtfile$'
