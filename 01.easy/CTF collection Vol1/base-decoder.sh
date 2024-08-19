#!/bin/bash

# Read input string from command prompt
read -p "Enter the encoded string: " encoded_string

# Display the original string
echo
echo "Original String: $encoded_string"
echo
# Decode using base32
decoded_base32=$(echo "$encoded_string" | base32 -d)
if [[ -n "$decoded_base32" ]]; then
    echo "Decoded (Base32): $decoded_base32"
fi

echo

# Decode using base58
decoded_base58=$(echo "$encoded_string" | base58 -d)
if [[ -n "$decoded_base58" ]]; then
    echo "Decoded (Base58): $decoded_base58"
fi

echo

# Decode using base64
decoded_base64=$(echo "$encoded_string" | base64 -d)
if [[ -n "$decoded_base64" ]]; then
    echo "Decoded (Base64): $decoded_base64"
fi

echo