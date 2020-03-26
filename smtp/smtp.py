import subprocess
class Snmpdf(object):
    """Инструмент командной строки snmpstatus"""
    def __init__(self,
                 Version="v2c",
                 DestHost="localhost",
                 Community="public",
                 verbose=True):
        self.Version = Version
        self.DestHost = DestHost
        self.Community = Community
        self.verbose = verbose
    def query(self):
        """Создает запрос для snmpstatus"""
        Version = self.Version
        DestHost = self.DestHost
        Community = self.Community
        verbose = self.verbose
        try:
            snmpstatus = "snmpstatus %s c %s %s" % (Version, Community, 
                                                     DestHost)
            if verbose:
                print ("Running: %s" % snmpstatus)
            p = subprocess.Popen(snmpstatus,
                                 shell=True,
                                 stdout=subprocess.PIPE)
            out = p.stdout.read()
            return out
        except:
            import sys
            print >> sys.stderr, "error running %s" % snmpstatus
def _main():
    snmpstatus = Snmpdf()
    result = snmpstatus.query()
    print (result)
    
if __name__ == "__main__":
    _main()

