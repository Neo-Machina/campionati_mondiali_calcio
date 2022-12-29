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
    
    @classmethod
    def get_players_3_championship_or_more_nation(cls):
        MySql.openConnection()
        MySql.query(f"select * \
                    from giocatore g \
                    where (select count(*) \
		                    from partecipazione \
		                    where IDGiocatore = g.id \
		                ) = 3 \
                    or (select count(distinct Nazione) \
                        from partecipazione \
                        where IDGiocatore = g.id \
                        ) > 1")
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data