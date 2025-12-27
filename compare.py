#!/usr/bin/env python3
"""
Tornado vs. Fire Tornado Comparison Tool
Educational script for meteorology students.
"""

class Tornado:
    """Represents a classic tornado (mesocyclone-induced vortex)."""
    
    def __init__(self):
        self.formation_mechanism = "Supercell thunderstorm mesocyclone"
        self.primary_energy_source = "Latent heat release from condensation"
        self.typical_duration = "Minutes to hours"
        self.destructive_potential = "EF0‑EF5 (Enhanced Fujita Scale)"
    
    def __str__(self):
        return "Classic Tornado"


class FireTornado:
    """Represents a fire tornado (firewhirl) – a vortex driven by intense heat."""
    
    def __init__(self):
        self.formation_mechanism = "Intense ground‑level heat and wind shear"
        self.primary_energy_source = "Combustion (heat from fire)"
        self.typical_duration = "Seconds to minutes"
        self.destructive_potential = "Extreme localized heat and ember transport"
    
    def __str__(self):
        return "Fire Tornado (Firewhirl)"


def compare_vortices(tornado, fire_tornado):
    """
    Prints a side‑by‑side comparison of key attributes of a tornado and a fire tornado.
    """
    print("\n" + "=" * 80)
    print("COMPARISON: CLASSIC TORNADO vs. FIRE TORNADO")
    print("=" * 80)
    print("\nAttribute                | Classic Tornado          | Fire Tornado")
    print("-" * 80)
    print(f"{'Formation mechanism':<25} | {tornado.formation_mechanism:<25} | {fire_tornado.formation_mechanism}")
    print(f"{'Primary energy source':<25} | {tornado.primary_energy_source:<25} | {fire_tornado.primary_energy_source}")
    print(f"{'Typical duration':<25} | {tornado.typical_duration:<25} | {fire_tornado.typical_duration}")
    print(f"{'Destructive potential':<25} | {tornado.destructive_potential:<25} | {fire_tornado.destructive_potential}")
    print("-" * 80)
    print("\nKey Meteorological Notes:")
    print("• Tornadoes derive their rotation from pre‑existing mesocyclones within supercells.")
    print("• Fire tornadoes are driven by intense surface heating; rotation is often generated")
    print("  by local wind shear and the fire's own convection column.")
    print("• While tornadoes are rated on the Enhanced Fujita (EF) scale, fire tornadoes")
    print("  are not formally scaled but can produce catastrophic localised damage.")
    print("=" * 80)


if __name__ == "__main__":
    # Instantiate the two vortex types
    classic = Tornado()
    fire = FireTornado()
    
    # Display the comparison
    compare_vortices(classic, fire)
    
    # Optionally show individual summaries
    print("\nIndividual summaries:")
    print(f"{classic}: {classic.formation_mechanism}")
    print(f"{fire}: {fire.formation_mechanism}")