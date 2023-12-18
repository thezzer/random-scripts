#!/bin/bash

# Function to calculate MD5 checksum of a file
calculate_checksum() {
    md5sum "$output_file" | awk '{print $1}'
}

get_timestamp() {
    date +"%Y-%m-%d %T"
}

# Run smbstatus, filter clients with nt1 protocol, extract IP addresses
smbstatus_output=$(smbstatus -b | grep "NT1" | awk '{print $3}')

# File to store IP addresses
output_file="smbparser/nt1_addresses"

initial_checksum=$(calculate_checksum "$output_file")

# Check each IP address
for ip_address in $smbstatus_output
do
    # Check if the IP address exists in the 'nt1_addresses' file
    grep -q "$ip_address" "$output_file"

    # If the IP address doesn't exist in the 'nt1_addresses' file, write it to the output file
    if [ $? -ne 0 ]; then
        echo "$(get_timestamp) :  $ip_address" >> "$output_file"
    fi
done

# Get the updated checksum of the output file
updated_checksum=$(calculate_checksum "$output_file")

# Check if the checksums are different, indicating a change in the file
if [ "$initial_checksum" != "$updated_checksum" ]; then
    # If the file has changed, do the following
    # INSERT YOUR SCRIPT HERE
fi