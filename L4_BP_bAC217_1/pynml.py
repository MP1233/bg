from netpyne import specs, sim, conversion

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters



"""

cellRule = netParams.importCellParams(
        label='PYR_HH3D_hoc',
        conds={'cellType': 'PYR', 'cellModel': 'HH3D'},
        fileName='geom.hoc',
        cellName='E21',
        importSynMechs=False)

cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70} # soma hh mechanism

for secName in cellRule['secs']:
        cellRule['secs'][secName]['mechs']['pas'] = {'g': 0.0000357, 'e': -70}
        cellRule['secs'][secName]['geom']['cm'] = 1

"""
## Population parameters
#netParams.popParams['E'] = {'cellType': 'E', 'numCells': 5, 'yRange': [700,800], 'cellModel': 'HH'}

## Cell property rules
#netParams.loadCellParamsRule(label='Erule', fileName='PT5B_full_cellParams.json')
#netParams.loadCellParamsRule(label='Erule', fileName='test.json')

#netParams.cellParams['Erule']['conds'] = {'cellType': ['E']}

#page 415 for model completeness in non-NEURON contexts, and to enable units checking, v should be declared in the ASSIGNED block


cellRule = netParams.importCellParams(
        label='PYR_HH3D_hoc',
        conds={'cellType': 'PYR', 'cellModel': 'HH3D'},
        fileName='createsimulation.hoc',
        cellName='bAC217_L4_BP_d04c4872bd',
        importSynMechs=True)


"""
## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 50, 'noise': 0.0}
netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 'conds': {'cellType': ['E']}, 'weight': 10.0, 'sec': 'soma', 'delay': 15, 'synMech': 'exc'}

"""
# Simulation options
simConfig = specs.SimConfig()        # object of class SimConfig to store simulation configuration
simConfig.duration = 0.05*1e3           # Duration of the simulation, in ms
simConfig.dt = 0.1                # Internal integration timestep to use
simConfig.verbose = False            # Show detailed messages
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'cell_lfp'  # Set file output name



#sim.importNeuroML2SimulateAnalyze('SimpleNet.net.nml', simConfig)
"""
nrml = conversion.neuromlFormat
#'SimpleNet.net.nml'
#'cACint209_L4_SBC_7382b080d8_0_0.cell.nml'
wtf = nrml.importNeuroML2('cACint209_L4_SBC_7382b080d8_0_0.cell.nml',simConfig)
#print wtf

nrhoc = conversion.neuronPyHoc
#wtf2 = nrhoc.importCell('morphology.hoc','morphology_d04c4872bd')

pynrml = conversion.pythonScript
#pynrml.createPythonScript('generated_python.py', wtf2, simConfig)
#pynrml.createPythonScript('generated_python.py', netParams, simConfig)
pynrml.createPythonScript('generated_python3.py', sim.net, simConfig)
#pynrml.createPythonScript('generated_python2.py', wtf, simConfig)

netParams.save('wow.json')
#wtf2.save('oops.json')
#sim.net.cells.save('oops.json')
"""
simConfig.recordLFP = [[x, y, 35] for y in range(280, 1000, 150) for x in [30, 90]]

simConfig.analysis['plotTraces'] = {'include': [('E',0)], 'oneFigPer':'cell', 'overlay': True, 'figSize': (5,3),'saveFig': True}      # Plot recorded traces for this list of cells
simConfig.analysis['plotLFP'] = {'includeAxon': False, 'plots': ['timeSeries',  'locations'], 'figSize': (5,9), 'saveFig': True}
simConfig.analysis['getCSD'] = {'spacing_um': 150, 'vaknin': True}
simConfig.analysis['plotCSD'] = {'timeRange': [10,45],'saveFig': True}
#sim.analysis.getCSD(spacing_um= 150, vaknin= True)
simConfig.analysis['plotCSD'] = {'saveFig': True}


# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)    
sim.analysis.plotCSD()

# check model output
sim.checkOutput('cell_lfp')



