from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell parameters/rules
PYRcell = {'secs': {}}
PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}  # soma params dict
PYRcell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  # soma geometry
PYRcell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  # soma hh mechanism
netParams.cellParams['PYR'] = PYRcell

## Population parameters
#netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20}

"""
netParams.popParams['Operator_PLUS'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Operator_MINUS'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['Component1_0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component1_1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component1_2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component1_3'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['Component2_0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component2_1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component2_2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Component2_3'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['Output_0PLUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0PLUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0PLUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0PLUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1PLUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1PLUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1PLUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1PLUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2PLUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2PLUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2PLUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2PLUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3PLUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3PLUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3PLUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3PLUS3'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['Output_0MINUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0MINUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0MINUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_0MINUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1MINUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1MINUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1MINUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1MINUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2MINUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2MINUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2MINUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2MINUS3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3MINUS0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3MINUS1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3MINUS2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3MINUS3'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['Output_0'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_3'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_4'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_5'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_6'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_-1'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_-2'] = {'cellType': 'PYR', 'numCells': 10}
netParams.popParams['Output_-3'] = {'cellType': 'PYR', 'numCells': 10}

netParams.popParams['FILTER'] = {'cellType': 'PYR', 'numCells': 10}
"""




netParams.popParams['TOTAL_INPUT'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Operator_PLUS'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Operator_MINUS'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['Component1_0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component1_1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component1_2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component1_3'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['Component2_0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component2_1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component2_2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Component2_3'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['Output_0PLUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0PLUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0PLUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0PLUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1PLUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1PLUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1PLUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1PLUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2PLUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2PLUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2PLUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2PLUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3PLUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3PLUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3PLUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3PLUS3'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['Output_0MINUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0MINUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0MINUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_0MINUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1MINUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1MINUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1MINUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1MINUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2MINUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2MINUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2MINUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2MINUS3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3MINUS0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3MINUS1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3MINUS2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3MINUS3'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['Output_0'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_3'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_4'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_5'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_6'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_-1'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_-2'] = {'cellType': 'PYR', 'numCells': 1}
netParams.popParams['Output_-3'] = {'cellType': 'PYR', 'numCells': 1}

netParams.popParams['FILTER'] = {'cellType': 'PYR', 'numCells': 1}



## Synaptic mechanism parameters
#netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  # excitatory synaptic mechanism
#netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.01, 'tau2': 15.0, 'e': -95}


netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism






exc_weight = 1.0
exc_weight2 = 1.0
exc_weight3 = 1.0

exc_delay1 = 3
exc_delay2 = 4
exc_delay3 = 5

## Cell connectivity rules
"""
netParams.stimTargetParams['bkg->PYRplus'] = {'source': 'bkg', 'conds': {'pop': 'Operator_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg->PYR2'] = {'source': 'bkg', 'conds': {'pop': 'Component1_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg->PYR3'] = {'source': 'bkg', 'conds': {'pop': 'Component2_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
"""
netParams.connParams['TI1'] = {    'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'Operator_PLUS'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['TI2'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'Component1_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['TI3'] = {     'preConds': {'pop': 'TOTAL_INPUT'},    'postConds': {'pop': 'Component2_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


#OSCILLATORS
"""
netParams.connParams['OscPLUS'] = {    'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Operator_PLUS'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['OscMINUS'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Operator_MINUS'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Osc1_0'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Component1_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc1_1'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Component1_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc1_2'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Component1_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc1_3'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Component1_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc2_0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Component2_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc2_1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Component2_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc2_2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Component2_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
netParams.connParams['Osc2_3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Component2_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}
"""




#FILTER
"""
netParams.connParams['1_0+0'] = {     'preConds': {'pop': ['Operator_PLUS','Operator_MINUS','Component1_0','Component1_1','Component1_2','Component1_3','Component2_0','Component2_1','Component2_2','Component2_3']},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
"""
#FILTER
"""
netParams.connParams['F_PLUS'] = {     'preConds': {'pop': 'Operator_PLUS'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_MINUS'] = {     'preConds': {'pop': 'Operator_MINUS'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_1_0'] = {     'preConds': {'pop': 'Component1_0'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_1_1'] = {     'preConds': {'pop': 'Component1_1'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_1_2'] = {     'preConds': {'pop': 'Component1_2'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_1_3'] = {     'preConds': {'pop': 'Component1_3'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_2_0'] = {     'preConds': {'pop': 'Component2_0'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_2_1'] = {     'preConds': {'pop': 'Component2_1'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_2_2'] = {     'preConds': {'pop': 'Component2_2'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 
netParams.connParams['F_2_3'] = {     'preConds': {'pop': 'Component2_3'},       # conditions of presyn cells
    'postConds': {'pop': 'FILTER'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'exc'} 



netParams.connParams['FFF'] = {    #  S -> M label
    'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': ['Output_0PLUS0','Output_0PLUS1','Output_0PLUS2','Output_0PLUS3','Output_1PLUS0','Output_1PLUS1','Output_1PLUS2','Output_1PLUS3','Output_2PLUS0','Output_2PLUS1','Output_2PLUS2','Output_2PLUS3','Output_3PLUS0','Output_3PLUS1','Output_3PLUS2','Output_3PLUS3','Output_0MINUS0','Output_0MINUS1','Output_0MINUS2','Output_0MINUS3','Output_1MINUS0','Output_1MINUS1','Output_1MINUS2','Output_1MINUS3','Output_2MINUS0','Output_2MINUS1','Output_2MINUS2','Output_2MINUS3','Output_3MINUS0','Output_3MINUS1','Output_3MINUS2','Output_3MINUS3']},      # conditions of postsyn cells
    'probability': 1.0,               # probability of connection
    'weight': 0.91,                 # synaptic weight
    'delay': 1,                     # transmission delay (ms)
    'synMech': 'inh'}               # synaptic mechanism    

netParams.connParams['FFF2'] = {    #  S -> M label
    'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': ['Output_0PLUS0','Output_0PLUS1','Output_0PLUS2','Output_0PLUS3','Output_1PLUS0','Output_1PLUS1','Output_1PLUS2','Output_1PLUS3','Output_2PLUS0','Output_2PLUS1','Output_2PLUS2','Output_2PLUS3','Output_3PLUS0','Output_3PLUS1','Output_3PLUS2','Output_3PLUS3','Output_0MINUS0','Output_0MINUS1','Output_0MINUS2','Output_0MINUS3','Output_1MINUS0','Output_1MINUS1','Output_1MINUS2','Output_1MINUS3','Output_2MINUS0','Output_2MINUS1','Output_2MINUS2','Output_2MINUS3','Output_3MINUS0','Output_3MINUS1','Output_3MINUS2','Output_3MINUS3']},      # conditions of postsyn cells
    'probability': 1.0,               # probability of connection
    'weight': 0.91,                 # synaptic weight
    'delay': 1,                     # transmission delay (ms)
    'synMech': 'inh'}               # synaptic mechanism   

netParams.connParams['FFF3'] = {    #  S -> M label
    'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': ['Output_0PLUS0','Output_0PLUS1','Output_0PLUS2','Output_0PLUS3','Output_1PLUS0','Output_1PLUS1','Output_1PLUS2','Output_1PLUS3','Output_2PLUS0','Output_2PLUS1','Output_2PLUS2','Output_2PLUS3','Output_3PLUS0','Output_3PLUS1','Output_3PLUS2','Output_3PLUS3','Output_0MINUS0','Output_0MINUS1','Output_0MINUS2','Output_0MINUS3','Output_1MINUS0','Output_1MINUS1','Output_1MINUS2','Output_1MINUS3','Output_2MINUS0','Output_2MINUS1','Output_2MINUS2','Output_2MINUS3','Output_3MINUS0','Output_3MINUS1','Output_3MINUS2','Output_3MINUS3']},      # conditions of postsyn cells
    'probability': 1.0,               # probability of connection
    'weight': 0.91,                 # synaptic weight
    'delay': 2,                     # transmission delay (ms)
    'synMech': 'inh'}               # synaptic mechanism  
"""
#FILTER
"""
netParams.connParams['F_0+0'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_0+1'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_0+2'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_0+3'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_1+0'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_1+1'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_1+2'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_1+3'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_2+0'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_2+1'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_2+2'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_2+3'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_3+0'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_3+1'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_3+2'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
netParams.connParams['F_3+3'] = {     'preConds': {'pop': 'FILTER'},       # conditions of presyn cells
    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,     'weight': 0.91,     'delay': 5,     'synMech': 'inh'} 
"""

#CALCULATION


netParams.connParams['1_0+0'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0+0'] = {    'preConds': {'pop': 'Output_0PLUS0'},    'postConds': {'pop': 'Output_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0+1'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0+1'] = {    'preConds': {'pop': 'Output_0PLUS1'},    'postConds': {'pop': 'Output_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0+2'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0+2'] = {    'preConds': {'pop': 'Output_0PLUS2'},    'postConds': {'pop': 'Output_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0+3'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0+3'] = {    'preConds': {'pop': 'Output_0PLUS3'},    'postConds': {'pop': 'Output_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_1+0'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1+0'] = {    'preConds': {'pop': 'Output_1PLUS0'},    'postConds': {'pop': 'Output_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1+1'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1+1'] = {    'preConds': {'pop': 'Output_1PLUS1'},    'postConds': {'pop': 'Output_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1+2'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1+2'] = {    'preConds': {'pop': 'Output_1PLUS2'},    'postConds': {'pop': 'Output_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1+3'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1+3'] = {    'preConds': {'pop': 'Output_1PLUS3'},    'postConds': {'pop': 'Output_4'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_2+0'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_2+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2+0'] = {    'preConds': {'pop': 'Output_2PLUS0'},    'postConds': {'pop': 'Output_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2+1'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_2+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2+1'] = {    'preConds': {'pop': 'Output_2PLUS1'},    'postConds': {'pop': 'Output_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2+2'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_2+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0+2'] = {    'preConds': {'pop': 'Output_2PLUS2'},    'postConds': {'pop': 'Output_4'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2+3'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_2+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2+3'] = {    'preConds': {'pop': 'Output_2PLUS3'},    'postConds': {'pop': 'Output_5'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_3+0'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_3+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3+0'] = {    'preConds': {'pop': 'Output_3PLUS0'},    'postConds': {'pop': 'Output_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3+1'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_3+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3+1'] = {    'preConds': {'pop': 'Output_3PLUS1'},    'postConds': {'pop': 'Output_4'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3+2'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_3+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3+2'] = {    'preConds': {'pop': 'Output_3PLUS2'},    'postConds': {'pop': 'Output_5'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3+3'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['PLUS_3+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3+3'] = {    'preConds': {'pop': 'Output_3PLUS3'},    'postConds': {'pop': 'Output_6'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}



netParams.connParams['1_0-0'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_0-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0-0'] = {    'preConds': {'pop': 'Output_0MINUS0'},    'postConds': {'pop': 'Output_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0-1'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_0-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0-1'] = {    'preConds': {'pop': 'Output_0MINUS1'},    'postConds': {'pop': 'Output_-1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0-2'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_0-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0-2'] = {    'preConds': {'pop': 'Output_0MINUS2'},    'postConds': {'pop': 'Output_-2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_0-3'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_0-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0-3'] = {    'preConds': {'pop': 'Output_0MINUS3'},    'postConds': {'pop': 'Output_-3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_1-0'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1-0'] = {    'preConds': {'pop': 'Output_1MINUS0'},    'postConds': {'pop': 'Output_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1-1'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1-1'] = {    'preConds': {'pop': 'Output_1MINUS1'},    'postConds': {'pop': 'Output_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1-2'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1-2'] = {    'preConds': {'pop': 'Output_1MINUS2'},    'postConds': {'pop': 'Output_-1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_1-3'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_1-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['1-3'] = {    'preConds': {'pop': 'Output_1MINUS3'},    'postConds': {'pop': 'Output_-2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_2-0'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2-0'] = {    'preConds': {'pop': 'Output_2MINUS0'},    'postConds': {'pop': 'Output_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2-1'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2-1'] = {    'preConds': {'pop': 'Output_2MINUS1'},    'postConds': {'pop': 'Output_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2-2'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['0-2'] = {    'preConds': {'pop': 'Output_2MINUS2'},    'postConds': {'pop': 'Output_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_2-3'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['2-3'] = {    'preConds': {'pop': 'Output_2MINUS3'},    'postConds': {'pop': 'Output_-1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}


netParams.connParams['1_3-0'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_3-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS0'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3-0'] = {    'preConds': {'pop': 'Output_3MINUS0'},    'postConds': {'pop': 'Output_3'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3-1'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_3-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS1'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3-1'] = {    'preConds': {'pop': 'Output_3MINUS1'},    'postConds': {'pop': 'Output_2'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3-2'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_3-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS2'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3-2'] = {    'preConds': {'pop': 'Output_3MINUS2'},    'postConds': {'pop': 'Output_1'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}

netParams.connParams['1_3-3'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': exc_weight2,    'delay': exc_delay2,    'synMech': 'exc'} 
netParams.connParams['MINUS_3-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS3'},     'probability': 1.0,     'weight': exc_weight3,    'delay': exc_delay3,     'synMech': 'exc'} 
netParams.connParams['3-3'] = {    'preConds': {'pop': 'Output_3MINUS3'},    'postConds': {'pop': 'Output_0'},    'probability': 1.0,    'weight': exc_weight,    'delay': 5,    'synMech': 'exc'}












inh_delay = 2
inh_delay2 = 2
inh_delay3 = 2

inh_weight = 1.0









netParams.connParams['AxonComponent10_1p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}

netParams.connParams['AxonComponent10_1m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_1m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_2m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent10_3m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}




netParams.connParams['AxonComponent11_0p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}

netParams.connParams['AxonComponent11_0m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_0m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_2m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent11_3m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}



netParams.connParams['AxonComponent12_1p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}

netParams.connParams['AxonComponent12_1m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_1m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_0m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent12_3m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}



netParams.connParams['AxonComponent13_1p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}

netParams.connParams['AxonComponent13_1m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_1m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_2m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}
netParams.connParams['AxonComponent13_0m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'}







netParams.connParams['AxonComponent20_0p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_0p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_0p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}

netParams.connParams['AxonComponent20_0m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_0m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_0m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_1m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_2m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent20_3m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}



netParams.connParams['AxonComponent21_0p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_0p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_0p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}

netParams.connParams['AxonComponent21_0m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_0m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_0m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_1m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_2m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent21_3m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}



netParams.connParams['AxonComponent22_0p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_0p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_0p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}

netParams.connParams['AxonComponent22_0m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_0m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_0m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_1m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_2m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent22_3m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}



netParams.connParams['AxonComponent23_0p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_0p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_0p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}

netParams.connParams['AxonComponent23_0m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_0m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_0m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_1m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_2m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}
netParams.connParams['AxonComponent23_3m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay2,    'synMech': 'inh'}






netParams.connParams['AxonComponentm_1p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_1p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_1p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_1p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_2p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_2p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_2p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_2p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_0p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_0p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_0p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_0p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_3p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_3p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_3p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentm_3p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}

netParams.connParams['AxonComponentp_1m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_1m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_1m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_1m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_2m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_2m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_2m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_2m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_0m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_0m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_0m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_0m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_3m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_3m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_3m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}
netParams.connParams['AxonComponentp_3m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': 1.0,    'weight': inh_weight,    'delay': inh_delay3,    'synMech': 'inh'}



























# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}
#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

"""
netParams.stimTargetParams['bkg->PYRplus'] = {'source': 'bkg', 'conds': {'pop': 'Operator_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg->PYR2'] = {'source': 'bkg', 'conds': {'pop': 'Component1_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg->PYR3'] = {'source': 'bkg', 'conds': {'pop': 'Component2_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
"""
netParams.stimTargetParams['bkg->PYRplus'] = {'source': 'bkg', 'conds': {'pop': 'TOTAL_INPUT'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

#1 oscilator
#2 PLUS MINUS
#3 filter
#4 html
#6layers
#+(+)



# Simulation options
simConfig = specs.SimConfig()       # object of class SimConfig to store simulation configuration

simConfig.duration = 1*1e3          # Duration of the simulation, in ms
simConfig.dt = 0.025                # Internal integration timestep to use
simConfig.verbose = False           # Show detailed messages
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1          # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'tut2'  # Set file output name
simConfig.savePickle = False        # Save params, network and sim output to pickle file
simConfig.saveJson = True

simConfig.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
simConfig.analysis['plotTraces'] = {'include': [0,11,12], 'saveFig': True}  # 0 - PLUS, 2 - Comp 1 0, 6 - Comp 2 0, 
simConfig.analysis['plot2Dnet'] = {'saveFig': True}                   # plot 2D cell positions and connections

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)

# import pylab; pylab.show()  # this line is only necessary in certain systems where figures appear empty

# check model output
sim.checkOutput('tut2')
