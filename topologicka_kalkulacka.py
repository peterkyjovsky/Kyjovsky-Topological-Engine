class TopologicalEngineer:
    """
    Calculator for material design based on the Cluster Index (K_cc)
    and phase alignment in a 55-point Higgs lattice.
    """

    def __init__(self, project_name="New Compound"):
        self.project_name = project_name
        self.components = []
        self.k_cc_total = 0.0

    def add_element(self, element_name, nucleon_count, atom_count=1):
        """
        Calculates the Cluster Index for a given element and adds it to the compound.
        K_cc = N * 3.25
        """
        k_cc_atom = nucleon_count * 3.25
        k_cc_subtotal = k_cc_atom * atom_count

        self.components.append({
            'element': element_name,
            'k_cc_1_atom': k_cc_atom,
            'count': atom_count,
            'k_cc_total': k_cc_subtotal
        })
        self.k_cc_total += k_cc_subtotal

    def analyze_stability(self):
        """
        Evaluates the phase shift of the entire molecule/alloy and determines its topological state.
        """
        print(f"\n=== PROJECT ANALYSIS: {self.project_name} ===")
        for comp in self.components:
            print(
                f"- {comp['count']}x {comp['element']} (Atom K_cc: {comp['k_cc_1_atom']}) -> Contribution: {comp['k_cc_total']}")

        print("-" * 40)
        print(f"TOTAL CLUSTER INDEX (K_cc_total): {self.k_cc_total}")

        # Extract the decimal part (phase shift)
        phase_shift = self.k_cc_total % 1

        print(f"PHASE SHIFT (modulo 1): .{int(phase_shift * 100):02d}")
        print("STABILITY DIAGNOSIS:")

        if phase_shift == 0.0:
            print(">>> ABSOLUTE RESONANCE (Slipstream) <<<")
            print("Compound is perfectly phase-locked. Ideal, highly stable structure.")
        elif phase_shift == 0.25:
            print(">>> PHASE SHIFT 1/4 <<<")
            print("Asymmetrical tension. Compound is highly reactive and seeks a partner to balance the asymmetry.")
        elif phase_shift == 0.50:
            print(">>> PHASE SHIFT 1/2 <<<")
            print("Bipolar tension. Compound exhibits polarity, fluidity, or a tendency to form additional bridges.")
        elif phase_shift == 0.75:
            print(">>> PHASE SHIFT 3/4 <<<")
            print("Extreme wave 'suction'. Compound aggressively absorbs phase waves from its surroundings.")


# --- Run Simulations ---
if __name__ == "__main__":
    # Test 1: Molecular Nitrogen (N2) - demonstration of perfect phase locking
    nitrogen = TopologicalEngineer("Molecular Nitrogen (N2)")
    nitrogen.add_element("Nitrogen", nucleon_count=14, atom_count=2)
    nitrogen.analyze_stability()

    # Test 2: Water (H2O) - demonstration of unaligned resonance and polarity
    water = TopologicalEngineer("Water (H2O)")
    water.add_element("Hydrogen", nucleon_count=1, atom_count=2)
    water.add_element("Oxygen", nucleon_count=16, atom_count=1)
    water.analyze_stability()