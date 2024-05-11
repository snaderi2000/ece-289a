#!/bin/bash

# Directory where the original PNG images are stored
input_dir="/Users/shawheennaderi/TextureSynthesis/Examples"

# Directory where the JPEG images will be stored
jpeg_dir="/Users/shawheennaderi/TextureSynthesis/JPEG"

# Create directory if it doesn't exist
mkdir -p "$jpeg_dir"

# Convert PNG to JPEG
for i in {1..12}; do
  png_file="$input_dir/$i.png"
  jpg_file="$jpeg_dir/$i.jpg"

  # Command to convert PNG to JPG
  gm convert "$png_file" "$jpg_file"
done

echo "Conversion complete. JPEGs are in $jpeg_dir."

