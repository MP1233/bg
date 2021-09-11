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


#CALCULATOR MODULE

netParams.popParams['TOTAL_INPUT'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Operator_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Operator_PLUSosc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Operator_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Operator_MINUSosc'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['Component1_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_0osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_1osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_2osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component1_3osc'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['Component2_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_0osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_1osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_2osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Component2_3osc'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['Output_0PLUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0PLUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0PLUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0PLUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1PLUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1PLUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1PLUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1PLUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2PLUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2PLUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2PLUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2PLUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3PLUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3PLUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3PLUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3PLUS3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['Output_0MINUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0MINUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0MINUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0MINUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1MINUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1MINUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1MINUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1MINUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2MINUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2MINUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2MINUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2MINUS3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3MINUS0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3MINUS1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3MINUS2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3MINUS3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['Output_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_0osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_1osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_2osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_3osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_4'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_5'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_6'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_-1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_-2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['Output_-3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['FILTER'] = {'cellType': 'PYR', 'numCells': 5}


#INPUT MODULE


netParams.popParams['INPUT_CE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_EQ'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_PLUSf'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_2f'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['INPUT2_CE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_EQ'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT2_3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['INPUTosc_CE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_EQ'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc_3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['INPUTosc2_CE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_EQ'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUTosc2_3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['INPUT_FILTER_CE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_EQ'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['INPUT_FILTER_3'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['OUTPUT_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component2_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component2_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component2_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component2_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_0osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_1osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_2osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_3osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_0osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_1osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_2osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['OUTPUT_Component1_3osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['MERGE_SUMM_Component1_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['MERGE_SUMM_Component1_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['MERGE_SUMM_Component1_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['MERGE_SUMM_Component1_3'] = {'cellType': 'PYR', 'numCells': 5}



netParams.popParams['TRANSACTION_NEURON_EMPTY'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_EMPTY_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_EMPTY_osc2'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['TRANSACTION_NEURON_ONLY_VALUE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_VALUE_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_VALUE_osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_VALUE_killer'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['TRANSACTION_NEURON_ONLY_OPERATOR'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_OPERATOR_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_OPERATOR_osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_ONLY_OPERATOR_killer'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['TRANSACTION_NEURON_COMPLETEO'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEO_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEO_osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEO_killer'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['TRANSACTION_NEURON_COMPLETEV'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEV_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEV_osc2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETEV_killer'] = {'cellType': 'PYR', 'numCells': 5}

netParams.popParams['TRANSACTION_NEURON_COMPLETE'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETE_osc'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TRANSACTION_NEURON_COMPLETE_osc2'] = {'cellType': 'PYR', 'numCells': 5}


netParams.popParams['TRANSACTION_NEURON_COMPLETE_GPI'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_PLUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_MINUS'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component1_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component1_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component1_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component1_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component2_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component2_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component2_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['START_TRANSACTION_Component2_3'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['FINISH_TRANSACTION'] = {'cellType': 'PYR', 'numCells': 5}





netParams.popParams['Output_0123'] = {'cellType': 'PYR', 'numCells': 5}



netParams.popParams['TOTAL_RESULT_GPI'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TOTAL_RESULT_0'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TOTAL_RESULT_1'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TOTAL_RESULT_2'] = {'cellType': 'PYR', 'numCells': 5}
netParams.popParams['TOTAL_RESULT_3'] = {'cellType': 'PYR', 'numCells': 5}




## Synaptic mechanism parameters
#netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  # excitatory synaptic mechanism
#netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.01, 'tau2': 15.0, 'e': -95}


netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism






exc_weight = 0.006
exc_weight2 = 0.9
exc_weight3 = 0.9
inh_weight = 5.0

exc_weight4 = 0.006 #0.006 0.007

exc_delay1 = 3
exc_delay2 = 4
exc_delay3 = 5
exc_delayosc1 = 30

exc_probability1 = 0.1

exc_probability4 = 1.0 #1.0 #0.35

exc_probability5 = 1.0
exc_probability6 = 0.1

#///STEP 1 = INPUT CE/EQ/+/- , block others. INPUT 0/1/2/3 , block others

#    //1.1 OSCILATE INPUT

netParams.connParams['Axon_INPUT2_CE'] = {     'preConds': {'pop': 'INPUT_CE'},    'postConds': {'pop': 'INPUT2_CE'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_EQ'] = {     'preConds': {'pop': 'INPUT_EQ'},    'postConds': {'pop': 'INPUT2_EQ'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_PLUS'] = {     'preConds': {'pop': 'INPUT_PLUS'},    'postConds': {'pop': 'INPUT2_PLUS'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_PLUSf'] = {     'preConds': {'pop': 'INPUT_PLUSf'},    'postConds': {'pop': 'INPUT2_PLUS'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_MINUS'] = {     'preConds': {'pop': 'INPUT_MINUS'},    'postConds': {'pop': 'INPUT2_MINUS'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_0'] = {     'preConds': {'pop': 'INPUT_0'},    'postConds': {'pop': 'INPUT2_0'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_1'] = {     'preConds': {'pop': 'INPUT_1'},    'postConds': {'pop': 'INPUT2_1'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_2'] = {     'preConds': {'pop': 'INPUT_2'},    'postConds': {'pop': 'INPUT2_2'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_2f'] = {     'preConds': {'pop': 'INPUT_2f'},    'postConds': {'pop': 'INPUT2_2'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2_3'] = {     'preConds': {'pop': 'INPUT_3'},    'postConds': {'pop': 'INPUT2_3'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 


netParams.connParams['Axon_INPUT2OscCE'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'INPUTosc_CE'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2OscEQ'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'INPUTosc_EQ'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2OscPLUS'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'INPUTosc_PLUS'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2OscMINUS'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'INPUTosc_MINUS'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2Osc0'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'INPUTosc_0'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2Osc1'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'INPUTosc_1'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2Osc2'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'INPUTosc_2'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUT2Osc3'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'INPUTosc_3'},    'probability': exc_probability4,    'weight': exc_weight4,    'delay': exc_delay1,    'synMech': 'exc'} 



netParams.connParams['Axon_INPUTOscCE2'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'INPUTosc2_CE'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOscEQ2'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'INPUTosc2_EQ'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOscPLUS2'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'INPUTosc2_PLUS'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOscMINUS2'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'INPUTosc2_MINUS'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOsc02'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'INPUTosc2_0'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOsc12'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'INPUTosc2_1'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOsc22'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'INPUTosc2_2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUTOsc32'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'INPUTosc2_3'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 


netParams.connParams['Axonl_INPUTOscCE2'] = {     'preConds': {'pop': 'INPUTosc2_CE'},    'postConds': {'pop': 'INPUTosc_CE'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOscEQ2'] = {     'preConds': {'pop': 'INPUTosc2_EQ'},    'postConds': {'pop': 'INPUTosc_EQ'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOscPLUS2'] = {     'preConds': {'pop': 'INPUTosc2_PLUS'},    'postConds': {'pop': 'INPUTosc_PLUS'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOscMINUS2'] = {     'preConds': {'pop': 'INPUTosc2_MINUS'},    'postConds': {'pop': 'INPUTosc_MINUS'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOsc02'] = {     'preConds': {'pop': 'INPUTosc2_0'},    'postConds': {'pop': 'INPUTosc_0'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOsc12'] = {     'preConds': {'pop': 'INPUTosc2_1'},    'postConds': {'pop': 'INPUTosc_1'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOsc22'] = {     'preConds': {'pop': 'INPUTosc2_2'},    'postConds': {'pop': 'INPUTosc_2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axonl_INPUTOsc32'] = {     'preConds': {'pop': 'INPUTosc2_3'},    'postConds': {'pop': 'INPUTosc_3'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 



#    //1.2 BLOCK OTHERS

netParams.connParams['Axon_INPUT2filter_CE'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'INPUT_FILTER_CE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_CE_EQ'] = {     'preConds': {'pop': 'INPUT_FILTER_CE'},    'postConds': {'pop': 'INPUTosc_EQ'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_CE_PLUS'] = {     'preConds': {'pop': 'INPUT_FILTER_CE'},    'postConds': {'pop': 'INPUTosc_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_CE_MINUS'] = {     'preConds': {'pop': 'INPUT_FILTER_CE'},    'postConds': {'pop': 'INPUTosc_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_EQ'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'INPUT_FILTER_EQ'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_EQ_CE'] = {     'preConds': {'pop': 'INPUT_FILTER_EQ'},    'postConds': {'pop': 'INPUTosc_CE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_EQ_PLUS'] = {     'preConds': {'pop': 'INPUT_FILTER_EQ'},    'postConds': {'pop': 'INPUTosc_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_EQ_MINUS'] = {     'preConds': {'pop': 'INPUT_FILTER_EQ'},    'postConds': {'pop': 'INPUTosc_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_PLUS'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'INPUT_FILTER_PLUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_PLUS_EQ'] = {     'preConds': {'pop': 'INPUT_FILTER_PLUS'},    'postConds': {'pop': 'INPUTosc_EQ'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_PLUS_CE'] = {     'preConds': {'pop': 'INPUT_FILTER_PLUS'},    'postConds': {'pop': 'INPUTosc_CE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_PLUS_MINUS'] = {     'preConds': {'pop': 'INPUT_FILTER_PLUS'},    'postConds': {'pop': 'INPUTosc_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_MINUS'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'INPUT_FILTER_MINUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_MINUSE_EQ'] = {     'preConds': {'pop': 'INPUT_FILTER_MINUS'},    'postConds': {'pop': 'INPUTosc_EQ'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_MINUS_PLUS'] = {     'preConds': {'pop': 'INPUT_FILTER_MINUS'},    'postConds': {'pop': 'INPUTosc_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_MINUS_CE'] = {     'preConds': {'pop': 'INPUT_FILTER_MINUS'},    'postConds': {'pop': 'INPUTosc_CE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 


netParams.connParams['Axon_INPUT2filter_0'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'INPUT_FILTER_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_0_1'] = {     'preConds': {'pop': 'INPUT_FILTER_0'},    'postConds': {'pop': 'INPUTosc_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_0_2'] = {     'preConds': {'pop': 'INPUT_FILTER_0'},    'postConds': {'pop': 'INPUTosc_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_0_3'] = {     'preConds': {'pop': 'INPUT_FILTER_0'},    'postConds': {'pop': 'INPUTosc_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_1'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'INPUT_FILTER_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_1_0'] = {     'preConds': {'pop': 'INPUT_FILTER_1'},    'postConds': {'pop': 'INPUTosc_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_1_2'] = {     'preConds': {'pop': 'INPUT_FILTER_1'},    'postConds': {'pop': 'INPUTosc_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_1_3'] = {     'preConds': {'pop': 'INPUT_FILTER_1'},    'postConds': {'pop': 'INPUTosc_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_2'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'INPUT_FILTER_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_2_1'] = {     'preConds': {'pop': 'INPUT_FILTER_2'},    'postConds': {'pop': 'INPUTosc_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_2_0'] = {     'preConds': {'pop': 'INPUT_FILTER_2'},    'postConds': {'pop': 'INPUTosc_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_2_3'] = {     'preConds': {'pop': 'INPUT_FILTER_2'},    'postConds': {'pop': 'INPUTosc_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_INPUT2filter_3'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'INPUT_FILTER_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_INPUToscfilter_3_1'] = {     'preConds': {'pop': 'INPUT_FILTER_3'},    'postConds': {'pop': 'INPUTosc_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_3_2'] = {     'preConds': {'pop': 'INPUT_FILTER_3'},    'postConds': {'pop': 'INPUTosc_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_INPUToscfilter_3_0'] = {     'preConds': {'pop': 'INPUT_FILTER_3'},    'postConds': {'pop': 'INPUTosc_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 







#    //1.3 DISTRIBUTE INPUTS


#       ///1.3.1 OPERATORS OUTPUT
netParams.connParams['Axon_OUTPUTPLUS1'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'OUTPUT_PLUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUTMINUS1'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'OUTPUT_MINUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 


#       ///1.3.2 CE * 0 1 2 3 > Comp1


#netParams.connParams['Axon_OUTPUT_Component1_01'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_02'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#///RESULT_0 > KILLOTHERSFILTER > inh OUTPUT_Component1_123
#netParams.connParams['Axon_OUTPUT_Component1_11'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_12'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#///RESULT_1 > KILLOTHERSFILTER > inh OUTPUT_Component1_023
#netParams.connParams['Axon_OUTPUT_Component1_21'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_22'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#///RESULT_2 > KILLOTHERSFILTER > inh OUTPUT_Component1_123
#netParams.connParams['Axon_OUTPUT_Component1_31'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_32'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#///RESULT_3 > KILLOTHERSFILTER > inh OUTPUT_Component1_123
netParams.connParams['Axon_OUTPUT_Component1_0a'] = {     'preConds': {'pop': 'OUTPUT_Component1_0'},    'postConds': {'pop': 'OUTPUT_Component1_0osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_1a'] = {     'preConds': {'pop': 'OUTPUT_Component1_1'},    'postConds': {'pop': 'OUTPUT_Component1_1osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_2a'] = {     'preConds': {'pop': 'OUTPUT_Component1_2'},    'postConds': {'pop': 'OUTPUT_Component1_2osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_3a'] = {     'preConds': {'pop': 'OUTPUT_Component1_3'},    'postConds': {'pop': 'OUTPUT_Component1_3osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_OUTPUT_Component1_0b'] = {     'preConds': {'pop': 'OUTPUT_Component1_0osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_1b'] = {     'preConds': {'pop': 'OUTPUT_Component1_1osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_2b'] = {     'preConds': {'pop': 'OUTPUT_Component1_2osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_3b'] = {     'preConds': {'pop': 'OUTPUT_Component1_3osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_OUTPUT_Component1_0c'] = {     'preConds': {'pop': 'OUTPUT_Component1_0osc'},    'postConds': {'pop': 'OUTPUT_Component1_0osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_1c'] = {     'preConds': {'pop': 'OUTPUT_Component1_1osc'},    'postConds': {'pop': 'OUTPUT_Component1_1osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_2c'] = {     'preConds': {'pop': 'OUTPUT_Component1_2osc'},    'postConds': {'pop': 'OUTPUT_Component1_2osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_3c'] = {     'preConds': {'pop': 'OUTPUT_Component1_3osc'},    'postConds': {'pop': 'OUTPUT_Component1_3osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 

netParams.connParams['Axon_OUTPUT_Component1_0d'] = {     'preConds': {'pop': 'OUTPUT_Component1_0osc2'},    'postConds': {'pop': 'OUTPUT_Component1_0osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_1d'] = {     'preConds': {'pop': 'OUTPUT_Component1_1osc2'},    'postConds': {'pop': 'OUTPUT_Component1_1osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_2d'] = {     'preConds': {'pop': 'OUTPUT_Component1_2osc2'},    'postConds': {'pop': 'OUTPUT_Component1_2osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_3d'] = {     'preConds': {'pop': 'OUTPUT_Component1_3osc2'},    'postConds': {'pop': 'OUTPUT_Component1_3osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 




netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0b'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0c'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_0f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1b'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1c'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1d'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_1f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2b'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2c'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2e'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_2f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3b'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3c'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_0FWDfilter_3f'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
"""
Axon_OUTPUT_Component1_0FWDfilter1:{start_node:"INPUTosc_CE", end_node:"FILTER_OUTPUT_Component1_0_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_0FWDfilter2:{start_node:"INPUTosc_0", end_node:"FILTER_OUTPUT_Component1_0_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_0FWDfilter3:{start_node:"FILTER_OUTPUT_Component1_0_A", end_node:"OUTPUT_Component1_0", shape:["default"], type:"GABA", lengthsec:4,power:-10},
Axon_OUTPUT_Component1_1FWDfilter1:{start_node:"INPUTosc_CE", end_node:"FILTER_OUTPUT_Component1_1_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_1FWDfilter2:{start_node:"INPUTosc_1", end_node:"FILTER_OUTPUT_Component1_1_A", shape:["default"], type:"glutamate", lengthsec:4,power:10},
Axon_OUTPUT_Component1_1FWDfilter3:{start_node:"FILTER_OUTPUT_Component1_1_A", end_node:"OUTPUT_Component1_1", shape:["default"], type:"GABA", lengthsec:5,power:-10},
Axon_OUTPUT_Component1_2FWDfilter1:{start_node:"INPUTosc_CE", end_node:"FILTER_OUTPUT_Component1_2_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_2FWDfilter2:{start_node:"INPUTosc_2", end_node:"FILTER_OUTPUT_Component1_2_A", shape:["default"], type:"glutamate", lengthsec:4,power:10},
Axon_OUTPUT_Component1_2FWDfilter3:{start_node:"FILTER_OUTPUT_Component1_2_A", end_node:"OUTPUT_Component1_2", shape:["default"], type:"GABA", lengthsec:5,power:-10},
Axon_OUTPUT_Component1_3FWDfilter1:{start_node:"INPUTosc_CE", end_node:"FILTER_OUTPUT_Component1_3_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_3FWDfilter2:{start_node:"INPUTosc_3", end_node:"FILTER_OUTPUT_Component1_3_A", shape:["default"], type:"glutamate", lengthsec:5,power:10},
Axon_OUTPUT_Component1_3FWDfilter3:{start_node:"FILTER_OUTPUT_Component1_3_A", end_node:"OUTPUT_Component1_3", shape:["default"], type:"GABA", lengthsec:4,power:-10},
"""


#       ///1.3.3 + - * 0 1 2 3 Comp2




netParams.connParams['Axon_OUTPUT_Component2_02'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_12'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_22'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_32'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 





netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_0a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_0b'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_0d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_0e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_0f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_1a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_1b'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_1d'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_1e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_1f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_2a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_2b'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_2d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_2e'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_2f'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_3a'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_3b'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_3d'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_3e'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0FWDfilter_3f'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 






"""

netParams.connParams['Axon_OUTPUT_Component2p_01'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'MidOutput_Component2p_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_03'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'MidOutput_Component2p_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_02'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'MidOutput_Component2m_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_03'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'MidOutput_Component2m_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_01'] = {     'preConds': {'pop': 'MidOutput_Component2m_0'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_02'] = {     'preConds': {'pop': 'MidOutput_Component2p_0'},    'postConds': {'pop': 'OUTPUT_Component2_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_11'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'MidOutput_Component2p_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_13'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'MidOutput_Component2p_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_12'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'MidOutput_Component2m_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_13'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'MidOutput_Component2m_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_11'] = {     'preConds': {'pop': 'MidOutput_Component2m_1'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_12'] = {     'preConds': {'pop': 'MidOutput_Component2p_1'},    'postConds': {'pop': 'OUTPUT_Component2_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_21'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'MidOutput_Component2p_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_23'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'MidOutput_Component2p_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_22'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'MidOutput_Component2m_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_23'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'MidOutput_Component2m_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_21'] = {     'preConds': {'pop': 'MidOutput_Component2m_2'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_22'] = {     'preConds': {'pop': 'MidOutput_Component2p_2'},    'postConds': {'pop': 'OUTPUT_Component2_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_31'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'MidOutput_Component2p_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2p_33'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'MidOutput_Component2p_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_32'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'MidOutput_Component2m_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2m_33'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'MidOutput_Component2m_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_31'] = {     'preConds': {'pop': 'MidOutput_Component2m_3'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_32'] = {     'preConds': {'pop': 'MidOutput_Component2p_3'},    'postConds': {'pop': 'OUTPUT_Component2_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#///filter
netParams.connParams['Axon_OUTPUT_Component2_0pFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_0_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_0pFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_0_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_0pFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2p_0_A'},    'postConds': {'pop': 'MidOutput_Component2p_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_0mFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_0_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component2_0mFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_0'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_0_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'esc'} 
netParams.connParams['Axon_OUTPUT_Component2_0mFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2m_0_A'},    'postConds': {'pop': 'MidOutput_Component2m_0'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_1pFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_1_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_1pFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_1_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_1pFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2p_1_A'},    'postConds': {'pop': 'MidOutput_Component2p_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_1mFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_1_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_1mFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_1'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_1_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_1mFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2m_1_A'},    'postConds': {'pop': 'MidOutput_Component2m_1'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_2pFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_2_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_2pFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_2_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_2pFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2p_2_A'},    'postConds': {'pop': 'MidOutput_Component2p_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_2mFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_2_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_2mFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_2'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_2_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_2mFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2m_2_A'},    'postConds': {'pop': 'MidOutput_Component2m_2'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_OUTPUT_Component2_3pFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_3_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_3pFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2p_3_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_3pFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2p_3_A'},    'postConds': {'pop': 'MidOutput_Component2p_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_3mFWDfilter1'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_3_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_3mFWDfilter2'] = {     'preConds': {'pop': 'INPUTosc_3'},    'postConds': {'pop': 'FILTER_OUTPUT_Component2m_3_A'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component2_3mFWDfilter3'] = {     'preConds': {'pop': 'FILTER_OUTPUT_Component2m_3_A'},    'postConds': {'pop': 'MidOutput_Component2m_3'},    'probability': exc_probability1,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'inh'} 





"""







netParams.connParams['Axon_Transaction_CORE00'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 


netParams.connParams['Axon_Transaction_CORE0b'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE0c'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE0d'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  

netParams.connParams['Axon_Transaction_CORE0e'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0f'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0g'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0h'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0i'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE0ee'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0ff'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0gg'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0hh'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE0ii'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

"""

netParams.connParams['Axon_Transaction_CORE10'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#INPUT2_0,1,2,3 > TRANSACTION_NEURON_ONLY_VALUE_killer inh
#TRANSACTION_NEURON_EMPTY > TRANSACTION_NEURON_ONLY_VALUE_killer exc
#TRANSACTION_NEURON_ONLY_VALUE_killer > TRANSACTION_ONLY_VALUE inh
netParams.connParams['Axon_Transaction_CORE11'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE12'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE13'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE14'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE15'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': 1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE16'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 1,    'synMech': 'inh'}

netParams.connParams['Axon_Transaction_CORE1b'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE1c'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE1d'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  

netParams.connParams['Axon_Transaction_CORE1e'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1f'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1g'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1h'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1i'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE1ee'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1ff'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1gg'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1hh'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1ii'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

"""




netParams.connParams['Axon_Transaction_CORE10'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#INPUT2_0,1,2,3 > TRANSACTION_NEURON_ONLY_VALUE_killer inh
#TRANSACTION_NEURON_EMPTY > TRANSACTION_NEURON_ONLY_VALUE_killer exc
#TRANSACTION_NEURON_ONLY_VALUE_killer > TRANSACTION_ONLY_VALUE inh
#netParams.connParams['Axon_Transaction_CORE11'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE12'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE13'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE14'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE15'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': 1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE16'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_killer'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 1,    'synMech': 'inh'}

netParams.connParams['Axon_Transaction_CORE1b'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE1c'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE1d'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  

netParams.connParams['Axon_Transaction_CORE1e'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1f'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1g'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1h'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1i'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE1ee'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1ff'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1gg'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1hh'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE1ii'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}








netParams.connParams['Axon_Transaction_CORE20'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
#INPUT2_0,1,2,3 > TRANSACTION_NEURON_ONLY_VALUE_killer inh
#TRANSACTION_NEURON_EMPTY > TRANSACTION_NEURON_ONLY_VALUE_killer exc
#TRANSACTION_NEURON_ONLY_VALUE_killer > TRANSACTION_ONLY_VALUE inh
netParams.connParams['Axon_Transaction_CORE21'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE22'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE23'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE24'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE25'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': 1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE26'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_killer'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 1,    'synMech': 'inh'}

netParams.connParams['Axon_Transaction_CORE27'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_CORE2b'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE2c'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE2d'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  

netParams.connParams['Axon_Transaction_CORE2e'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2f'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2g'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2h'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2i'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE2ee'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2ff'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2gg'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2hh'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2ii'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}






netParams.connParams['Axon_aTransaction_CORE27'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_aTransaction_CORE28'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_aTransaction_CORE29'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_aTransaction_CORE30'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_startTransaction_PLUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_MINUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
#+10 to block phase
netParams.connParams['Axon_10startTransaction_PLUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_MINUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component1_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component1_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component1_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component1_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component2_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component2_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component2_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_10startTransaction_Component2_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 10+exc_delay1,    'synMech': 'inh'} 
#+20 to block phase
netParams.connParams['Axon_20startTransaction_PLUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_MINUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component1_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component1_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component1_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component1_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component2_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component2_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component2_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_20startTransaction_Component2_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': 20+exc_delay1,    'synMech': 'inh'} 





#SUMM_MERGE > STC
netParams.connParams['Axon_astartTransaction_PLUS'] = {     'preConds': {'pop': 'OUTPUT_PLUS'},    'postConds': {'pop': 'START_TRANSACTION_PLUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_MINUS'] = {     'preConds': {'pop': 'OUTPUT_MINUS'},    'postConds': {'pop': 'START_TRANSACTION_MINUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component1_0'] = {     'preConds': {'pop': 'MERGE_SUMM_Component1_0'},    'postConds': {'pop': 'START_TRANSACTION_Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component1_1'] = {     'preConds': {'pop': 'MERGE_SUMM_Component1_1'},    'postConds': {'pop': 'START_TRANSACTION_Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component1_2'] = {     'preConds': {'pop': 'MERGE_SUMM_Component1_2'},    'postConds': {'pop': 'START_TRANSACTION_Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component1_3'] = {     'preConds': {'pop': 'MERGE_SUMM_Component1_3'},    'postConds': {'pop': 'START_TRANSACTION_Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component2_0'] = {     'preConds': {'pop': 'OUTPUT_Component2_0'},    'postConds': {'pop': 'START_TRANSACTION_Component2_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component2_1'] = {     'preConds': {'pop': 'OUTPUT_Component2_1'},    'postConds': {'pop': 'START_TRANSACTION_Component2_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component2_2'] = {     'preConds': {'pop': 'OUTPUT_Component2_2'},    'postConds': {'pop': 'START_TRANSACTION_Component2_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_astartTransaction_Component2_3'] = {     'preConds': {'pop': 'OUTPUT_Component2_3'},    'postConds': {'pop': 'START_TRANSACTION_Component2_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 





exc_delay7=50

#STC > 'FINISH_TRANSACTION'
netParams.connParams['Axon_bstartTransaction_PLUS'] = {     'preConds': {'pop': 'START_TRANSACTION_PLUS'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_MINUS'] = {     'preConds': {'pop': 'START_TRANSACTION_MINUS'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component1_0'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_0'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component1_1'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_1'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component1_2'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_2'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component1_3'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_3'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component2_0'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_0'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component2_1'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_1'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component2_2'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_2'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'} 
netParams.connParams['Axon_bstartTransaction_Component2_3'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_3'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay7,    'synMech': 'exc'}  



#FT > EMPTY
netParams.connParams['Axon_bTransaction_CORE27'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_bTransaction_CORE28'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_bTransaction_CORE29'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}  
netParams.connParams['Axon_bTransaction_CORE30'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_bbTransaction_CORE27'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_bbTransaction_CORE28'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_bbTransaction_CORE29'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}  
netParams.connParams['Axon_bbTransaction_CORE30'] = {     'preConds': {'pop': 'FINISH_TRANSACTION'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 




#STC > CALCULATOR !!!
netParams.connParams['Axon_cstartTransaction_PLUS'] = {     'preConds': {'pop': 'START_TRANSACTION_PLUS'},    'postConds': {'pop': 'Operator_PLUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_MINUS'] = {     'preConds': {'pop': 'START_TRANSACTION_MINUS'},    'postConds': {'pop': 'Operator_MINUS'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_0'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_0'},    'postConds': {'pop': 'Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_1'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_1'},    'postConds': {'pop': 'Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_2'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_2'},    'postConds': {'pop': 'Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_3'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_3'},    'postConds': {'pop': 'Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_0'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_0'},    'postConds': {'pop': 'Component2_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_1'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_1'},    'postConds': {'pop': 'Component2_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_2'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_2'},    'postConds': {'pop': 'Component2_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_3'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_3'},    'postConds': {'pop': 'Component2_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}  

#Calculator Oscilator
netParams.connParams['Axon_cstartTransaction_PLUSosc'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Operator_PLUSosc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_MINUSosc'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Operator_MINUSosc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_0osc'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Component1_0osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_1osc'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Component1_1osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_2osc'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Component1_2osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_3osc'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Component1_3osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_0osc'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Component2_0osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_1osc'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Component2_1osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  
netParams.connParams['Axon_cstartTransaction_Component2_2osc'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Component2_2osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  
netParams.connParams['Axon_cstartTransaction_Component2_3osc'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Component2_3osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 

netParams.connParams['Axon_cstartTransaction_PLUSosc2'] = {     'preConds': {'pop': 'Operator_PLUSosc'},    'postConds': {'pop': 'Operator_PLUS'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_MINUSosc2'] = {     'preConds': {'pop': 'Operator_MINUSosc'},    'postConds': {'pop': 'Operator_MINUS'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_0osc2'] = {     'preConds': {'pop': 'Component1_0osc'},    'postConds': {'pop': 'Component1_0'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_1osc2'] = {     'preConds': {'pop': 'Component1_1osc'},    'postConds': {'pop': 'Component1_1'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_2osc2'] = {     'preConds': {'pop': 'Component1_2osc'},    'postConds': {'pop': 'Component1_2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component1_3osc2'] = {     'preConds': {'pop': 'Component1_3osc'},    'postConds': {'pop': 'Component1_3'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_0osc2'] = {     'preConds': {'pop': 'Component2_0osc'},    'postConds': {'pop': 'Component2_0'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  
netParams.connParams['Axon_cstartTransaction_Component2_1osc2'] = {     'preConds': {'pop': 'Component2_1osc'},    'postConds': {'pop': 'Component2_1'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_2osc2'] = {     'preConds': {'pop': 'Component2_2osc'},    'postConds': {'pop': 'Component2_2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_Component2_3osc2'] = {     'preConds': {'pop': 'Component2_3osc'},    'postConds': {'pop': 'Component2_3'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 


#STC > Calculator - kill filter
netParams.connParams['Axon_cstartTransaction_KILL1'] = {     'preConds': {'pop': 'START_TRANSACTION_PLUS'},    'postConds': {'pop': 'Operator_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
#netParams.connParams['Axon_cstartTransaction_KILL2'] = {     'preConds': {'pop': 'START_TRANSACTION_PLUS'},    'postConds': {'pop': 'Operator_MINUSosc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL3'] = {     'preConds': {'pop': 'START_TRANSACTION_MINUS'},    'postConds': {'pop': 'Operator_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
#netParams.connParams['Axon_cstartTransaction_KILL4'] = {     'preConds': {'pop': 'START_TRANSACTION_MINUS'},    'postConds': {'pop': 'Operator_PLUSosc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

netParams.connParams['Axon_cstartTransaction_KILL5'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_0'},    'postConds': {'pop': 'Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL6'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_0'},    'postConds': {'pop': 'Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL7'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_0'},    'postConds': {'pop': 'Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL8'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_1'},    'postConds': {'pop': 'Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL9'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_1'},    'postConds': {'pop': 'Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL10'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_1'},    'postConds': {'pop': 'Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL11'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_2'},    'postConds': {'pop': 'Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL12'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_2'},    'postConds': {'pop': 'Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL13'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_2'},    'postConds': {'pop': 'Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL14'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_3'},    'postConds': {'pop': 'Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL15'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_3'},    'postConds': {'pop': 'Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL16'] = {     'preConds': {'pop': 'START_TRANSACTION_Component1_3'},    'postConds': {'pop': 'Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

netParams.connParams['Axon_cstartTransaction_KILL17'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_0'},    'postConds': {'pop': 'Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL18'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_0'},    'postConds': {'pop': 'Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL19'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_0'},    'postConds': {'pop': 'Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL20'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_1'},    'postConds': {'pop': 'Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL21'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_1'},    'postConds': {'pop': 'Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL22'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_1'},    'postConds': {'pop': 'Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL23'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_2'},    'postConds': {'pop': 'Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL24'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_2'},    'postConds': {'pop': 'Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL25'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_2'},    'postConds': {'pop': 'Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL26'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_3'},    'postConds': {'pop': 'Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL27'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_3'},    'postConds': {'pop': 'Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_KILL28'] = {     'preConds': {'pop': 'START_TRANSACTION_Component2_3'},    'postConds': {'pop': 'Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

"""

netParams.connParams['Axon_Transaction_CORE20'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 


netParams.connParams['Axon_Transaction_CORE00'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE10'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

#INPUT2_0,1,2,3 > TRANSACTION_NEURON_ONLY_VALUE_killer inh
#TRANSACTION_NEURON_EMPTY > TRANSACTION_NEURON_ONLY_VALUE_killer exc
#TRANSACTION_NEURON_ONLY_VALUE_killer > TRANSACTION_ONLY_VALUE inh

netParams.connParams['Axon_Transaction_CORE11'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE12'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE13'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE14'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_Transaction_CORE15'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY_osc'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_CORE16'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_killer'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}






netParams.connParams['Axon_Transaction_CORE2b'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_ONLY_OPERATOR_osc'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE2c'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR_osc'},    'postConds': {'pop': 'TRANSACTION_ONLY_OPERATOR_osc2'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE2d'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR_osc2'},    'postConds': {'pop': 'TRANSACTION_ONLY_OPERATOR_osc'},    'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}  
netParams.connParams['Axon_Transaction_CORE2e'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_EMPTY_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2f'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2g'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2h'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_CORE2i'] = {     'preConds': {'pop': 'TRANSACTION_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

"""

"""


"""
#////NO GPI > Output inh
#//NO will loop Output > Operator_PLUS,MINUS,0123 inh
# Output > TN_EMPTY exc
exc_delay8 = 1
exc_delay9 = 50

"""
netParams.connParams['Axon_fbstartTransaction_PLUSa'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_MINUSb'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_Component1_0c'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_Component1_1d'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
"""

netParams.connParams['Axon_fbstartTransaction_PLUSa'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'Output_0123'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_MINUSb'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'Output_0123'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_Component1_0c'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'Output_0123'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 
netParams.connParams['Axon_fbstartTransaction_Component1_1d'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'Output_0123'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 

"""
netParams.connParams['Axon_fbstartTransaction_PLUSa2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'FINISH_TRANSACTION'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay8,    'synMech': 'exc'} 




#block input loop
netParams.connParams['Axon_cstartTransaction_PLUSosca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Operator_PLUSosc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_MINUSosca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Operator_MINUSosc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_Component1_0osca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component1_0osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_Component1_1osca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component1_1osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_Component1_2osca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component1_2osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_Component1_3osca2'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component1_3osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_Component2_0osca3'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component2_0osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_Component2_1osca3'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component2_1osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_Component2_2osca3'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component2_2osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_cstartTransaction_Component2_3osca3'] = {     'preConds': {'pop': 'Output_0123'},    'postConds': {'pop': 'Component2_3osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
"""

#IF TRANSACTION STARTED > inh Output_osc (once not loop)

netParams.connParams['Axon_clear_calculator_output_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'Output_0osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_clear_calculator_output_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'Output_1osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_clear_calculator_output_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'Output_2osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_clear_calculator_output_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'Output_3osc'},     'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}


netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER1'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'Output_1osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER2'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'Output_2osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER3'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'Output_3osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER4'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'Output_0osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER5'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'Output_2osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER6'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'Output_3osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER7'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'Output_1osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER8'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'Output_0osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER9'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'Output_3osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER10'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'Output_1osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER11'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'Output_2osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0uKILLER12'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'Output_0osc'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}


#Output > OutputOSC
netParams.connParams['Axon_cstartTransaction_PLUSosc2R0e'] = {     'preConds': {'pop': 'Output_0'},    'postConds': {'pop': 'Output_0osc'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2R1f'] = {     'preConds': {'pop': 'Output_1'},    'postConds': {'pop': 'Output_1osc'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2R2g'] = {     'preConds': {'pop': 'Output_2'},    'postConds': {'pop': 'Output_2osc'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R3h'] = {     'preConds': {'pop': 'Output_3'},    'postConds': {'pop': 'Output_3osc'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['Axon_cstartTransaction_PLUSosc2R0i'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'Output_0osc2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R1j'] = {     'preConds': {'pop': 'Output_1osc'},    'postConds': {'pop': 'Output_1osc2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R2k'] = {     'preConds': {'pop': 'Output_2osc'},    'postConds': {'pop': 'Output_2osc2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R3l'] = {     'preConds': {'pop': 'Output_30sc'},    'postConds': {'pop': 'Output_3osc2'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 

netParams.connParams['Axon_cstartTransaction_PLUSosc2R0m'] = {     'preConds': {'pop': 'Output_0osc2'},    'postConds': {'pop': 'Output_0osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R1n'] = {     'preConds': {'pop': 'Output_1osc2'},    'postConds': {'pop': 'Output_1osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R2o'] = {     'preConds': {'pop': 'Output_2osc2'},    'postConds': {'pop': 'Output_2osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R3p'] = {     'preConds': {'pop': 'Output_30sc2'},    'postConds': {'pop': 'Output_3osc'},     'probability': exc_probability5,    'weight': exc_weight,    'delay': exc_delayosc1,    'synMech': 'exc'}

#OutputOSC > SUMM_MERGE


netParams.connParams['Axon_cstartTransaction_PLUSosc2R0q'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay9,    'synMech': 'exc'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2R1r'] = {     'preConds': {'pop': 'Output_1osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay9,    'synMech': 'exc'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2R2s'] = {     'preConds': {'pop': 'Output_2osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay9,    'synMech': 'exc'} 
netParams.connParams['Axon_cstartTransaction_PLUSosc2R3t'] = {     'preConds': {'pop': 'Output_30sc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay9,    'synMech': 'exc'} 

netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL0u'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL1v'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL2w'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL3x'] = {     'preConds': {'pop': 'Output_1osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL4y'] = {     'preConds': {'pop': 'Output_1osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL5z'] = {     'preConds': {'pop': 'Output_1osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL6aa'] = {     'preConds': {'pop': 'Output_2osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL7ab'] = {     'preConds': {'pop': 'Output_2osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL8ac'] = {     'preConds': {'pop': 'Output_2osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL9ad'] = {     'preConds': {'pop': 'Output_3osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL10ae'] = {     'preConds': {'pop': 'Output_3osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}
netParams.connParams['Axon_cstartTransaction_PLUSosc2RKILL11af'] = {     'preConds': {'pop': 'Output_3osc'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay9,    'synMech': 'inh'}



"""



#///STEP 2 A = TRANSACTION_NEURON_EMPTY, T_N_ONLYVALUE, T_N_ONLYOPERATOR, T_N_COMPLETE)



netParams.connParams['Axon_Transaction_CORE0'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_CORE1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE2'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE3'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE4'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE5'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_FILTER1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER2'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER3'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER4'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER5'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER6'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_Transaction_FILTER7'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER8'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER8'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}



netParams.connParams['Axon_Transaction_CORE6'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE7'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE8'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE9'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE10'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_FILTER11'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER12'] = {     'preConds': {'pop': 'INPUT2_CE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER13'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER14'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER15'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER16'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE_FILTER'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_Transaction_FILTER17'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER18'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER18a'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'}

netParams.connParams['Axon_Transaction_CORE11'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE13'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE14'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE15'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_FILTER21'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER22'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER23'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER24'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER25'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER26'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV_FILTER'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 



netParams.connParams['Axon_Transaction_CORE16'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE17'] = {     'preConds': {'pop': 'INPUT2_0'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE18'] = {     'preConds': {'pop': 'INPUT2_1'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE19'] = {     'preConds': {'pop': 'INPUT2_2'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE20'] = {     'preConds': {'pop': 'INPUT2_3'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_FILTER31'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER33'] = {     'preConds': {'pop': 'INPUT2_EQ'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER34'] = {     'preConds': {'pop': 'INPUT2_PLUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER35'] = {     'preConds': {'pop': 'INPUT2_MINUS'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_FILTER'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_FILTER36'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO_FILTER'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 


netParams.connParams['Axon_Transaction_CORE21'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEO'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE22'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETEV'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 

netParams.connParams['Axon_Transaction_FILTER47'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER48'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_Transaction_FILTER49'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_Transaction_CORE23'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_EMPTY", shape:["loop"], type:"glutamate", lengthsec:1,power:10},
netParams.connParams['Axon_Transaction_CORE24'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE", shape:["loop"], type:"glutamate", lengthsec:1,power:10},
netParams.connParams['Axon_Transaction_CORE25'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR", shape:["loop"], type:"glutamate", lengthsec:1,power:10},
netParams.connParams['Axon_Transaction_CORE26'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE", shape:["loop"], type:"glutamate", lengthsec:1,power:10},

netParams.connParams['Axon_Transaction_CORE27'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_EMPTY'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE28'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_VALUE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE29'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_ONLY_OPERATOR'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_Transaction_CORE30'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE'},    'postConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['Axon_startTransaction_PLUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_PLUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_MINUS'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_MINUS'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component1_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_0'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_1'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_2'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_startTransaction_Component2_3'] = {     'preConds': {'pop': 'TRANSACTION_NEURON_COMPLETE_GPI'},    'postConds': {'pop': 'START_TRANSACTION_Component2_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 










netParams.connParams['Axon_OUTPUT_Component1_03'] = {     'preConds': {'pop': 'RESULTosc_0'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_03fa'] = {     'preConds': {'pop': 'RESULTosc_0'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_03fb'] = {     'preConds': {'pop': 'RESULTosc_0'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_03fc'] = {     'preConds': {'pop': 'RESULTosc_0'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
#///RESULT_0 > KILLOTHERSFILTER > inh OUTPUT_Component1_123
netParams.connParams['Axon_OUTPUT_Component1_13'] = {     'preConds': {'pop': 'RESULTosc_1'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_13fa'] = {     'preConds': {'pop': 'RESULTosc_1'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_13fb'] = {     'preConds': {'pop': 'RESULTosc_1'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_13fc'] = {     'preConds': {'pop': 'RESULTosc_1'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
#///RESULT_1 > KILLOTHERSFILTER > inh OUTPUT_Component1_023
netParams.connParams['Axon_OUTPUT_Component1_23'] = {     'preConds': {'pop': 'RESULTosc_2'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_23fa'] = {     'preConds': {'pop': 'RESULTosc_2'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_23fb'] = {     'preConds': {'pop': 'RESULTosc_2'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_23fc'] = {     'preConds': {'pop': 'RESULTosc_2'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
#///RESULT_2 > KILLOTHERSFILTER > inh OUTPUT_Component1_123
netParams.connParams['Axon_OUTPUT_Component1_33'] = {     'preConds': {'pop': 'RESULTosc_3'},    'postConds': {'pop': 'MERGE_SUMM_Component1_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['Axon_OUTPUT_Component1_33fa'] = {     'preConds': {'pop': 'RESULTosc_3'},    'postConds': {'pop': 'MERGE_SUMM_Component1_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_33fb'] = {     'preConds': {'pop': 'RESULTosc_3'},    'postConds': {'pop': 'MERGE_SUMM_Component1_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['Axon_OUTPUT_Component1_33fc'] = {     'preConds': {'pop': 'RESULTosc_3'},    'postConds': {'pop': 'MERGE_SUMM_Component1_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
#///RESULT_3 > KILLOTHERSFILTER > inh OUTPUT_Component1_123






"""


#///STEP 2 = OPERATOR+VALUE > OUTPUT. AFTER VALUE INPUT if OPERATOR & VALUE start TRANSACTION TO OUTPUT (neuron that detects both value+operator were input. after transaction delete. TRANSACTION_NEURON_EMPTY, T_N_ONLYVALUE, T_N_ONLYOPERATOR, T_N_COMPLETE)
#///FEEDBACK FILTER FOR 1 PLUS/MINUS 2 Comp_1 3 Comp_2





netParams.connParams['TR0'] = {     'preConds': {'pop': 'INPUTosc_EQ'},    'postConds': {'pop': 'TOTAL_RESULT_GPI'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['TR1'] = {     'preConds': {'pop': 'INPUTosc_CE'},    'postConds': {'pop': 'TOTAL_RESULT_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['TR2'] = {     'preConds': {'pop': 'INPUTosc_PLUS'},    'postConds': {'pop': 'TOTAL_RESULT_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['TR3'] = {     'preConds': {'pop': 'INPUTosc_MINUS'},    'postConds': {'pop': 'TOTAL_RESULT_GPI'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['TR4'] = {     'preConds': {'pop': 'TOTAL_RESULT_GPI'},    'postConds': {'pop': 'TOTAL_RESULT_0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['TR5'] = {     'preConds': {'pop': 'TOTAL_RESULT_GPI'},    'postConds': {'pop': 'TOTAL_RESULT_1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['TR6'] = {     'preConds': {'pop': 'TOTAL_RESULT_GPI'},    'postConds': {'pop': 'TOTAL_RESULT_2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 
netParams.connParams['TR7'] = {     'preConds': {'pop': 'TOTAL_RESULT_GPI'},    'postConds': {'pop': 'TOTAL_RESULT_3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': exc_delay1,    'synMech': 'inh'} 

netParams.connParams['TR8'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'TOTAL_RESULT_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['TR9'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'TOTAL_RESULT_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['TRa'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'TOTAL_RESULT_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['TRb'] = {     'preConds': {'pop': 'Output_0osc'},    'postConds': {'pop': 'TOTAL_RESULT_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}







#exc_weight = 0.9
#exc_weight2 = 0.9
#exc_weight3 = 0.9

exc_delay1 = 3
exc_delay2 = 4
exc_delay3 = 5

exc_probability1 = 0.1
exc_probability2 = 0.1
exc_probability3 = 0.1







#CALCULATION


netParams.connParams['1_0+0'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_0+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0+0'] = {    'preConds': {'pop': 'Output_0PLUS0'},    'postConds': {'pop': 'Output_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0+1'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0+1'] = {    'preConds': {'pop': 'Output_0PLUS1'},    'postConds': {'pop': 'Output_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0+2'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['PLUS_0+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0+2'] = {    'preConds': {'pop': 'Output_0PLUS2'},    'postConds': {'pop': 'Output_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0+3'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_0+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_0PLUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0+3'] = {    'preConds': {'pop': 'Output_0PLUS3'},    'postConds': {'pop': 'Output_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_1+0'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1+0'] = {    'preConds': {'pop': 'Output_1PLUS0'},    'postConds': {'pop': 'Output_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1+1'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['PLUS_1+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1+1'] = {    'preConds': {'pop': 'Output_1PLUS1'},    'postConds': {'pop': 'Output_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1+2'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_1+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1+2'] = {    'preConds': {'pop': 'Output_1PLUS2'},    'postConds': {'pop': 'Output_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1+3'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_1+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_1PLUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1+3'] = {    'preConds': {'pop': 'Output_1PLUS3'},    'postConds': {'pop': 'Output_4'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_2+0'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_2+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2+0'] = {    'preConds': {'pop': 'Output_2PLUS0'},    'postConds': {'pop': 'Output_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2+1'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_2+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2+1'] = {    'preConds': {'pop': 'Output_2PLUS1'},    'postConds': {'pop': 'Output_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2+2'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['PLUS_2+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2+2'] = {    'preConds': {'pop': 'Output_2PLUS2'},    'postConds': {'pop': 'Output_4'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2+3'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_2+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_2PLUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2+3'] = {    'preConds': {'pop': 'Output_2PLUS3'},    'postConds': {'pop': 'Output_5'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_3+0'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3+0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_3+0'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['3+0'] = {    'preConds': {'pop': 'Output_3PLUS0'},    'postConds': {'pop': 'Output_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3+1'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3+1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_3+1'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['3+1'] = {    'preConds': {'pop': 'Output_3PLUS1'},    'postConds': {'pop': 'Output_4'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3+2'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3+2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_3+2'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['3+2'] = {    'preConds': {'pop': 'Output_3PLUS2'},    'postConds': {'pop': 'Output_5'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3+3'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3+3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['PLUS_3+3'] = {     'preConds': {'pop': 'Operator_PLUS'},     'postConds': {'pop': 'Output_3PLUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['3+3'] = {    'preConds': {'pop': 'Output_3PLUS3'},    'postConds': {'pop': 'Output_6'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}



netParams.connParams['1_0-0'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_0-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0-0'] = {    'preConds': {'pop': 'Output_0MINUS0'},    'postConds': {'pop': 'Output_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0-1'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_0-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['MINUS_0-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['0-1'] = {    'preConds': {'pop': 'Output_0MINUS1'},    'postConds': {'pop': 'Output_-1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0-2'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_0-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['0-2'] = {    'preConds': {'pop': 'Output_0MINUS2'},    'postConds': {'pop': 'Output_-2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_0-3'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_0-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_0-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_0MINUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['0-3'] = {    'preConds': {'pop': 'Output_0MINUS3'},    'postConds': {'pop': 'Output_-3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_1-0'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1-0'] = {    'preConds': {'pop': 'Output_1MINUS0'},    'postConds': {'pop': 'Output_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1-1'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_1-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1-1'] = {    'preConds': {'pop': 'Output_1MINUS1'},    'postConds': {'pop': 'Output_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1-2'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['MINUS_1-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['1-2'] = {    'preConds': {'pop': 'Output_1MINUS2'},    'postConds': {'pop': 'Output_-1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_1-3'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_1-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_1-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_1MINUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['1-3'] = {    'preConds': {'pop': 'Output_1MINUS3'},    'postConds': {'pop': 'Output_-2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_2-0'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2-0'] = {    'preConds': {'pop': 'Output_2MINUS0'},    'postConds': {'pop': 'Output_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2-1'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_2-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2-1'] = {    'preConds': {'pop': 'Output_2MINUS1'},    'postConds': {'pop': 'Output_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2-2'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_2-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_2-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2-2'] = {    'preConds': {'pop': 'Output_2MINUS2'},    'postConds': {'pop': 'Output_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_2-3'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_2-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['MINUS_2-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_2MINUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2-3'] = {    'preConds': {'pop': 'Output_2MINUS3'},    'postConds': {'pop': 'Output_-1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}


netParams.connParams['1_3-0'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3-0'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_3-0'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS0'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['3-0'] = {    'preConds': {'pop': 'Output_3MINUS0'},    'postConds': {'pop': 'Output_3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3-1'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3-1'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_3-1'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS1'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['3-1'] = {    'preConds': {'pop': 'Output_3MINUS1'},    'postConds': {'pop': 'Output_2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3-2'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'} 
netParams.connParams['2_3-2'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_3-2'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS2'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['3-2'] = {    'preConds': {'pop': 'Output_3MINUS2'},    'postConds': {'pop': 'Output_1'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}

netParams.connParams['1_3-3'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['2_3-3'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['MINUS_3-3'] = {     'preConds': {'pop': 'Operator_MINUS'},     'postConds': {'pop': 'Output_3MINUS3'},     'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}
netParams.connParams['3-3'] = {    'preConds': {'pop': 'Output_3MINUS3'},    'postConds': {'pop': 'Output_0'},    'probability': exc_probability4,    'weight': exc_weight,    'delay': exc_delay1,    'synMech': 'exc'}












inh_delay = 2
inh_delay2 = 2
inh_delay3 = 2

#inh_weight = 5.9









netParams.connParams['AxonComponent10_1p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3p0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3p1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3p2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3p3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent10_1m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_1m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_2m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3m0a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3m1a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3m2a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent10_3m3a'] = {     'preConds': {'pop': 'Component1_0'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 




netParams.connParams['AxonComponent11_0p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3p0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3p1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3p2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3p3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent11_0m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_0m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_2m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3m0a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3m1a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3m2a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent11_3m3a'] = {     'preConds': {'pop': 'Component1_1'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 



netParams.connParams['AxonComponent12_1p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3p0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3p1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3p2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3p3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent12_1m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_1m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_0m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3m0a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3m1a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3m2a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent12_3m3a'] = {     'preConds': {'pop': 'Component1_2'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 



netParams.connParams['AxonComponent13_1p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0p0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0p1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0p2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0p3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent13_1m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_1m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_2m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0m0a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0m1a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0m2a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent13_0m3a'] = {     'preConds': {'pop': 'Component1_3'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 







netParams.connParams['AxonComponent20_0p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_0p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_0p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3p1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3p2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3p3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent20_0m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_0m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_0m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_1m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_2m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3m1a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3m2a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent20_3m3a'] = {     'preConds': {'pop': 'Component2_0'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 



netParams.connParams['AxonComponent21_0p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_0p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_0p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3p0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3p2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3p3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent21_0m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_0m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_0m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_1m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_2m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3m0a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3m2a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent21_3m3a'] = {     'preConds': {'pop': 'Component2_1'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 



netParams.connParams['AxonComponent22_0p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_0p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_0p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3p1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3p0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3p3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent22_0m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_0m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_0m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_1m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_2m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3m1a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3m0a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent22_3m3a'] = {     'preConds': {'pop': 'Component2_2'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 



netParams.connParams['AxonComponent23_0p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_0p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_0p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3p1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3p2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3p0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponent23_0m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_0m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_0m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_1m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_2m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3m1a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3m2a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponent23_3m0a'] = {     'preConds': {'pop': 'Component2_3'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 






netParams.connParams['AxonComponentm_1p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_1p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_1p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_1p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_1PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_2p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_2p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_2p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_2p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_2PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_0p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_0p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_0p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_0p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_0PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_3p0a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_3p1a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_3p2a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentm_3p3a'] = {     'preConds': {'pop': 'Operator_MINUS'},    'postConds': {'pop': 'Output_3PLUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

netParams.connParams['AxonComponentp_1m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_1m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_1m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_1m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_1MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_2m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_2m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_2m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_2m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_2MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_0m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_0m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_0m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_0m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_0MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_3m0a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS0'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_3m1a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS1'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_3m2a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS2'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 
netParams.connParams['AxonComponentp_3m3a'] = {     'preConds': {'pop': 'Operator_PLUS'},    'postConds': {'pop': 'Output_3MINUS3'},    'probability': exc_probability4,    'weight': inh_weight,    'delay': inh_delay,    'synMech': 'inh'} 

























#simConfig.duration = 100

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}

netParams.stimSourceParams['bkg_1'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 100, 'duration': 200}
netParams.stimSourceParams['bkg_2'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 600, 'duration': 200}
netParams.stimSourceParams['bkg_3'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 1100, 'duration': 200}
netParams.stimSourceParams['bkg_4'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 1600, 'duration': 200}
netParams.stimSourceParams['bkg_5'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 2100, 'duration': 200}
netParams.stimSourceParams['bkg_6'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 2600, 'duration': 200}
netParams.stimSourceParams['bkg_7'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 3100, 'duration': 200}
netParams.stimSourceParams['bkg_8'] = {'type': 'NetStim', 'rate': 30, 'noise': 0.5, 'start': 3600, 'duration': 200}

netParams.stimSourceParams['bkg_1i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 300, 'duration': 200}
netParams.stimSourceParams['bkg_2i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 800, 'duration': 200}
netParams.stimSourceParams['bkg_3i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 1300, 'duration': 200}
netParams.stimSourceParams['bkg_4i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 1800, 'duration': 200}
netParams.stimSourceParams['bkg_5i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 2300, 'duration': 200}
netParams.stimSourceParams['bkg_6i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 2800, 'duration': 200}
netParams.stimSourceParams['bkg_7i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 3300, 'duration': 200}
netParams.stimSourceParams['bkg_8i'] = {'type': 'NetStim', 'rate': 310, 'noise': 0.5, 'start': 3800, 'duration': 200}


#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}


#netParams.stimTargetParams['bkg->PYRplus'] = {'source': 'bkg', 'conds': {'pop': 'Operator_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PYR2'] = {'source': 'bkg', 'conds': {'pop': 'Component1_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
#netParams.stimTargetParams['bkg->PYR3'] = {'source': 'bkg', 'conds': {'pop': 'Component2_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}


netParams.stimTargetParams['bkg_1->CE'] = {'source': 'bkg_1', 'conds': {'pop': 'INPUT_CE'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_2->0'] = {'source': 'bkg_2', 'conds': {'pop': 'INPUT_0'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_3->PLUS'] = {'source': 'bkg_3', 'conds': {'pop': 'INPUT_PLUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_4->2'] = {'source': 'bkg_4', 'conds': {'pop': 'INPUT_2'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_5->MINUS'] = {'source': 'bkg_5', 'conds': {'pop': 'INPUT_MINUS'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_6->1'] = {'source': 'bkg_6', 'conds': {'pop': 'INPUT_1'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_7->PLUS'] = {'source': 'bkg_7', 'conds': {'pop': 'INPUT_PLUSf'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}
netParams.stimTargetParams['bkg_8->2'] = {'source': 'bkg_8', 'conds': {'pop': 'INPUT_2f'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

netParams.stimTargetParams['bkg_1i>CE'] = {'source': 'bkg_1i', 'conds': {'pop': 'INPUT_CE'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_2i->0'] = {'source': 'bkg_2i', 'conds': {'pop': 'INPUT_0'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_3i->PLUS'] = {'source': 'bkg_3i', 'conds': {'pop': 'INPUT_PLUS'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_4i>2'] = {'source': 'bkg_4i', 'conds': {'pop': 'INPUT_2'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_5i->MINUS'] = {'source': 'bkg_5i', 'conds': {'pop': 'INPUT_MINUS'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_6i>1'] = {'source': 'bkg_6i', 'conds': {'pop': 'INPUT_1'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_7i->PLUSf'] = {'source': 'bkg_7i', 'conds': {'pop': 'INPUT_PLUSf'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}
netParams.stimTargetParams['bkg_8i>2f'] = {'source': 'bkg_8i', 'conds': {'pop': 'INPUT_2f'}, 'weight': 5.1, 'delay': 3, 'synMech': 'inh'}




#netParams.stimTargetParams['bkg->PYRplus'] = {'source': 'bkg', 'conds': {'pop': 'TOTAL_INPUT'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

#1 oscilator
#2 PLUS MINUS
#3 filter
#4 html
#6layers
#+(+)



# Simulation options
simConfig = specs.SimConfig()       # object of class SimConfig to store simulation configuration

simConfig.duration = 4*1e3          # Duration of the simulation, in ms
simConfig.dt = 0.025                # Internal integration timestep to use
simConfig.verbose = False           # Show detailed messages
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1          # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'tut2'  # Set file output name
simConfig.savePickle = False        # Save params, network and sim output to pickle file
simConfig.saveJson = True

simConfig.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
simConfig.analysis['plotTraces'] = {'include': [0,55,270,275,280,285,290,295,300,305,310,315,320], 'saveFig': True} #590,595,600,605,610,615,620,625,630,635,640,645,650,655,660,665,670,675,680,685,690,695,700,705,710,715,120,725,730,735,740,745,750,755,760,765,770,775], 'saveFig': True} # ,65,215,225,275,280,285,290,295,300,305,310,315,320,325,330,335,340,345,350,355,360,365,370,375,380,385,390,395,400,405,410,415,420,425], 'saveFig': True}  # 0 - PLUS, 2 - Comp 1 0, 6 - Comp 2 0, 
simConfig.analysis['plot2Dnet'] = {'saveFig': True}                   # plot 2D cell positions and connections

# Create network and run simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)

# import pylab; pylab.show()  # this line is only necessary in certain systems where figures appear empty

# check model output
sim.checkOutput('tut2')
