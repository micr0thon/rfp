#!/bin/sh

echo "Preparing installation of rgfp..."

cp ./rgfp.py ./rgfp

chmod +x ./rgfp

echo "Installing to /usr/local/bin (requires sudo authentication)..."
sudo mv ./rgfp /usr/local/bin/rgfp

echo "Complete. Run rgfp to execute."