import numpy as np
import matplotlib.pyplot as plt


class KomplexnaInterferencia:
    """
    Engine demonštrujúci preplnenie prvej rezonančnej vrstvy
    a vznik smerových uzlov (sp3) pri uhlíku v Higgsovej mriežke.
    """

    def __init__(self, rozlisenie=300):
        # Širšie zorné pole pre zobrazenie druhej vrstvy
        x = np.linspace(-200, 200, rozlisenie)
        y = np.linspace(-200, 200, rozlisenie)
        self.X, self.Y = np.meshgrid(x, y)

        # Prevod do polárnych súradníc pre jednoduchšiu prácu so smerovosťou vĺn
        self.R = np.sqrt(self.X ** 2 + self.Y ** 2)
        self.Theta = np.arctan2(self.Y, self.X)
        self.R[self.R == 0] = 0.1  # Ochrana proti deleniu nulou

        # Limity mriežky
        self.limit_1_vrstva = 53.0  # Polomer prvej (preplnenej) vrstvy
        self.limit_2_vrstva = 150.0  # Polomer druhej (smerovej) vrstvy

    def simuluj_uhlik(self):
        """
        Simuluje 18 vytŕčajúcich gluónov uhlíka.
        Prvá vrstva sa preplní (sférická) a druhá vrstva sa formuje
        pozdĺž smerových osí ikosahedra (4 uzly v 2D reze).
        """
        vlnove_cislo_1 = 2 * np.pi / self.limit_1_vrstva
        vlnove_cislo_2 = 2 * np.pi / self.limit_2_vrstva

        # 1. PRVÁ VRSTVA: Masívny sférický nápor z 18 gluónov
        # Tlmíme ju vo väčšej vzdialenosti, pretože energia sa "vytláča" von
        amplituda_1 = (18 * np.sin(vlnove_cislo_1 * self.R)) / (self.R * 0.1)
        maska_1 = np.exp(-(self.R - self.limit_1_vrstva) ** 2 / 1000)
        vlna_1 = amplituda_1 * maska_1

        # 2. DRUHÁ VRSTVA: Smerové šírenie (odtlačok vrcholov ikosahedra)
        # Matematicky pridáme uhlovú závislosť (sin(2*Theta)), ktorá vytvorí 4 uzly
        smerovy_faktor = np.abs(np.sin(2 * self.Theta))

        # Rezonancia druhej vrstvy vzniká len tam, kde smerový faktor zosilňuje vlnu
        amplituda_2 = (18 * np.sin(vlnove_cislo_2 * self.R)) / (self.R * 0.05)
        maska_2 = np.exp(-(self.R - self.limit_2_vrstva) ** 2 / 3000)
        vlna_2 = amplituda_2 * maska_2 * smerovy_faktor

        # Celková fázová mapa je súčtom oboch rezonancií
        celkova_rezonancia = vlna_1 + vlna_2
        return celkova_rezonancia


# --- Spustenie a Vizualizácia ---
if __name__ == "__main__":
    engine = KomplexnaInterferencia()
    rezonancna_mapa = engine.simuluj_uhlik()

    plt.figure(figsize=(10, 8))

    # Vykreslíme mapu stojatých vĺn
    plt.contourf(engine.X, engine.Y, np.abs(rezonancna_mapa), levels=80, cmap='plasma')
    plt.colorbar(label='Fázová odozva (Amplitúda stojatej vlny)')

    # Vyznačenie jadra Uhlíka (39 klastrov)
    plt.plot(0, 0, 'wo', markersize=12, label='Jadro Uhlíka (39 klastrov)')

    # Vyznačenie preplnenej prvej vrstvy
    kruh_1 = plt.Circle((0, 0), 53, color='cyan', fill=False, linestyle='-', linewidth=2,
                        label='1. Vrstva (Preplnená sférická)')
    plt.gca().add_patch(kruh_1)

    # Vyznačenie druhej (smerovej) vrstvy
    kruh_2 = plt.Circle((0, 0), 150, color='lime', fill=False, linestyle='--', linewidth=1.5,
                        label='2. Vrstva (Smerový limit mriežky)')
    plt.gca().add_patch(kruh_2)

    plt.title("Uhlík: Preplnenie prvej vrstvy a vznik smerových väzobných uzlov ($sp^3$)")
    plt.xlabel("Pikometre")
    plt.ylabel("Pikometre")
    plt.legend(loc='upper right')
    plt.axis('equal')
    plt.show()