#!/bin/tcsh
source /cvmfs/cms.cern.ch/crab3/crab.csh
voms-proxy-init --voms cms --valid 168:00
voms-proxy-info --all
cmsenv
