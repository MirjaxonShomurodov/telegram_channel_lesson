import json
from pprint import pprint 
def fromJson(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    f=open(file_path,'r',encoding="UTF8")
    data = f.read()
    return json.loads(data)

if __name__=="__main__":
    data=fromJson('data/result.json')
    pprint(data)
