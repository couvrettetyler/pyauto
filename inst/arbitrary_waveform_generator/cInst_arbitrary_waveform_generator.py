from cInst import cInst

class cInst_arbitrary_waveform_generator(cInst):
    '''
    arbitrary waveform generator main class
    '''
    def __init__(self, inst, inst_id, connection_mode, address):
        super().__init__(inst, inst_id, connection_mode, address)
        self.type = 'arbitrary_waveform_generator'
