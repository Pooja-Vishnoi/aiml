# When package is installed but import says - Module not found in jupyter

# Step 1 - get installed package actual path from command prompt using these steps
# > pip show <package name> in command prompt to see actual path of installed package
# Ex output : C:\Users\abcd\aiml\venv\Lib\site-packages
path_1 = "C:\Users\abcd\aiml\venv\Lib\site-packages"

# Step 2 - Check where is  python searching any package which we are importing here
import sys
sys.path
path_2 = sys.path

# Output
# ['C:\\Users\\abcd\\aiml\\aiml',
#  'C:\\Program Files\\Python312\\python312.zip',
# ..............
#  'C:\\Users\\abcd\\AppData\\Roaming\\Python\\Python312\\site-packages\\Pythonwin',
#  'C:\\Program Files\\Python312\\Lib\\site-packages']

# Step 3 - see if path-1 is in path_2 list. If not, follow these steps to set path. But its temporary and you hav eto run this command every time whne you start this program 
# Python path set up - ASk python to look into correct path
sys.path.append('C:\\Users\\abcd\\aiml\\venv\\Lib\\site-packages')