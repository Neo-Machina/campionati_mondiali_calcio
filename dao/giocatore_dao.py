from dao.utility.db import MySql
from dto.giocatore_dto import Giocatore

class Giocatore_dao:
    @classmethod
    def get_all_players(cls):
        MySql.openConnection()
        MySql.query(f"select * from giocatore")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def get_player_by_id(cls, id):
        MySql.openConnection()
        MySql.query(f"select * from giocatore g where g.id ={id}")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data