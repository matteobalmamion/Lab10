from database.DB_connect import DBConnect
from model.border import Border
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getBorders(year):
        conn = DBConnect.get_connection()
        result={}
        query="select * from contiguity where `year` <=%s"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query,(year,))
        for row in cursor:
            border=Border(row["state1no"],row["state2no"],row["year"],row["conttype"])
            if border.state1no in result:
                result[border.state1no].append(border)
            else:
                result[border.state1no] = [border]
            if border.state2no in result:
                result[border.state2no].append(border)
            else:
                result[border.state2no] = [border]
        return result

    @staticmethod
    def getCountries():
        conn = DBConnect.get_connection()
        result=[]
        query="select * from country"
        cursor=conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Country(**row))
        return result