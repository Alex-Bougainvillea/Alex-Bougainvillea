#!/bin/bash
text=$*
length=${#text}
for i in $(seq 1 $((length + 2))); do
     line+="-"
done
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
