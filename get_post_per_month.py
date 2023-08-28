from read_data import fromJson
from datetime import datetime

def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month
    Args:
        data (dict): a dictionary of posts  
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    msgs=data.get('messages')
    answer = {}
    for msg in msgs:
        date = msg['date']
        date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
        month_n=int(date.strftime('%m'))
        
        answer.setdefault(month_n,0)

        answer[month_n]+=1

    return answer       
data=fromJson('data/result.json')
print(get_post_per_month(data))



    
