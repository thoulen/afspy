from afs.model.BaseModel import BaseModel
from datetime import datetime


class Server(BaseModel):
    """
    Model object of a server of any type
    """
    
    def __init__(self):
        """
        initialize an empty object.
        Partitions are not in the same Table in DB_CACHE as 
        Server, so the attribute Parts will be inserted by VolumeService
        """
        ## for db index
        self.id = None
        ## AFS Server UUID
        self.uuid = ""
        ## list of DNS-hostnames
        self.servernames = []
        ## list of ipaddrs
        self.ipaddrs = []
        ## flag if this server is a fileserver
        self.fileserver = 0
        ## flag if this server is a databaseserver
        self.dbserver  = False
        ## flag if this server is a databaseserver-Cloneonly
        self.clonedbserver = False
        ## flag if this ??
        self.confserver = 0
        ## flag if this ??
        self.distserver = 0
        ## rxdebug version string
        self.version = ""
        ## ??
        self.status   = ''
        ## Id for table location where this server is placed physically
        self.id_location = 0
        ## custom description about HW etc.
        self.description = ''
        ## Date of object creation
        self.cdate   = datetime.now()
        ## Date of last object update
        self.udate   = datetime.now()
        ## flag if this object is synced with reality.
        self.sync    = 0
        ## flag if this object is not fully filled yet
        self._isComplete = False
