import datetime



class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod #não precisa de instancia
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} Minutos'
        return answer
        #print(now.year, now.month, now.day, now.hour,now.minute, now.second)