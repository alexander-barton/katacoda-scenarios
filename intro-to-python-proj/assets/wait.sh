#!/bin/bash

show_progress()
{
    echo -n "Updating apt"
    local -r pid="${1}"
    local -r delay='0.75'
    local spinstr='\|/-'
    local temp

    # Loop for apt-update
    while true; do
        sudo grep -i "done" /root/apt-update &> /dev/null
        if [[ "$?" -ne 0 ]]; then
            temp="${spinstr#?}"
            printf " [%c]  " "${spinstr}"
            spinstr=${temp}${spinstr%"${temp}"}
            sleep "${delay}"
            printf "\b\b\b\b\b\b"
        else
            break
        fi
    done

    # Loop for installing dependencies
    printf "    \b\b\b\b"
    echo ""
    echo -n "Installing packages"
    while true; do 
        sudo grep -i "done" /root/apt-install &> /dev/null
        if [[ "$?" -ne 0 ]]; then
            temp="${spinstr#?}"
            printf " [%c]  " "${spinstr}"
            spinstr=${temp}${spinstr%"${temp}"}
            sleep "${delay}"
            printf "\b\b\b\b\b\b"
        else
            break
        fi
    done

    # Loop for linking python
    printf "    \b\b\b\b"
    echo ""
    echo -n "Final clean-up"
    while true; do
        sudo grep -i "done" /root/linking &> /dev/null
        if [[ "$?" -ne 0 ]]; then
            temp="${spinstr#?}"
            printf " [%c]  " "${spinstr}"
            spinstr=${temp}${spinstr%"${temp}"}
            sleep "${delay}"
            printf "\b\b\b\b\b\b"
        else
            break
        fi
    done

    printf "    \b\b\b\b"
    echo ""
    echo "Ready!!!"

}

show_progress