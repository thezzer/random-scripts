#!/bin/bash

# if [ "$EUID" -ne 0 ]
#   then echo "Please run as root"
#   exit
# fi

# allgames=(nudoku nsnake moon-buggy)

# lenght=${allgames[@]}

# for t in $lenght; do
#   if ! command -v $t &> /dev/null
#   then
#     apt install $t
#     echo "uliuli"
#   fi
# done

# random=$(($RANDOM % ${#allgames[@]}))

# ${allgames[$random]}

############

# if [ "$EUID" -ne 0 ]
#   then echo "Please run as root"
#   exit
# fi

# allgames=(nudoku nsnake moon-buggy)

# apt install -y ${allgames[@]}

# random=$(($RANDOM % ${#allgames[@]}))

# ${allgames[$random]}

############

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

allgames=(nudoku nsnake moon-buggy)

apt install -y ${allgames[@]}

# random=$(($RANDOM % ${#allgames[@]}))

${allgames[ (( $RANDOM % ${#allgames[@]} )) ]}
