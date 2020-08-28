from datetime import date,time,datetime,timedelta
from enum import Enum

class Format(Enum):
    YMDHMS = '%Y-%m-%d %H:%M:%S'
    YMD = '%Y-%m-%d'
    HMS = '%H:%M:%S'
    HM = '%H:%M'
    # 更多其他格式在这里添加

def dtFormat(dt:datetime,format):
    if format == Format.YMDHMS:
        return dt.strftime(Format.YMDHMS.value)
    if format == Format.YMD:
        return dt.date().today().isoformat()
    if format == Format.HMS:
        return dt.strftime(Format.HMS.value) 
    if format == Format.HM:
        return dt.strftime(Format.HM.value)


class dtchi(object):
    def __init__(self,dt):
        self._dt = dt 

    @staticmethod
    def today(format=Format.YMDHMS):
        """
        返回today的字符串格式
        """
        return dtFormat(datetime.now(),format=format)
          
    def dtdiff(self,days=0,format=Format.YMDHMS):
        """
        与当前时间的偏移
        days: 偏移小时数，可为负；若偏移一小时，days=1/24
        format 
        """
        t = self._dt + timedelta(days=days)
        return dtFormat(t,format=format) 
        

    
if __name__ == '__main__':
    print(dtFormat(datetime.now(),format=Format.YMDHMS))

    dt = dtchi(datetime.now())
    print(dt.dtdiff(days=-1/24))
