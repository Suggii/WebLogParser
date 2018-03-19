###Program to Find the Histogram for Status Code, top 10######## ###Statustime and mean and median for the Status time###########
################################################################################################################################ 
from cement.core import foundation, backend
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.utils.misc import init_defaults
from datetime import datetime
import collections
from decimal import *
import os.path
######creating configuration to run the script in Cement frame work############################################################
###############################################################################################################################
date1 =  datetime.now().strftime('%Y-%m-%d')
defaults = init_defaults('myapp', 'log.logging')
defaults['log.logging']['file'] = 'myapp-' + date1 + '.log'
defaults['log.logging']['to_console'] = 'False'

class MyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "My Application does amazing things!"
        arguments = [
            ( ['-f', '--foo'],
              dict(action='store', help='the notorious foo option') ),
            ( ['-C'],
              dict(action='store_true', help='the big C option') ),
                    ]
    @expose(hide=True)
    def default(self):
        self.app.log.info('Inside MyBaseController.default()')
        if self.app.pargs.foo:
            print("Recieved option: foo => %s" % self.app.pargs.foo)
################################################################################################################################
####Function to check if files exist or not, if exists open the ##file##########################################################
################################################################################################################################
    @expose(hide=True)
    def openFile(self):
        self.app.log.info("Inside Open File.command1()")
        fobj = None
        if(os.path.exists(self.app.pargs.foo)):
                  fobj = open(self.app.pargs.foo,"r")
        else:
             self.app.log.error("file not found")
        return fobj
################################################################################################################################
#######Function histogramHttpStatus to  Collect Stats for the HTTPS Status######################################################
################################################################################################################################
    @expose(help="this command does relatively nothing useful")
    def histogramHttpStatus(self):
        self.app.log.info("Inside MyBaseController.histogramHttpStatus()")
        cntHttpStatus = dict()
        fobj = self.openFile()
        if (fobj != None):
            for line in fobj:
              try:
                  spltLine =  int(line.split()[10])
                  if not spltLine in cntHttpStatus:
                    cntHttpStatus[spltLine] = 1
                  else:
                    cntHttpStatus[spltLine] += 1
              except ValueError:
                   self.app.log.error("the value is not correct:" + line)
            cntHttpStatusO = collections.OrderedDict(sorted(cntHttpStatus.items()))
            fobj.close()
        print(cntHttpStatusO)
################################################################################################################################
#######Function topTenStatusTimes  to Get top 10 Status time####################################################################
################################################################################################################################

    @expose(aliases=['cmd2'], help="more of nothing")
    def topTenStatusTimes(self):
        self.app.log.info("Inside MyBaseController.topTenStatusTimes()")
        fobj = self.openFile()
        rqstTimes = []
        if (fobj != None):
           for line in fobj:
              try:
                   rqstTimes.append(Decimal((line.split()[6])))
              except InvalidOperation:
                   self.app.log.error("data line error :" + line)
           rqstTimesReverse = sorted(rqstTimes,reverse=True)
           fobj.close()
        print(rqstTimesReverse[:10])

###############################################################################################################################
#######Function meanAndMedianStatusTimes to Get the Mean and Median for the Status time########################################
    @expose(aliases=['cmd3'], help="more of nothing")
    def meanAndMedianStatusTimes(self):
        self.app.log.info("Inside MyBaseController.meanAndMedianStatusTimes()")
        fobj = self.openFile()
        i = 0
        sum = 0
        dict = {}
        rqstMeanTimes = []
        if (fobj != None):
            for line in fobj:
               try:
                    rqstMeanTimes.append(Decimal((line.split()[6])))
                    sum = sum + rqstMeanTimes[i]
                    i = i + 1
               except InvalidOperation:
                       self.app.log.error("data line error :" + line)
            rqstMeanTimes = sorted(rqstMeanTimes)
            records = len(rqstMeanTimes)
#########################Mean value############################################################################################
            mean = sum/records
#############################Median Value######################################################################################
            if (records%2 != 0):
              median1 = rqstMeanTimes[((records + 1)/2) -1]
            else:
              median1 =  (rqstMeanTimes[(records/2) -1] + rqstMeanTimes[(records/2)])/2
            dict['mean'] = mean
            dict['median'] = median1
        fobj.close()
        print(dict)

###################Cement Configuration########################################################################################
class MyApp(CementApp):
    class Meta:
        label = 'myapp'
        config_defaults = defaults
        base_controller = 'base'
        handlers = [MyBaseController]


#######################My App run method#######################################################################################
with MyApp() as app:
     app.setup()
     app.run()
     app.close()

###############################################################################################################################