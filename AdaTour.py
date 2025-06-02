from Controllers import *
from Models import *
from View import auth
import json

# Start Region of CONSTANT DATA
CONNECTION_STRING: str
try:
    with open('appsettings.json', 'r') as f:
        config = json.load(f)
        CONNECTION_STRING = config["ConnectionStrings"]["DefaultConnection"]
except:
    raise "Check appsettings.json"


# End Region of CONSTANT DATA

# Start Region of Main Program
def main():
    auth.home_page()

# End Region of Main Program
if __name__ == "__main__":
    main()