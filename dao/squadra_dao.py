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
    
    @classmethod
    def get_nations_never_won_championship_organized_by_them(cls):
        MySql.openConnection()
        MySql.query(f"select * \
                        from squadra \
                        where PosizioneInClassifica != 1")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Squadra(element[0], element[1], element[2], element[3]))
        MySql.closeConnection()
        
        return results