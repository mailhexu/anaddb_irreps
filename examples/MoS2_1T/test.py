from anaddb_irreps import IrRepsAnaddb


def show_phbst_irreps():
    irr = IrRepsAnaddb(
        phbst_fname="/home/hexu/projects/Others/MoS2-P/MoS2_P/1T/run_PHBST.nc",
        ind_q=0, symprec=1e-1, degeneracy_tolerance=1e-4)
    irr.run()
    irr._show(True)


show_phbst_irreps()
