# Amirreza Hosseini 9820363
# CN2 Project
# Floodlight Controller - flows

import httplib
import json

class StaticEntryPusher(object):
	def __init__(self, server):
		self.server = server
	def get(self, data):
		ret = self.rest_call({}, 'GET')
		return json.loads(ret[2])
	def Set(self, data):
		ret = self.rest_call(data, 'POST')
		return ret[0] == 200
	def remove(self, objtype, data):
		ret = self.rest_call(data, 'DELETE')
		return ret[0] == 200
	def rest_call(self, data, action):
		path = '/wm/staticentrypusher/json'
		header = {
			'Cantent-type':'application/json',
			'Accept':'application/json'
		}
		body = json.dumps(data)
		Conn = httplib.HTTPConnection(self.server, 8080)
		Conn.request(action,path,body,header)
		response = Conn.getresponse()
		ret = (response.status, response.reason, response.read())
		print(ret)
		Conn.close()
		return ret


pusher = StaticEntryPusher('127.0.0.1')

# PATH1 = H4 > S5 > S10 > S3 > S9 > S6 > S7 > H6
# Route from H4 to H6
flow1 = {
	"switch":"00:00:00:00:00:00:00:05",
	"name":"flow1",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=2",
}
flow2 = {
	"switch":"00:00:00:00:00:00:00:0a",
	"name":"flow2",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=5",
}
flow3 = {
	"switch":"00:00:00:00:00:00:00:03",
	"name":"flow3",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"5",
	"active":"true",
	"actions":"output=4",
}
flow4 = {
	"switch":"00:00:00:00:00:00:00:09",
	"name":"flow4",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=1",
}
flow5 = {
	"switch":"00:00:00:00:00:00:00:06",
	"name":"flow5",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=2",
}
flow6 = {
	"switch":"00:00:00:00:00:00:00:07",
	"name":"flow6",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.04",
	"ipv4_dst":"10.0.0.06",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=5",
}

# PATH2 = H8 > S9 > S6 > S11 > S10 > S5 > S2 > S8 > H9
#route from H8 to H9
flow7 = {
	"switch":"00:00:00:00:00:00:00:09",
	"name":"flow7",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"4",
	"active":"true",
	"actions":"output=1",
}
flow8 = {
	"switch":"00:00:00:00:00:00:00:06",
	"name":"flow8",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=4",
}
flow9 = {
	"switch":"00:00:00:00:00:00:00:0b",
	"name":"flow9",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=4",
}
flow10 = {
	"switch":"00:00:00:00:00:00:00:0a",
	"name":"flow10",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"7",
	"active":"true",
	"actions":"output=1",
}
flow11 = {
	"switch":"00:00:00:00:00:00:00:05",
	"name":"flow11",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"2",
	"active":"true",
	"actions":"output=1",
}
flow12 = {
	"switch":"00:00:00:00:00:00:00:02",
	"name":"flow12",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=5",
}
flow13 = {
	"switch":"00:00:00:00:00:00:00:08",
	"name":"flow13",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.08",
	"ipv4_dst":"10.0.0.09",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=4",
}

# PATH3 = H10 > S6 > S7 > S4 > S1 > S8 > S2 > S5 > S10 > H5
#route from H10 to H5
flow14 = {
	"switch":"00:00:00:00:00:00:00:06",
	"name":"flow14",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"5",
	"active":"true",
	"actions":"output=2",
}
flow15 = {
	"switch":"00:00:00:00:00:00:00:07",
	"name":"flow15",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=2",
}
flow16 = {
	"switch":"00:00:00:00:00:00:00:04",
	"name":"flow16",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"3",
	"active":"true",
	"actions":"output=4",
}
flow17 = {
	"switch":"00:00:00:00:00:00:00:0b",
	"name":"flow17",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"5",
	"active":"true",
	"actions":"output=2",
}
flow18 = {
	"switch":"00:00:00:00:00:00:00:01",
	"name":"flow18",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"4",
	"active":"true",
	"actions":"output=3",
}
flow19 = {
	"switch":"00:00:00:00:00:00:00:08",
	"name":"flow19",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=3",
}
flow20 = {
	"switch":"00:00:00:00:00:00:00:02",
	"name":"flow20",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"5",
	"active":"true",
	"actions":"output=3",
}
flow21 = {
	"switch":"00:00:00:00:00:00:00:05",
	"name":"flow21",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=2",
}
flow22 = {
	"switch":"00:00:00:00:00:00:00:0a",
	"name":"flow22",
	"eth_type":"0x0800",
	"ipv4_src":"10.0.0.10",
	"ipv4_dst":"10.0.0.05",
	"priority":"32768",
	"in_port":"1",
	"active":"true",
	"actions":"output=6",
}


pusher.Set(flow1)
pusher.Set(flow2)
pusher.Set(flow3)
pusher.Set(flow4)
pusher.Set(flow5)
pusher.Set(flow6)
pusher.Set(flow7)
pusher.Set(flow8)
pusher.Set(flow9)
pusher.Set(flow10)
pusher.Set(flow11)
pusher.Set(flow12)
pusher.Set(flow13)
pusher.Set(flow14)
pusher.Set(flow15)
pusher.Set(flow16)
pusher.Set(flow17)
pusher.Set(flow18)
pusher.Set(flow19)
pusher.Set(flow20)
pusher.Set(flow21)
pusher.Set(flow22)
