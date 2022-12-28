from dao.utility.db import MySql
from dto.squadra_dto import Squadra

class Squadra_dao:
    @classmethod
    def get_all_teams(cls):
        MySql.openConnection()
        MySql.query(f"select * from squadra")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def get_team_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"select * from squadra s where s.id ={id}")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data