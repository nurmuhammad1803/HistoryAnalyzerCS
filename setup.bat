@echo off

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing necessary Python libraries...
python -m pip install --upgrade pip

pip install -r requirements.txt

echo Setup completed successfully!

echo Running the project...
python main.py