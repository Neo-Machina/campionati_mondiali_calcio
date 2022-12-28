from dao.utility.db import MySql
from dto.organizzazione_dto import Organizzazione

class Organizzazione_dao:
    @classmethod
    def get_nations_never_won_championship_organized_by_them(cls):
        MySql.openConnection()
        MySql.query(f"select * \
                        from organizzazione org \
                        where nazione not in ( \
                                            select nazione \
                                            from squadra s \
                                            where PosizioneInClassifica = 1 \
				                            ) as squadre_vincenti")  
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(Organizzazione(element[0], element[1]))
        MySql.closeConnection()
        
        return results