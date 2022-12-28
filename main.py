from dao.squadra_dao import Squadra_dao
from dao.giocatore_dao import Giocatore_dao
from dao.partecipazione_dao import Partecipazione_dao
from dao.organizzazione_dao import Organizzazione_dao

squadre = Squadra_dao.get_nations_never_won_championship_organized_by_them()

for squadra in squadre:
    print(squadra)