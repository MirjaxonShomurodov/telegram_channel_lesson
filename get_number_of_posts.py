from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """

    d = data["messages"]
    return len(d)

if __name__=="__main__":
    data=fromJson('data/result.json')
    print(get_number_of_posts(data))