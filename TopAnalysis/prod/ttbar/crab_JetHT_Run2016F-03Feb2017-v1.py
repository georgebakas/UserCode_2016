from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()
config.General.requestName = 'JetHT_Run2016F-03Feb2017-v1'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'flat-data-cfg.py'
config.JobType.maxJobRuntimeMin = 2750
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDataset = '/JetHT/Run2016F-03Feb2017-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
config.Data.outLFNDirBase = '/store/user/gbakas/ttbar/'
config.Data.publication = False
config.Site.storageSite = 'T2_CH_CERN'
