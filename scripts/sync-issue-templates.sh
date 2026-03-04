#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PRODUCT_TEMPLATE_ROOT="$(dirname "$SCRIPT_DIR")"
# Assuming standard workspace structure where repos are siblings
WORKSPACE_ROOT="$(dirname "$PRODUCT_TEMPLATE_ROOT")"
OPS_PLAYBOOK_DIR="$WORKSPACE_ROOT/ops-playbook"

SOURCE_DIR="$OPS_PLAYBOOK_DIR/github/issue_templates/product"
DEST_DIR="$PRODUCT_TEMPLATE_ROOT/.github/ISSUE_TEMPLATE"

echo "Product Template Root: $PRODUCT_TEMPLATE_ROOT"
echo "Source Directory: $SOURCE_DIR"
echo "Destination Directory: $DEST_DIR"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found at $SOURCE_DIR"
    echo "Please ensure ops-playbook is cloned as a sibling directory to product-template"
    exit 1
fi

# Create destination directory if it doesn't exist
if [ ! -d "$DEST_DIR" ]; then
    echo "Creating destination directory..."
    mkdir -p "$DEST_DIR"
fi

echo "Syncing 'product' issue templates..."
cp -v "$SOURCE_DIR"/*.yml "$DEST_DIR/"

echo "Sync complete!"
