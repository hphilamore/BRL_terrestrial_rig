Instructions for sample Python programs for OAK-D camera

1. Create virtual environment
python3 -m venv .venv

2. Activate
source .venv/bin/activate

3. Install required packages
python -m pip install --upgrade pip
python -m pip install depthai opencv-python

4. Test packages installed correctly 
python -c "import depthai, cv2; print('Both packages installed successfully')"

