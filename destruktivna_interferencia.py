import numpy as np
import matplotlib.pyplot as plt


class DestruktivnaInterferencia:
    """
    Engine demonštrujúci mechanické odpudzovanie atómov (Pauliho princíp)
    cez fázovú nekompatibilitu v Higgsovej mriežke.
    """

    def __init__(self, rozlisenie_mriezky=200):
        x = np.linspace(-120, 120, rozlisenie_mriezky)
        y = np.linspace(-80, 80, rozlisenie_mriezky)
        self.X, self.Y = np.meshgrid(x, y)
        self.kritic_vzdialenost = 53.0

    def generuj_vlnu_jadra(self, pozicia_jadra, fazovy_posun=0.0):
        """
        Vypočíta excitačnú vlnu. Umožňuje zadať fázový posun,
        aby sme simulovali nekompatibilné atómy.
        """
        r = np.sqrt((self.X - pozicia_jadra[0]) ** 2 + (self.Y - pozicia_jadra[1]) ** 2)
        r[r == 0] = 0.1
        vlnove_cislo = 2 * np.pi / self.kritic_vzdialenost

        # Matematické pridanie fázového posunu priamo do vlnenia
        return (3 * np.sin(vlnove_cislo * r + fazovy_posun)) / (r * 0.05)

    def simuluj_odpudzovanie(self, vzdialenost_jadier):
        """
        Simuluje priblíženie dvoch fázovo nekompatibilných atómov.
        """
        pozicia_1 = [-vzdialenost_jadier / 2, 0]
        pozicia_2 = [vzdialenost_jadier / 2, 0]

        # Prvé jadro vibruje v základnej fáze
        vlna_1 = self.generuj_vlnu_jadra(pozicia_1, fazovy_posun=0.0)

        # Druhé jadro vibruje v absolútnej protifáze (posun o π, teda 180 stupňov)
        vlna_2 = self.generuj_vlnu_jadra(pozicia_2, fazovy_posun=np.pi)

        # DEŠTRUKTÍVNA INTERFERENCIA: Vlny narazia na seba tak, že sa vyrušia
        spolocna_rezonancia = vlna_1 + vlna_2

        return spolocna_rezonancia, pozicia_1, pozicia_2


# --- Spustenie a Vizualizácia ---
if __name__ == "__main__":
    engine = DestruktivnaInterferencia()

    # Atómy tlačíme k sebe na rovnakú vzdialenosť ako predtým
    vysledna_mapa, p1, p2 = engine.simuluj_odpudzovanie(vzdialenost_jadier=74.0)

    plt.figure(figsize=(10, 6))

    # Vykreslíme mapu vĺn
    plt.contourf(engine.X, engine.Y, np.abs(vysledna_mapa), levels=60, cmap='bone')
    plt.colorbar(label='Sila rezonančnej zóny')

    # Vyznačenie jadier
    plt.plot(p1[0], p1[1], 'wo', markersize=8, label='Atóm 1')
    plt.plot(p2[0], p2[1], 'wo', markersize=8, label='Atóm 2 (V protifáze)')

    # Zvýraznenie hluchého miesta v strede
    plt.axvline(x=0, color='red', linestyle='--', alpha=0.7, label='Hluchá zóna (mriežka zhasla)')

    plt.title("Deštruktívna interferencia: Absencia väzby a mechanické odpudzovanie")
    plt.xlabel("Pikometre")
    plt.ylabel("Pikometre")
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.show()