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
                        having count(*) >= ( select count(*) \
                                            from partecipazione")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Partecipazione(element[0], element[1], element[2], element[3], element[4]))
        MySql.closeConnection()
        MySql.closeConnection()
        
        return results