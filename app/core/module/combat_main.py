# coding: utf-8
# 
import app.base.game_module_mgr
from app.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.combatsvr.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.core.game_module_def as game_module_def
class combat_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(combat_main,self).__init__();
		self.character_map = {};
		
		return
	
	def start(self):
		super(combat_main,self).start();
		self.register_event(EVENT_LOGIN,self.on_login);
		self.register_event(EVENT_LOGOUT,self.on_logout);
		self.register_event(EVENT_STARTCOMBAT,self.on_startcombat);
		self.register_event(EVENT_ENDCOMBAT,self.on_endcombat);
		self.register_net_event(C2S_WAR_PLAYEND,self.on_war_playend)
		self.register_event(EVENT_SEND2CLIENT,self._send2client);
		self.register_event(EVENT_SEND2CLIENTBYCID,self._send2clientbycid)
		return
	def _getdidbycid(self,cId):
		if self.character_map.has_key(cId):
			return self.character_map[cId];
		return
	def _send2clientbycid(self,ud):
		cmd = ud[0]
		cId = ud[1];
		dId = self._getdidbycid(cId);
		if dId == None:
			log.err("_send2clientbycid err:%s %s"%(cId,ud));
			return
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
		return
	def _send2client(self,ud):
		cmd = ud[0]
		dId = ud[1];
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
		return
	
	def _float_msg(self,dId,msg):
		c_data = {};
		c_data['msg'] = msg;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_NOTIFY_FLOAT,dId,c_data]);
		return;
	def _is_cId_valid(self,cId):#其实就是角色是否在线的判定
		return self.character_map.has_key(cId);
	def on_login(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		self.character_map[cId] = dId;
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('chat_main on_login fatal err %d'%(cId));
			return
		c_info = c_data.get('data');
		
		
	
		return
	def on_logout(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];

		del self.character_map[cId];

		return
	def on_startcombat(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		return
	def on_endcombat(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		return
	def on_war_playend(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		return
	def dispose(self):
		super(combat_main,self).dispose();
		return