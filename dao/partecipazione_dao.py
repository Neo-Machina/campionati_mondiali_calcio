from dao.utility.db import MySql
from dto.partecipazione_dto import Partecipazione

class Squadra_dao:
    @classmethod
    def get_all_participations(cls):
        MySql.openConnection()
        MySql.query(f"select * from partecipazione")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data
    
    @classmethod
    def get_participation_by_id_player(cls, id_giocatore):
        MySql.openConnection()
        MySql.query(f"select * from partecipazione p where p.IDGIOCATORE ={id_giocatore}")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data