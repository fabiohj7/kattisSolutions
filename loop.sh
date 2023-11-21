#!/bin/bash

exec="./a.out"
n=1

for((i = 1; i <= 1000; i++)); do
  echo "$n:"
  echo "$i" | "$exec"
  echo
  ((n++))
done

