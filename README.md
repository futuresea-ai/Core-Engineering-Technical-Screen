# Core-Engineering-Technical-Screen: Package Sorting Challenge

## Problem Statement
We need to sort packages into categories based on their dimensions and weight.

### Rules
A package is classified as:

- **Bulky** if:
  - Its volume (Width × Height × Length) is **≥ 1,000,000 cm³**, OR
  - Any one dimension (Width, Height, Length) is **≥ 150 cm**
- **Heavy** if:
  - Its mass is **≥ 20 kg**

### Categories
- **STANDARD**: Packages that are neither heavy nor bulky
- **SPECIAL**: Packages that are either heavy OR bulky (but not both)
- **REJECTED**: Packages that are both heavy AND bulky
