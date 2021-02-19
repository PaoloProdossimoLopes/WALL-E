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

    def get_day():
        now = datetime.datetime.now()
        answer = f'Hoje é dia {now.day} '
        return answer
        #print(now.year, now.month, now.day, now.hour,now.minute, now.second)
    
    def eu_sou():
        answer = "eu sou Uuuuaaallyyyye"
        return answer

    def blessed():
        answer = 'amem'
        return answer
    
    def criador():
        answer = 'quen me criou foi o paolo'
        return answer