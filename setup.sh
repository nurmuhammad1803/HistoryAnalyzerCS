echo "Installing necessary Python libraries..."

python3 -m pip install --upgrade pip

pip3 install -r requirements.txt

echo "Setup completed successfully!"

python3 main.py