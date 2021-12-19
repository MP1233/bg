from netpyne import specs, sim
import os

SAVE_CPU = 2.0
#57853.87 s
#Total time = 15802.92 s

# template.hoc replace $1 > 1
#morphology.hoc add load_file("import3d.hoc")
#morphology.hoc replace           nl.input("morphology/dend-C300797C-P4_axon-C200897C-P4_-_Scale_x1.000_y1.025_z1.000_-_Clone_11.asc")
#with           nl.input("L4_PC_cADpyr230_1/morphology/dend-C300797C-P4_axon-C200897C-P4_-_Scale_x1.000_y1.025_z1.000_-_Clone_11.asc")
#in synapses/synapses.hoc replace all new File("synapses/synapses.tsv")
#with new File("L4_PC_cADpyr230_1/synapses/synapses.tsv")

"""
execute `nrnivmodl L4_BP_bAC217_1/mechanisms`
execute `nrnivmodl mechanisms`

After changing the file names for the second cell, you need to edit its template.hoc file also:

    load_file("morphology_1.hoc")
    load_file("biophysics_1.hoc")
    load_file("synapses/synapses_1.hoc")


    print use in synapses.hoc and by use find type of synapse and synapse id. put ids in SynMech:[]
"""


# Network parameters


#xChCx, xSBCx LBC




netParams = specs.NetParams()  # object of class NetParams to store the network parameters





PYRcell = {'secs': {}}
PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}  # soma params dict
PYRcell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  # soma geometry
PYRcell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  # soma hh mechanism
netParams.cellParams['PYR'] = PYRcell
netParams.popParams['OPERATOR_PLUS'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['OPERATOR_MINUS'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT1_0'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT1_1'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT1_2'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT1_3'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT2_0'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT2_1'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT2_2'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['COMPONENT2_3'] = {'cellType': 'PYR', 'numCells': 17}

netParams.popParams['fOPERATOR_PLUS'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['fCOMPONENT1_1'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['fCOMPONENT2_2'] = {'cellType': 'PYR', 'numCells': 17}
"""
netParams.popParams['BLOCK300'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['BLOCK700'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['BLOCK900'] = {'cellType': 'PYR', 'numCells': 17}
netParams.popParams['BLOCK1100'] = {'cellType': 'PYR', 'numCells': 17}
"""




"""
cellRule = netParams.importCellParams(
        label='PYR_HH3D_hoc',
        fileName='L23_PC_cADpyr229_1/template.hoc',
        cellName='cADpyr229_L23_PC_5ecbf9b163', #'cADpyr230_L4_SP_6fe41ae9cd', #'bAC217_L4_BP_d04c4872bd',
        importSynMechs=True)

netParams.popParams['test1'] = {'cellType': 'PYR_HH3D_hoc', 'numCells': 1}
"""


cellRule = netParams.importCellParams(
        label='L23_PC_HH3D_hoc',
        fileName='L23_PC_cADpyr229_2/template.hoc',
        cellName='cADpyr229_L23_PC_8ef1aa6602', #'cADpyr230_L4_SP_6fe41ae9cd', #'bAC217_L4_BP_d04c4872bd',
        importSynMechs=True)
"""
netParams.popParams['0PLUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['0PLUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['0PLUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['0PLUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1PLUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1PLUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['1PLUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['1PLUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}

netParams.popParams['2PLUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2PLUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2PLUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2PLUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['3PLUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}

netParams.popParams['3PLUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}

netParams.popParams['3PLUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}

netParams.popParams['3PLUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['0MINUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['0MINUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['0MINUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['0MINUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1MINUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1MINUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1MINUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['1MINUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2MINUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2MINUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2MINUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['2MINUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['3MINUS0_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['3MINUS1_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""
netParams.popParams['3MINUS2_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
netParams.popParams['3MINUS3_L23_PC'] = {'cellType': 'L23_PC_HH3D_hoc', 'numCells': int(61/SAVE_CPU)}
"""



cellRule = netParams.importCellParams(
        label='L23_LBC_HH3D_hoc',
        fileName='L23_LBC_bNAC219_1/template.hoc',
        cellName='bNAC219_L23_LBC_fe2122c75c', #'cADpyr230_L4_SP_6fe41ae9cd', #'bAC217_L4_BP_d04c4872bd',
        importSynMechs=True)

netParams.popParams['FILTER_L23_LBC'] = {'cellType': 'L23_LBC_HH3D_hoc', 'numCells': 20}
"""
cellRule = netParams.importCellParams(
        label='STELL_HH3D_hoc',
        fileName='L4_SS_cADpyr230_1/template.hoc',
        cellName='cADpyr230_L4_SS_9e49de205b', #'cADpyr230_L4_SP_6fe41ae9cd', #'bAC217_L4_BP_d04c4872bd',
        importSynMechs=True)

netParams.popParams['test2'] = {'cellType': 'STELL_HH3D_hoc', 'numCells': 1}
"""





netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism


print ("SSSSSSSSSSSSSMMMMMMMMMMMM" )
for a in netParams.synMechParams : 
        print (a)
        print (netParams.synMechParams[a])





"""
    "L23_PC:L23_PC":{
        "number_of_convergent_neuron_std":37,
        "connection_probability":5.6000000000000005,
        "number_of_divergent_neuron_std":42,
        "total_synapse_count":1562050,
        "mean_number_of_synapse_per_connection":2.8,
        "common_neighbor_bias":3.2,
        "number_of_convergent_neuron_mean":61,
        "number_of_synapse_per_connection_std":1.2,
        "number_of_divergent_neuron_mean":61
    },

        "L23_PC:L23_PC":{
        "gsyn_mean":0.3,
        "epsp_mean":1.9,
        "risetime_std":0.92,
        "f_std":2.7,
        "gsyn_std":0.11,
        "u_std":0.14,
        "decay_mean":47,
        "latency_mean":1.3,
        "failures_mean":3.9,
        "u_mean":0.46,
        "d_std":9.1,
        "synapse_type":"Excitatory, depressing",
        "space_clamp_correction_factor":"Synaptic conductance not measured experimentally",
        "latency_std":0.42,
        "decay_std":5.2,
        "cv_psp_amplitude_std":0.1,
        "risetime_mean":1.9,
        "cv_psp_amplitude_mean":0.43,
        "epsp_std":0.7,
        "d_mean":670,
        "f_mean":17,
        "failures_std":4.7
    },

    16:51-16:59

    """
#netParams.connParams['AxonComponentm_1p0a'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'test1'},    'probability': 15.6,    'weight': 200,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_27'} 

#netParams.connParams['AxonComponentm_1p0d'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'test1'},    'probability': 15.6,    'weight': 200,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_120'} 

"""
Added excitatory synapse 73 originating from cell 606 of m-type L23_PC on apical section 2(0.328000) and dep 664.000000 use 0.354234 
Added excitatory synapse 74 originating from cell 606 of m-type L23_PC on apical section 5(0.970000) and dep 655.000000 use 0.213351 
Added excitatory synapse 77 originating from cell 633 of m-type L23_PC on apical section 9(0.593000) and dep 660.000000 use 0.293921 
"""


#netParams.connParams['AxonComponentm_1p0d'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'test1'},    'probability': 1,    'weight': 200,    'delay': 1.3,    'synMech': ['cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_935', 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_930']} 

#AVOID SHOCK WAVE ON L23_PCs. ASYNCHRONIZE THEM. 1 make small weights 2 make probabilities < 1 to allow different combinations.

#CONFIGURATION 1: 2 syn, prob 1, weight 0.5, del 1.3
#netParams.connParams['AxonComponentm_2e'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'test1'},    'probability': 1,    'weight': 0.5,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_935'} 
#netParams.connParams['AxonComponentm_2f'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'test1'},    'probability': 1,    'weight': 0.5,    'delay': 1.4,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_930'} 

total_input_weight = 0.31 #0.31 best #0.30-0.35 if partial match doesn't disappear - use L23_LBC # 0.35 ideal for both! #0.5 BOTH OSC! 2nd too early #0.25 OSC! #0.35 EQ! #0.25 very good # 0.5

def InputNeuronsLayer23(_Neuron1, _Neuron2) : 


        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_1'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_885'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_2'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.4,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_884'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_3'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_939'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_4'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.4,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_975'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_5'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_985'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_6'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.4,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_937'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_7'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.3,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_947'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_8'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.25,    'weight': total_input_weight,    'delay': 1.4,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_892'} 

def NeuronsLayer23PCTOLayer23LBC(_Neuron1, _Neuron2) : 
#totnum of syn = 2.8(L23PC>L23PC)*0.3k_Num to GABA(L23PC>) = 0.9
        L23PC_L23LBC_weight = 1.0
        L23PC_L23LBC_delay = 0.5

        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_1'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_68'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_2'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_147'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_3'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_46'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_4'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_250'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_5'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_47'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_6'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_40'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_7'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_39'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_8'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_38'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_9'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_406'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_10'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.09,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay,    'synMech': 'bNAC219_L23_LBC_fe2122c75c_ProbAMPANMDA_EMS_454'} 



NeuronsLayer23PCTOLayer23LBC('0PLUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0PLUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0PLUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0PLUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1PLUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1PLUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1PLUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1PLUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2PLUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2PLUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2PLUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2PLUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3PLUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3PLUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3PLUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3PLUS3_L23_PC', 'FILTER_L23_LBC')

NeuronsLayer23PCTOLayer23LBC('0MINUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0MINUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0MINUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('0MINUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1MINUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1MINUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1MINUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('1MINUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2MINUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2MINUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2MINUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('2MINUS3_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3MINUS0_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3MINUS1_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3MINUS2_L23_PC', 'FILTER_L23_LBC')
NeuronsLayer23PCTOLayer23LBC('3MINUS3_L23_PC', 'FILTER_L23_LBC')



def NeuronsLayer23LBCTOLayer23LPC(_Neuron1, _Neuron2) : 
#totnum of syn = 2.8(L23PC>L23PC)*0.3k_Num to GABA(L23PC>) = 0.9
        L23PC_L23LBC_weight = 0.5 #35.0
        L23PC_L23LBC_delay = 0.5 #30
        L23PC_L23LBC_delay_k = 2.0

        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_1'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 0.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_873'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_2'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 1.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_1288'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_3'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 2.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_1162'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_4'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 3.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_847'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_5'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 4.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_569'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_6'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 5.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_588'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_7'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 6.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_587'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_8'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 7.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_586'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_9'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 8.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_597'} 
        netParams.connParams['Axon_' + _Neuron1 + '_' + _Neuron2 + '_10'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 0.19,    'weight': L23PC_L23LBC_weight,    'delay': L23PC_L23LBC_delay + 9.0*L23PC_L23LBC_delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbGABAAB_EMS_596'} 






NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0PLUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0PLUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0PLUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0PLUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1PLUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1PLUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1PLUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1PLUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2PLUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2PLUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2PLUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2PLUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3PLUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3PLUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3PLUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3PLUS3_L23_PC')

NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0MINUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0MINUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0MINUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '0MINUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1MINUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1MINUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1MINUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '1MINUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2MINUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2MINUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2MINUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '2MINUS3_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3MINUS0_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3MINUS1_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3MINUS2_L23_PC')
NeuronsLayer23LBCTOLayer23LPC('FILTER_L23_LBC', '3MINUS3_L23_PC')




"""

"""
#netParams.popParams['fOPERATOR_PLUS'] = {'cellType': 'PYR', 'numCells': 17}
InputNeuronsLayer23('fOPERATOR_PLUS', '0PLUS0_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '0PLUS1_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '0PLUS2_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '0PLUS3_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '1PLUS0_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '1PLUS1_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '1PLUS2_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '1PLUS3_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '2PLUS0_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '2PLUS1_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '2PLUS2_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '2PLUS3_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '3PLUS0_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '3PLUS1_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '3PLUS2_L23_PC')
InputNeuronsLayer23('fOPERATOR_PLUS', '3PLUS3_L23_PC')

#netParams.popParams['fCOMPONENT1_1'] = {'cellType': 'PYR', 'numCells': 17}
InputNeuronsLayer23('fCOMPONENT1_1', '1PLUS0_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1PLUS1_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1PLUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1PLUS3_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1MINUS0_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1MINUS1_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1MINUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT1_1', '1MINUS3_L23_PC')

#netParams.popParams['fCOMPONENT2_2'] = {'cellType': 'PYR', 'numCells': 17}
InputNeuronsLayer23('fCOMPONENT2_2', '0PLUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '1PLUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '2PLUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '3PLUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '0MINUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '1MINUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '2MINUS2_L23_PC')
InputNeuronsLayer23('fCOMPONENT2_2', '3MINUS2_L23_PC')



InputNeuronsLayer23('OPERATOR_PLUS', '0PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '0PLUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '0PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '0PLUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '0PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '0PLUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '0PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '0PLUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_PLUS', '1PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '1PLUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '1PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '1PLUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '1PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '1PLUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '1PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '1PLUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_PLUS', '2PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '2PLUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '2PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '2PLUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '2PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '2PLUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '2PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '2PLUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_PLUS', '3PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3PLUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '3PLUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '3PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3PLUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '3PLUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '3PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3PLUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '3PLUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_PLUS', '3PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3PLUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '3PLUS3_L23_PC')


InputNeuronsLayer23('OPERATOR_MINUS', '0MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '0MINUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '0MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '0MINUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '0MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '0MINUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '0MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_0', '0MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '0MINUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_MINUS', '1MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '1MINUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '1MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '1MINUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '1MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '1MINUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '1MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_1', '1MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '1MINUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_MINUS', '2MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '2MINUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '2MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '2MINUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '2MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '2MINUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '2MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_2', '2MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '2MINUS3_L23_PC')

InputNeuronsLayer23('OPERATOR_MINUS', '3MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3MINUS0_L23_PC')
InputNeuronsLayer23('COMPONENT2_0', '3MINUS0_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '3MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3MINUS1_L23_PC')
InputNeuronsLayer23('COMPONENT2_1', '3MINUS1_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '3MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3MINUS2_L23_PC')
InputNeuronsLayer23('COMPONENT2_2', '3MINUS2_L23_PC')
InputNeuronsLayer23('OPERATOR_MINUS', '3MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT1_3', '3MINUS3_L23_PC')
InputNeuronsLayer23('COMPONENT2_3', '3MINUS3_L23_PC')



#1 input on apical L1
#2 Input > osc1 61 > osc2 61 > osc1 61

"""
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_483
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_503
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_502
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_501
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_370
cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_571
Added excitatory synapse 985 originating from cell 7324 of m-type L23_PC on basal section 53(0.966000) and dep 685.000000 use 0.666524 
Added excitatory synapse 986 originating from cell 7324 of m-type L23_PC on basal section 19(0.211000) and dep 668.000000 use 0.411139 
Added excitatory synapse 987 originating from cell 7324 of m-type L23_PC on basal section 60(0.737000) and dep 683.000000 use 0.645544 
Added excitatory synapse 988 originating from cell 7324 of m-type L23_PC on apical section 11(0.128000) and dep 667.000000 use 0.395561 
Added excitatory synapse 989 originating from cell 7350 of m-type L23_PC on apical section 18(0.862000) and dep 666.000000 use 0.384939 
Added excitatory synapse 990 originating from cell 7350 of m-type L23_PC on basal section 27(0.180000) and dep 665.000000 use 0.360758 
Added excitatory synapse 991 originating from cell 7494 of m-type L23_PC on basal section 27(0.493000) and dep 683.000000 use 0.643938 
Added excitatory synapse 992 originating from cell 7494 of m-type L23_PC on basal section 8(0.857000) and dep 656.000000 use 0.233770 
Added excitatory synapse 993 originating from cell 7540 of m-type L23_PC on basal section 14(0.811000) and dep 675.000000 use 0.522245 
Added excitatory synapse 994 originating from cell 7540 of m-type L23_PC on basal section 55(0.483000) and dep 665.000000 use 0.365931 
Added excitatory synapse 995 originating from cell 7540 of m-type L23_PC on basal section 53(0.698000) and dep 674.000000 use 0.505717 
Added excitatory synapse 996 originating from cell 7540 of m-type L23_PC on apical section 1(0.831000) and dep 658.000000 use 0.261172 
Added excitatory synapse 997 originating from cell 7604 of m-type L23_PC on basal section 65(0.371000) and dep 668.000000 use 0.407136 
Added excitatory synapse 998 originating from cell 7604 of m-type L23_PC on apical section 20(0.354000) and dep 664.000000 use 0.352564 
Added excitatory synapse 999 originating from cell 7632 of m-type L23_PC on basal section 42(0.486000) and dep 682.000000 use 0.634709 
Added excitatory synapse 1000 originating from cell 7632 of m-type L23_PC on basal section 42(0.519000) and dep 670.000000 use 0.438682 
Added excitatory synapse 1001 originating from cell 7666 of m-type L23_PC on apical section 13(0.664000) and dep 658.000000 use 0.266720 
Added excitatory synapse 1002 originating from cell 7666 of m-type L23_PC on apical section 18(0.834000) and dep 684.000000 use 0.660437 
Added excitatory synapse 1003 originating from cell 7666 of m-type L23_PC on apical section 20(0.019000) and dep 666.000000 use 0.389600 
Added excitatory synapse 1004 originating from cell 7755 of m-type L23_PC on basal section 65(0.667000) and dep 680.000000 use 0.596118 
Added excitatory synapse 1005 originating from cell 7755 of m-type L23_PC on basal section 35(0.625000) and dep 659.000000 use 0.273036 
Added excitatory synapse 1006 originating from cell 7755 of m-type L23_PC on basal section 38(0.115000) and dep 683.000000 use 0.637420 
Added excitatory synapse 1007 originating from cell 7774 of m-type L23_PC on basal section 18(0.759000) and dep 665.000000 use 0.368005 
Added excitatory synapse 1008 originating from cell 7774 of m-type L23_PC on basal section 18(0.798000) and dep 658.000000 use 0.259768 

As in vivo, photo-stimulation of the same neuronal sub-classes in vitro also generated potent gamma
oscillations (Fig. 3A–F; peak frequency, L4: 36 ± 1 Hz,
L2/3: 28 ± 1 Hz, L5: 38 ± 2 Hz; L6: 51 ± 3 Hz, n = 8
"""





#must be n_syn * weight = 60. delay must cover refractory period
# 1 - Reduce TOTAL_INPUT weight until dense test1 reaction & no shockwave afterblock
#AVOID SHOCK WAVE ON L23_PCs. ASYNCHRONIZE THEM. 1 make small weights 2 make probabilities < 1 to allow different combinations. but first find optimal weight
# 2 - test1 > test1a > test1 - reduce weight and delay step by step until delay = 20-25. OR 1.3 but 40Hz osc
#60*6*weight = 60. equilibrium weight 1/6

#afferent = 61 aff neurons * 2.8 syn * 1.9 weight * probability of spiking = 60 >>> probability of spiking = 1/6. probability of spiking NOT connection probability IS asynchrony of 1/6
#add noise

#w 1 d 70
#w 1.5 d 120
#w 3.9 d 100
#w 25 d 30
weight_k = 25*SAVE_CPU #25! #10.0 #7.9 #2.9 #1.9
prob_k = 0.24/15.6
delay_k = 30.0 #30 #100.0


#MUST BE 12 syn * prob 0.24



#//////////////////////////////////////////

def JoinNeuronsLayer23(_Neuron1, _Neuron2) : 

        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_1'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_851'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_2'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_1195'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_3'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_1063'} 

        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_4'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_574'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_5'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_581'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_6'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_748'} 



        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_7'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_483'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_8'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_503'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_9'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_502'} 

        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_10'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_501'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_11'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_370'} 
        netParams.connParams['Axon_'+_Neuron1+'_'+ _Neuron2 + '_12'] = {     'preConds': {'pop': _Neuron1},    'postConds': {'pop': _Neuron2},    'probability': 15.6*prob_k,    'weight': 1.9*weight_k,    'delay': 1.3 + 1.0*delay_k,    'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_571'} 



JoinNeuronsLayer23('0PLUS0_L23_PC', '0PLUS0_L23_PC')
JoinNeuronsLayer23('0PLUS1_L23_PC', '0PLUS1_L23_PC')
JoinNeuronsLayer23('0PLUS2_L23_PC', '0PLUS2_L23_PC')
JoinNeuronsLayer23('0PLUS3_L23_PC', '0PLUS3_L23_PC')
JoinNeuronsLayer23('1PLUS0_L23_PC', '1PLUS0_L23_PC')
JoinNeuronsLayer23('1PLUS1_L23_PC', '1PLUS1_L23_PC')
JoinNeuronsLayer23('1PLUS2_L23_PC', '1PLUS2_L23_PC')
JoinNeuronsLayer23('1PLUS3_L23_PC', '1PLUS3_L23_PC')
JoinNeuronsLayer23('2PLUS0_L23_PC', '2PLUS0_L23_PC')
JoinNeuronsLayer23('2PLUS1_L23_PC', '2PLUS1_L23_PC')
JoinNeuronsLayer23('2PLUS2_L23_PC', '2PLUS2_L23_PC')
JoinNeuronsLayer23('2PLUS3_L23_PC', '2PLUS3_L23_PC')
JoinNeuronsLayer23('3PLUS0_L23_PC', '3PLUS0_L23_PC')
JoinNeuronsLayer23('3PLUS1_L23_PC', '3PLUS1_L23_PC')
JoinNeuronsLayer23('3PLUS2_L23_PC', '3PLUS2_L23_PC')
JoinNeuronsLayer23('3PLUS3_L23_PC', '3PLUS3_L23_PC')

JoinNeuronsLayer23('0MINUS0_L23_PC', '0MINUS0_L23_PC')
JoinNeuronsLayer23('0MINUS1_L23_PC', '0MINUS1_L23_PC')
JoinNeuronsLayer23('0MINUS2_L23_PC', '0MINUS2_L23_PC')
JoinNeuronsLayer23('0MINUS3_L23_PC', '0MINUS3_L23_PC')
JoinNeuronsLayer23('1MINUS0_L23_PC', '1MINUS0_L23_PC')
JoinNeuronsLayer23('1MINUS1_L23_PC', '1MINUS1_L23_PC')
JoinNeuronsLayer23('1MINUS2_L23_PC', '1MINUS2_L23_PC')
JoinNeuronsLayer23('1MINUS3_L23_PC', '1MINUS3_L23_PC')
JoinNeuronsLayer23('2MINUS0_L23_PC', '2MINUS0_L23_PC')
JoinNeuronsLayer23('2MINUS1_L23_PC', '2MINUS1_L23_PC')
JoinNeuronsLayer23('2MINUS2_L23_PC', '2MINUS2_L23_PC')
JoinNeuronsLayer23('2MINUS3_L23_PC', '2MINUS3_L23_PC')
JoinNeuronsLayer23('3MINUS0_L23_PC', '3MINUS0_L23_PC')
JoinNeuronsLayer23('3MINUS1_L23_PC', '3MINUS1_L23_PC')
JoinNeuronsLayer23('3MINUS2_L23_PC', '3MINUS2_L23_PC')
JoinNeuronsLayer23('3MINUS3_L23_PC', '3MINUS3_L23_PC')






netParams.connParams['Axon_PLUS_BLOCK300'] = {     'preConds': {'pop':'BLOCK300'},    'postConds': {'pop':'OPERATOR_PLUS'},    'probability': 1,    'weight': 5.1, 'delay': 3, 'synMech': 'inh'} 
netParams.connParams['Axon_PLUS_BLOCK900'] = {     'preConds': {'pop':'BLOCK900'},    'postConds': {'pop':'BLOCK300'},    'probability': 1,    'weight': 5.1, 'delay': 3, 'synMech': 'inh'} 
netParams.connParams['Axon_PLUS_BLOCK1100'] = {     'preConds': {'pop':'BLOCK1100'},    'postConds': {'pop':'BLOCK900'},    'probability': 1,    'weight': 5.1, 'delay': 3, 'synMech': 'inh'} 




netParams.stimSourceParams['bkg_1'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 100, 'duration': 200}
netParams.stimSourceParams['bkg_1i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 300, 'duration': 200}
#netParams.stimSourceParams['bkg_1pl'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 100, 'duration': 200}
#netParams.stimSourceParams['bkg_1ipl'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 300, 'duration': 200}

netParams.stimSourceParams['bkg_11'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 500, 'duration': 200}
netParams.stimSourceParams['bkg_11i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 700, 'duration': 200}

netParams.stimSourceParams['bkg_111'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 900, 'duration': 200}
netParams.stimSourceParams['bkg_111i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 1100, 'duration': 200}
###############################
#netParams.stimTargetParams['bkg_1->PLUSUnblock'] = {'source': 'bkg_111', 'conds': {'pop': 'bkg_1ipl'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg_1->PLUSUnblockUnblock'] = {'source': 'bkg_111i', 'conds': {'pop': 'bkg_111'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}


###############################

#netParams.stimSourceParams['bkg_111ii'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 1100, 'duration': 200}
#netParams.stimSourceParams['bkg_111iii'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 1100, 'duration': 200}

netParams.stimTargetParams['bkg_i>BLOCK300'] = {'source': 'bkg_1i', 'conds': {'pop': 'BLOCK300'}, 'weight': 1.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_i>BLOCK700'] = {'source': 'bkg_11i', 'conds': {'pop': 'BLOCK700'}, 'weight': 1.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_i>BLOCK900'] = {'source': 'bkg_111', 'conds': {'pop': 'BLOCK900'}, 'weight': 1.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_i>BLOCK1100'] = {'source': 'bkg_111i', 'conds': {'pop': 'BLOCK1100'}, 'weight': 1.01, 'delay': 5, 'synMech': 'exc'}


netParams.stimTargetParams['bkg_1->CE3'] = {'source': 'bkg_1', 'conds': {'pop': '0PLUS2_L23_PC'}, 'weight': 0.01, 'delay': 5, 'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_851'}
netParams.stimTargetParams['bkg_1->CE3a'] = {'source': 'bkg_1', 'conds': {'pop': '3PLUS1_L23_PC'}, 'weight': 0.01, 'delay': 5, 'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_851'}
netParams.stimTargetParams['bkg_1->CE3aa'] = {'source': 'bkg_1', 'conds': {'pop': '3PLUS3_L23_PC'}, 'weight': 0.01, 'delay': 5, 'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_851'}

#0+2
netParams.stimTargetParams['bkg_1->PLUS'] = {'source': 'bkg_1', 'conds': {'pop': 'OPERATOR_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_1i>PLUS'] = {'source': 'bkg_1i', 'conds': {'pop': 'OPERATOR_PLUS'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_1->COMPONENT1_0'] = {'source': 'bkg_1', 'conds': {'pop': 'COMPONENT1_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_1i>COMPONENT1_0'] = {'source': 'bkg_1i', 'conds': {'pop': 'COMPONENT1_0'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_1->COMPONENT2_2'] = {'source': 'bkg_1', 'conds': {'pop': 'COMPONENT2_2'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_1i>COMPONENT2_2'] = {'source': 'bkg_1i', 'conds': {'pop': 'COMPONENT2_2'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}

#3-1
netParams.stimTargetParams['bkg_11->MINUS'] = {'source': 'bkg_11', 'conds': {'pop': 'OPERATOR_MINUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_11i>MINUS'] = {'source': 'bkg_11i', 'conds': {'pop': 'OPERATOR_MINUS'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_11->COMPONENT1_3'] = {'source': 'bkg_11', 'conds': {'pop': 'COMPONENT1_3'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_11i>COMPONENT1_3'] = {'source': 'bkg_11i', 'conds': {'pop': 'COMPONENT1_3'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_11->COMPONENT2_1'] = {'source': 'bkg_11', 'conds': {'pop': 'COMPONENT2_1'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_11i>COMPONENT2_1'] = {'source': 'bkg_11i', 'conds': {'pop': 'COMPONENT2_1'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}

#1+2
netParams.stimTargetParams['bkg_111->PLUS'] = {'source': 'bkg_111', 'conds': {'pop': 'fOPERATOR_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_111i>PLUS'] = {'source': 'bkg_111i', 'conds': {'pop': 'fOPERATOR_PLUS'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_111->COMPONENT1_1'] = {'source': 'bkg_111', 'conds': {'pop': 'fCOMPONENT1_1'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_111i>COMPONENT1_1'] = {'source': 'bkg_111i', 'conds': {'pop': 'fCOMPONENT1_1'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_111->COMPONENT2_2'] = {'source': 'bkg_111', 'conds': {'pop': 'fCOMPONENT2_2'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_111i>COMPONENT2_2'] = {'source': 'bkg_111i', 'conds': {'pop': 'fCOMPONENT2_2'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}

#netParams.stimTargetParams['bkg_1->CE4'] = {'source': 'bkg_1', 'conds': {'pop': 'test1b'}, 'weight': 0.1, 'delay': 5, 'synMech': 'cADpyr229_L23_PC_8ef1aa6602_ProbAMPANMDA_EMS_851'}








# Simulation options
simConfig = specs.SimConfig()

simConfig.duration = 1000
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}
simConfig.recordStep = 0.1
simConfig.filename = 'tut2'

"""
simConfig.analysis['plotTraces'] = {'saveFig': True}
simConfig.analysis['plot2Dnet'] = {'saveFig': True}
simConfig.analysis['plotShape'] = {'saveFig': True, showSyns=True} 
"""
##############
#simConfig.analysis['plotShape'] = {'saveFig': True, 'showSyns' : True, 'showFig':False} 
################
simConfig.analysis['plotRaster'] = {'saveFig': True, 'showFig':False}                  # Plot a raster
simConfig.analysis['plotTraces'] = {'include': [0,51,12,13,14,15], 'saveFig': True, 'showFig':False} #, 'saveData' : 'wow.json'} #590,595,600,605,610,615,620,625,630,635,640,645,650,655,660,665,670,675,680,685,690,695,700,705,710,715,120,725,730,735,740,745,750,755,760,765,770,775], 'saveFig': True} # ,65,215,225,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,360,365,370,375,380,385,390,395,400,405,410,415,420,425], 'saveFig': True}  # 0 - PLUS, 2 - Comp 1 0, 6 - Comp 2 0, 
#simConfig.analysis['plot2Dnet'] = {'saveFig': True, 'showFig':False}                   # plot 2D cell positions and connections
"""
simConfig.recordLFP = [[x, y, 35] for y in range(280, 1000, 150) for x in [30, 90]]

simConfig.analysis['plotTraces'] = {'include': [('E',0)], 'oneFigPer':'cell', 'overlay': True, 'figSize': (5,3),'saveFig': True}      # Plot recorded traces for this list of cells
simConfig.analysis['plotLFP'] = {'includeAxon': False, 'plots': ['timeSeries',  'locations'], 'figSize': (5,9), 'saveFig': True}
simConfig.analysis['getCSD'] = {'spacing_um': 150, 'vaknin': True}
"""

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)
