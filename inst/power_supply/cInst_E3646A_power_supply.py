from cInst_power_supply import cInst_power_supply

def cInst_E3646A_power_supply(inst, inst_id, connection_mode, address):
    return [cInst_E3646A_1(inst, inst_id, connection_mode, address),
            cInst_E3646A_2(inst, inst_id, connection_mode, address)]

class cInst_E3646A_1(cInst_power_supply):
    '''
    TBD
    '''
    pass

class cInst_E3646A_2(cInst_power_supply):
    '''
    TBD
    '''
    pass