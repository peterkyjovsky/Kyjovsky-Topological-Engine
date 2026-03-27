import numpy as np
import matplotlib.pyplot as plt


class TopologickaInterferencia:
    """
    Engine pre výpočet fázovej interferencie medzi viacerými atómami
    v 55-bodovej Higgsovej mriežke.
    """

    def __init__(self, rozlisenie_mriezky=200):
        # Širšie zorné pole pre zobrazenie dvoch atómov
        x = np.linspace(-120, 120, rozlisenie_mriezky)
        y = np.linspace(-80, 80, rozlisenie_mriezky)
        self.X, self.Y = np.meshgrid(x, y)

        # Topologický limit (Bohrov polomer v pikometroch)
        self.kritic_vzdialenost = 53.0

    def generuj_vlnu_jadra(self, pozicia_jadra, pocet_gluonov=3):
        """Vypočíta excitačnú vlnu jedného protónu (3 vytŕčajúce gluóny)."""
        r = np.sqrt((self.X - pozicia_jadra[0]) ** 2 + (self.Y - pozicia_jadra[1]) ** 2)
        r[r == 0] = 0.1
        vlnove_cislo = 2 * np.pi / self.kritic_vzdialenost
        # Vlna klesajúca so vzdialenosťou
        return (pocet_gluonov * np.sin(vlnove_cislo * r)) / (r * 0.05)

    def simuluj_kovalentnu_vazbu(self, vzdialenost_jadier):
        """
        Umiestni dve jadrá vedľa seba a vypočíta ich skalárne sčítavanie fázových posunov.
        """
        # Umiestnenie dvoch protónov na osi X
        pozicia_1 = [-vzdialenost_jadier / 2, 0]
        pozicia_2 = [vzdialenost_jadier / 2, 0]

        # Vygenerovanie vĺn z oboch nezávislých zdrojov
        vlna_1 = self.generuj_vlnu_jadra(pozicia_1)
        vlna_2 = self.generuj_vlnu_jadra(pozicia_2)

        # KONŠTRUKTÍVNA INTERFERENCIA: Sčítanie vĺn v štruktúrovanom vákuu
        # Toto je matematický dôkaz toho, čomu hovoríme "chemická väzba"
        spolocna_rezonancia = vlna_1 + vlna_2

        return spolocna_rezonancia, pozicia_1, pozicia_2


# --- Spustenie a Vizualizácia ---
if __name__ == "__main__":
    engine = TopologickaInterferencia()

    # Priblížime dva atómy vodíka na vzdialenosť 74 pikometrov
    # (čo je reálna dĺžka väzby v molekule H2)
    vysledna_mapa, p1, p2 = engine.simuluj_kovalentnu_vazbu(vzdialenost_jadier=74.0)

    plt.figure(figsize=(10, 6))

    # Vykreslenie intenzity stojatej vlny. Absolútna hodnota ukazuje silu rezonančného uzla.
    plt.contourf(engine.X, engine.Y, np.abs(vysledna_mapa), levels=60, cmap='magma')
    plt.colorbar(label='Sila spoločnej rezonančnej zóny (Slipstream)')

    # Vyznačenie jadier (každé obsadzuje 3,25 klastra)
    plt.plot(p1[0], p1[1], 'wo', markersize=8, label='Protón 1 (3,25 klastra)')
    plt.plot(p2[0], p2[1], 'wo', markersize=8, label='Protón 2 (3,25 klastra)')

    plt.title("Molekula $H_2$: Kovalentná väzba ako konštruktívne fázové uzamknutie")
    plt.xlabel("Pikometre")
    plt.ylabel("Pikometre")
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.show()