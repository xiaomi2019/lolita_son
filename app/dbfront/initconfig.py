#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from dataloader import registe_madmin,CheckMemDB,MAdminManager
from firefly.dbentrust.memclient import mclient
from firefly.server.globalobject import GlobalObject,remoteserviceHandle

from twisted.python import log

@remoteserviceHandle('gate')
def flushdata():
	print "dbfront flushdata"
	MAdminManager().checkAdmins()

def doWhenStop():
    """服务器关闭前的处理
    """
    print "##############################"
    print "##########checkAdmins#############"
    print "##############################"
    MAdminManager().checkAdmins()
    
GlobalObject().stophandler = doWhenStop
    

def loadModule():
    mclient.flush_all()
    registe_madmin()
    CheckMemDB(60)