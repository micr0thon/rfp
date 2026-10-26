#!/bin/sh

echo "Preparing installation of rfp..."

cp ./rfp.py ./rfp

chmod +x ./rfp

echo "Installing to /usr/local/bin (requires sudo authentication)..."
sudo mv ./rfp /usr/local/bin/rfp

echo "Complete. Run rfp to execute."
