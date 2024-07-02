variable Si equal 1
variable O  equal 2

mass ${Si} 28.0855
mass ${O}  15.9994

set type ${Si} charge 2.4
set type ${O}  charge -1.2

pair_style     hybrid/overlay buck/coul/long 5.5 10.0 table linear 950
pair_coeff     * * buck/coul/long 0.0         1.0      0.0
pair_coeff     ${Si} ${Si} buck/coul/long 0.0         1.0      0.0
pair_coeff     ${Si} ${O}  buck/coul/long 414612.50   0.20520  3075.278
pair_coeff     ${O}  ${O}  buck/coul/long 31982.360   0.36231  4030.1136
pair_coeff     ${Si} ${Si} table ../bks.dat BKS_SISI
pair_coeff     ${Si} ${O}  table ../bks.dat BKS_SIO
pair_coeff     ${O}  ${O}  table ../bks.dat BKS_OO

kspace_style    pppm 1.0e-5
neighbor        2.0 bin
neigh_modify    every 1 check yes
timestep        1.0