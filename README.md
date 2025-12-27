# Vortex Comparison Tool

A simple Python script to compare the characteristics of tornadoes and fire tornadoes (firewhirls). This educational tool is designed for students and early‑career meteorologists to understand the key differences in formation, energy sources, duration, and destructive potential between these two vortex types.

## Features

- **Two Python classes**: `Tornado` and `FireTornado` with scientifically accurate attributes.
- **Side‑by‑side comparison**: A `compare_vortices()` function prints a clear, formatted table.
- **Educational output**: Includes meteorological notes that explain the underlying science.
- **Ready to run**: No external dependencies; works with Python 3.6+.

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/ruqdr/vortex-comparison-tool.git
   cd vortex-comparison-tool
   ```

2. Run the script:
   ```bash
   python compare.py
   ```

3. View the comparison table and explanatory notes.

## Example Output

Running `python compare.py` produces output similar to the following:

```
================================================================================
COMPARISON: CLASSIC TORNADO vs. FIRE TORNADO
================================================================================

Attribute                | Classic Tornado          | Fire Tornado
--------------------------------------------------------------------------------
Formation mechanism      | Supercell thunderstorm mesocyclone | Intense ground‑level heat and wind shear
Primary energy source    | Latent heat release from condensation | Combustion (heat from fire)
Typical duration         | Minutes to hours         | Seconds to minutes
Destructive potential    | EF0‑EF5 (Enhanced Fujita Scale) | Extreme localized heat and ember transport
--------------------------------------------------------------------------------

Key Meteorological Notes:
• Tornadoes derive their rotation from pre‑existing mesocyclones within supercells.
• Fire tornadoes are driven by intense surface heating; rotation is often generated
  by local wind shear and the fire's own convection column.
• While tornadoes are rated on the Enhanced Fujita (EF) scale, fire tornadoes
  are not formally scaled but can produce catastrophic localised damage.
================================================================================
```

## Project Structure

- `compare.py` – Main script containing the classes and comparison function.
- `PROJECT_SCOPE.md` – Detailed requirements and acceptance criteria.
- `README.md` – This file.

## How It Works

1. The script defines two classes:
   - **`Tornado`**: Represents a classic tornado, with attributes based on supercell thunderstorm dynamics.
   - **`FireTornado`**: Represents a firewhirl, with attributes driven by combustion and intense surface heating.

2. Each class is instantiated with representative data drawn from meteorological literature.

3. The `compare_vortices()` function formats the attribute values into a readable table and prints it alongside explanatory notes.

## Contributing

Feel free to open issues or submit pull requests to improve the accuracy, add new features, or enhance the educational value of the tool. Please refer to `PROJECT_SCOPE.md` for the original project requirements.

## License

This project is licensed under the MIT License – see the LICENSE file for details.