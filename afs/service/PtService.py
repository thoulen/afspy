from afs.service.BaseService import BaseService

class PtService(BaseService):
    """
    Provides Service about a Cell global information.
    The cellname is set in the configuration passed to constructor.
    Thus one instance works only for cell, or you
    need to change self._CFG
    """
    def __init__(self,conf=None):
        BaseService.__init__(self, conf, DAOList=["fs",  ])
