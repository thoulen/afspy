# Init 
__all__=["DbMapper",]

# setup logging, but only when configuration is setup properly
import afs
import logging

logger=logging.getLogger("DBCache")
if getattr(afs,"defaultConfig",None) :
    if getattr(afs.defaultConfig, "classBasedLogLevels", None) :
        classBasedLogLevel=afs.defaultConfig.classLogLevels.get("DBCache", None)
        if classBasedLogLevel != None :
            logger.setLevel(getattr(logging, afs.defaultConfig.classBasedLogLevels["DBCache"].upper()))
