from dao.utility.db import MySql
from dto.partecipazione_dto import Partecipazione

class Partecipazione_dao:
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
    
    @classmethod
    def get_nation_has_max_players_for_championship(cls):
        MySql.openConnection()
        MySql.query(f"select anno, nazione, count(*) as numero_giocatori \
                        from partecipazione p \
                        group by p.anno, nazione \
                        having count(*) >= ALL ( select count(*) \
                                            from partecipazione \
                                            where p.anno = anno \
                                            group by Nazione)")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data