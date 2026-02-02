#!/bin/bash

# Configuration
CSV_FILE="icon_audit.csv"
SOURCE_DIR="$1"
DEST_DIR="renamed_icons_$(date +%Y%m%d_%H%M%S)"

# Help / Usage
if [ -z "$SOURCE_DIR" ]; then
    echo "Usage: $0 <path_to_original_icons_folder>"
    echo "Example: $0 /Users/username/Downloads/UI_icons"
    exit 1
fi

# Check if CSV exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: $CSV_FILE not found in current directory."
    exit 1
fi

# Create Destination Directory
mkdir -p "$DEST_DIR"
echo "📂 Created destination folder: $DEST_DIR"

# Counters
count_success=0
count_skip=0
count_error=0

# Read CSV and Process
# Skip the header line (1st line)
tail -n +2 "$CSV_FILE" | while IFS=';' read -r old_name new_name category tags notes; do
    # Remove carriage returns if any
    old_name=$(echo "$old_name" | tr -d '\r')
    new_name=$(echo "$new_name" | tr -d '\r')
    category=$(echo "$category" | tr -d '\r')

    # Create category slug (lowercase)
    category_slug=$(echo "$category" | tr '[:upper:]' '[:lower:]')

    # Construct paths
    src_path="$SOURCE_DIR/$old_name"
    category_dir="$DEST_DIR/$category_slug"
    dest_path="$category_dir/$new_name"

    # Ensure category directory exists
    mkdir -p "$category_dir"

    if [ -f "$src_path" ]; then
        cp "$src_path" "$dest_path"
        if [ $? -eq 0 ]; then
            echo "✅ Renamed: '$old_name' -> '$category_slug/$new_name'"
            ((count_success++))
        else
            echo "❌ Error copying: '$old_name'"
            ((count_error++))
        fi
    else
        echo "⚠️  Skipped (Not Found): '$old_name'"
        ((count_skip++))
    fi
done

echo "------------------------------------------------"
echo "🎉 Processing Complete!"
echo "📂 Output Directory: $DEST_DIR"
