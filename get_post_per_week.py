from read_data import fromJson
import datetime
def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        dict: a dictionary with the number of posts for each week.
    """
    msgs=data.get('messages')
    
    answer = {
        month:{}
    }

    for msg in msgs:
        date = msg['date']
        date = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
        month_n=int(date.strftime('%m'))
        week_n =int(date.strftime("%w"))

        if month==month_n:
            month_week = date.strftime('%V')
            answer[month].setdefault(month_week,0)
            answer[month][month_week]+=1
    return answer

data=fromJson('data/result.json')
print(get_post_per_week(data,10))

