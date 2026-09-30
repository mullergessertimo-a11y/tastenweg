#!/bin/bash
export NODE_PATH=$(npm root -g)
out=$1; : > $out
while read kind wav piece secs soll; do
  if [ "$kind" = "bg" ]; then
    res=$(timeout $((secs+25)) node runbg.js $wav $piece $secs 2>/dev/null | grep -o "Onsets=[0-9]* Richtig=[0-9]* ICH-HOERE=[0-9]*%")
  else
    res=$(timeout $((secs+25)) node run.js $wav $piece 0 $secs 2>/dev/null | grep -v ERR | tail -1 | awk '{print $2}')
  fi
  echo "$kind $wav $piece soll=$soll => $res" >> $out
done < $2
echo DONE >> $out
