#!/bin/bash

# Define directories
jpeg_dir="/Users/shawheennaderi/TextureSynthesis/JPEG"
output_dir="/Users/shawheennaderi/TextureSynthesis/Outputs"

# Convert PNG to JPEG and then run the synthesis script
for i in {1..12}; do
    jpg_file="${jpeg_dir}/${i}.jpg"
    output_file="${output_dir}/output_${i}.jpg"

    echo $jpg_file
    echo $output_file

    # Explicitly use the Python interpreter
    /usr/bin/python3 /Users/shawheennaderi/TextureSynthesis/synthesis.py --sample_path="$jpg_file" --out_path="$output_file"

    # Output the status
    echo "Processed $jpg_file, output saved to $output_file"
done

echo "All processing complete. Check $output_dir for results."

