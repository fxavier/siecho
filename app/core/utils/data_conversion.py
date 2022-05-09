from datetime import datetime

class DataConversion:
    
    @staticmethod
    def convert_int_date(int_date):
        if int_date is None:
            date_str_format = '1900-01-01 00:00:00'
            return datetime.strptime(date_str_format, '%Y-%m-%d %H:%M:%S')
        return datetime.fromtimestamp(int_date / 1e3)
        
    
    #datetime.fromtimestamp(data['ultimo_lev'] / 1e3)