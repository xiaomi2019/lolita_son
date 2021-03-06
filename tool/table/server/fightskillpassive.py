# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightskillpassive_map = {};
fightskillpassive_map[101] = {"id":101,"name":"连击","type":"普通","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"连击预处理","efftime":"使用技能","effrate":45,"effdst":1,"effvalue":"1,0",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":0,"effvalue":"",},{"efftype":"连击","efftime":"未命中","effrate":100,"effdst":0,"effvalue":"",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"连击预处理","efftime":"使用技能","effrate":55,"effdst":1,"effvalue":"1,0",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":0,"effvalue":"",},{"efftype":"连击","efftime":"未命中","effrate":100,"effdst":0,"effvalue":"",},],},],},],};
fightskillpassive_map[102] = {"id":102,"name":"法连","type":"法术","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"连击预处理","efftime":"使用技能","effrate":25,"effdst":1,"effvalue":"1,0,(406,441,442,407,447,456,459,463,9032,9042,465,466,469,472,473,474,476,477,6953,6954,479,)",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":0,"effvalue":"500",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"连击预处理","efftime":"使用技能","effrate":35,"effdst":1,"effvalue":"1,0,(406,441,442,407,447,456,459,463,9032,9042,465,466,469,472,473,474,476,477,6953,6954,479,)",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":0,"effvalue":"400",},],},],},],};
fightskillpassive_map[103] = {"id":103,"name":"反击","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反击","efftime":"伤害","effrate":30,"effdst":0,"effvalue":"40",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反击","efftime":"伤害","effrate":30,"effdst":0,"effvalue":"80",},],},],},],};
fightskillpassive_map[104] = {"id":104,"name":"反震","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反震","efftime":"伤害","effrate":30,"effdst":0,"effvalue":"25",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反震","efftime":"伤害","effrate":30,"effdst":0,"effvalue":"50",},],},],},],};
fightskillpassive_map[105] = {"id":105,"name":"反射","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反射","efftime":"伤害","effrate":30,"effdst":0,"effvalue":"446,1",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"effdata":[{"efftype":"反射","efftime":"受击","effrate":30,"effdst":0,"effvalue":"457,1",},],},],},],};
fightskillpassive_map[106] = {"id":106,"name":"吸血","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"攻击增加","pvalue":20,"effdata":[{"efftype":"吸血","efftime":"命中","effrate":50,"effdst":1,"effvalue":"30",},],},],},],};
fightskillpassive_map[120] = {"id":120,"name":"强力","type":"普通","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"攻击增加","pvalue":100,"effdata":[],},],},],};
fightskillpassive_map[119] = {"id":119,"name":"强壮","type":"普通","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"气血增加","pvalue":20,"effdata":[],},],},],};
fightskillpassive_map[112] = {"id":112,"name":"感知","type":"普通","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"感知","pvalue":30,"effdata":[],},],},],};


class Fightskillpassive:
	def __init__(self, key):
		config = fightskillpassive_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightskillpassive(key):
		config = fightskillpassive_map.get(key);
		if not config:
			return
		return Fightskillpassive(key)

