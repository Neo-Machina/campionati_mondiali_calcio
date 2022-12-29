from dao.utility.db import MySql
from dto.organizzazione_dto import Organizzazione

class Organizzazione_dao:
    @classmethod
    def get_nations_never_won_championship_organized_by_them(cls):
        MySql.openConnection()
        MySql.query(f"select nazione \
                        from organizzazione org \
                        where nazione not in ( \
                                            select nazione \
                                            from squadra s \
                                            where Anno = org.Anno and PosizioneInClassifica = 1 \
				                            )")  
        data = MySql.getResults()
        MySql.closeConnection()
        
        return data