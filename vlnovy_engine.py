import numpy as np
import matplotlib.pyplot as plt


class VlnovyEngine:
    """
    Engine, ktorý prekladá vytŕčajúce vektory protónu
    na priestorovú interferenciu v mriežke.
    """

    def __init__(self, rozlisenie_mriezky=100):
        # Vytvoríme 2D rez Higgsovou mriežkou pre názornú vizualizáciu
        x = np.linspace(-100, 100, rozlisenie_mriezky)
        y = np.linspace(-100, 100, rozlisenie_mriezky)
        self.X, self.Y = np.meshgrid(x, y)

        # Geometricko-topologický limit (odpovedá Bohrovmu polomeru ~53 pm)
        self.kritic_vzdialenost = 53.0

    def generuj_stojatu_vlnu(self, pozicia_jadra, pocet_gluonov=3):
        """
        Vypočíta šírenie vibrácií od protónu. Namiesto hmotnej častice
        generuje sférickú excitáciu v štruktúrovanom vákuu.
        """
        # Výpočet vzdialenosti každého bodu mriežky od jadra (polomer r)
        r = np.sqrt((self.X - pozicia_jadra[0]) ** 2 + (self.Y - pozicia_jadra[1]) ** 2)

        # Ochrana proti deleniu nulou v samotnom strede jadra
        r[r == 0] = 0.1

        # Vlnová funkcia reprezentujúca mechanické narušenie mriežky gluónmi.
        # Amplitúda klesá so vzdialenosťou, ale na 'kritic_vzdialenost'
        # mriežka vynúti vznik stabilnej fázovej rezonancie.
        vlnove_cislo = 2 * np.pi / self.kritic_vzdialenost

        # Sila excitácie je násobená počtom vytŕčajúcich gluónov (3 pre protón)
        amplituda_vibracii = (pocet_gluonov * np.sin(vlnove_cislo * r)) / (r * 0.05)

        return amplituda_vibracii


# --- Spustenie a Vizualizácia ---
if __name__ == "__main__":
    engine = VlnovyEngine()

    # Umiestnime náš protón (vodík) do stredu mriežky
    pozicia_protonu = [0, 0]

    # Vypočítame rezonančnú stopu (to, čomu klasická veda hovorí 'elektrón')
    rezonancna_mapa = engine.generuj_stojatu_vlnu(pozicia_protonu)

    # Vykreslenie výsledku
    plt.figure(figsize=(8, 6))

    # Použijeme teplotnú mapu, kde najvyššie hodnoty (červená/žltá)
    # reprezentujú najsilnejšiu stojatu vlnu (rezonančný uzol)
    plt.contourf(engine.X, engine.Y, np.abs(rezonancna_mapa), levels=50, cmap='inferno')
    plt.colorbar(label='Amplitúda stojatej vlny (Fázová odozva mriežky)')

    # Vyznačíme jadro
    plt.plot(pozicia_protonu[0], pozicia_protonu[1], 'wo', markersize=8, label='Protón (Jadro 3,25 klastra)')

    # Vyznačíme hranicu prvej rezonančnej sféry
    kruh_rezonancie = plt.Circle((0, 0), 53, color='cyan', fill=False, linestyle='--', linewidth=2,
                                 label='1. Rezonančná sféra (Topologický limit)')
    plt.gca().add_patch(kruh_rezonancie)

    plt.title("Vlnová podstata elektrónu: Stojatá vlna namiesto bodovej častice")
    plt.xlabel("Pikometre")
    plt.ylabel("Pikometre")
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.show()