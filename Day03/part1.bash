#!/bin/bash 

grep -o -e 'mul([0-9]\{1,3\},[0-9]\{1,3\})' input.txt | sed -nE  's/mul\(([0-9]+),([0-9]+)\)/\1 * \2/p' | bc | paste -sd+ | bc
