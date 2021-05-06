class VálasztásiEredmény(object):
    _kerület: int
    _szavazatok: int
    _vnév: str
    _knév: str
    _párt_jel: str

    def __init__(self, sor: str) -> None:
        kerület, szavazatok, vnév, knév, párt_jel = sor.split(' ')
        self._kerület = int(kerület)
        self._szavazatok = int(szavazatok)
        
  
        
        

