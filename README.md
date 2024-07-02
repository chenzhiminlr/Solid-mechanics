# Simulation and analyses for "Universal signatures for stress prediction in ordered and disordered solids"

## Content
- ```sample_data```: Sample datasets for SiO<sub>2</sub> glass and crystal.
- ```sample_potential```: Sample BKS potential for SiO<sub>2</sub> glass and crystal.
- ```scripts```: Shell and LAMMPS scripts for running simulations and loading.
- python scripts: Data processing and plot the figures.

## Dependencies
Python module dependencies are:
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [pandas](https://pypi.org/project/pandas/)
- [pickle](https://pypi.org/project/pickle5/)
- [ovito](https://pypi.org/project/ovito/)

## Potential for LAMMPS simulations
#### Beest Kramer van Santen (BKS) potential is used to simulated SiO<sub>2</sub> system
Vollmayr, K., Kob, W., & Binder, K. (1996). Cooling-rate effects in amorphous silica: A computer-simulation study. Physical Review B, 54(22), 15808.

#### Embedded Atom Method (EAM) potential is used to simulated Cu-Zr metallic glass system
Mendelev, M. I., Kramer, M. J., Ott, R. T., Sordelet, D. J., Yagodin, D., & Popel, P. J. P. M. (2009). Development of suitable interatomic potentials for simulation of liquid and amorphous Cu–Zr alloys. Philosophical Magazine, 89(11), 967-987.

#### Neuron network potential from our previews work is used to simulated Li<sub>3</sub>PS<sub>4</sub> solid electrolytes
Chen, Z., Du, T., Krishnan, N. M., Yue, Y., & Smedskjaer, M. M. (2024). Disorder-induced enhancement of lithium-ion transport in solid-state electrolytes. arXiv preprint arXiv:2401.05151.

[LiPS potential file](https://github.com/OxideGlassGroupAAU/LiPS)

#### Neuron network potential from our previews work is used to simulated zeolitic imidazolate frameworks system
Du, T., Li, S., Ganisetti, S., Bauchy, M., Yue, Y., & Smedskjaer, M. M. (2024). Deciphering the controlling factors for phase transitions in zeolitic imidazolate frameworks. National Science Review, nwae023.

[ZIF4 potential file](https://github.com/OxideGlassGroupAAU/DeepZIF)

#### Neuron network potential is used to simulated solid ice system
Zhang, L., Wang, H., Car, R., & E, W. (2021). Phase diagram of a deep potential water model. Physical review letters, 126(23), 236001.

#### Buckingham potential is ued to simulated sodium borate glass system
Deng, L., & Du, J. (2019). Development of boron oxide potentials for computer simulations of multicomponent oxide glasses. Journal of the American Ceramic Society, 102(5), 2482-2505.
