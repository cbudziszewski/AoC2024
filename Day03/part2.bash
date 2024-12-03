#!/bin/bash 

#grep -o -e 'mul([0-9]\{1,3\},[0-9]\{1,3\})' input.txt | sed -nE  's/mul\(([0-9]+),([0-9]+)\)/\1 * \2/p' | bc | paste -sd+ | bc

INSTR=( $(grep -o -e "don't\|do\|mul([0-9]\{1,3\},[0-9]\{1,3\})" input.txt) )

enable=1
sum=0
for instr in ${INSTR[@]};
do	
	case ${instr} in 
		"don't")
			enable=0
			;;
		"do")
			enable=1
			;;
		*)
			sum=$(( sum + $(echo $instr | sed -nE  "s/mul\(([0-9]+),([0-9]+)\)/$enable * \1 * \2/p" | bc) ))
			;;
	esac
done
echo $sum

