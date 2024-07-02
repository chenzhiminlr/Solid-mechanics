# voronoi volume
import numpy as np
from ovito.io import import_file, export_file
from ovito.vis import *
from ovito.pipeline import *
from ovito.modifiers import *
from ovito.data import *
import os

os.chdir('your_path_to_data')
n_data = 16
for i in range(1,n_data+1):
    pipeline = import_file('{}/loading/video_*.cfg'.format(i), multiple_frames = True,sort_particles=True)
    pipeline.modifiers.append(VoronoiAnalysisModifier())
    data = pipeline.compute(0)
    N_frames = pipeline.source.num_frames
    AtomType = data.particles['Particle Type'][...]
    N_atoms = len(data.particles['Particle Identifier'][...])
    voro = np.zeros((N_atoms,N_frames+2))
    voro[:,0] = data.particles['Particle Type'][...]
    voro[:,1] = data.particles['Particle Identifier'][...]
    for frame in range(N_frames):
        data = pipeline.compute(frame)
        voro[:,frame+2] = data.particles['Atomic Volume'][...]
    np.savetxt('voro_sio2_{}.csv'.format(i), voro, delimiter=',', fmt='%s')