@ECHO OFF
REM py -m pip install coverage
REM py -m unittest discover tests/Util
py -m coverage run -m unittest -v
py -m coverage html
PAUSE
