import json
import pickle

from abc import abstractmethod, ABCMeta

# containers: List, Dict, Tuple, Set



class SerializationInterface(metaclass=ABCMeta):
	@abstractmethod
	def serialize(self):
		pass



# list to json serialization/deserialization
class SerializationJsonList(SerializationInterface):
	def serialize(self, data):
		with open('data_list.json', 'w') as file:
			json.dump(data, file)
 
	def deserialize(self):
		with open('data_list.json', 'r') as file:
			data = json.load(file)
			return data
	
# list to bin serialization/deserialization
class SerializationBinList(SerializationInterface):
	def serialize(self, data):
		with open('data_list.bin', 'wb') as file:
			pickle.dump(data, file)
 
	def deserialize(self):
		with open('data_list.bin', 'rb') as file:
			data = pickle.load(file)
			return data

# dict to json serialization/deserialization
class SerializationJsonDict(SerializationInterface):
	def serialize(self, data):
		with open('data_dict.json', 'w') as file:
			json.dump(data, file)
 
	def deserialize(self):
		with open('data_dict.json', 'r') as file:
			data = json.load(file)
			return data
	
# dict to bin serialization/deserialization
class SerializationBinDict(SerializationInterface):
	def serialize(self, data):
		with open('data_dict.bin', 'wb') as file:
			pickle.dump(data, file)
 
	def deserialize(self):
		with open('data_dict.bin', 'rb') as file:
			data = pickle.load(file)
			return data


# tuple to json serialization/deserialization
class SerializationJsonTuple(SerializationInterface):
	def serialize(self, data):
		with open('data_tuple.json', 'w') as file:
			json.dump(data, file)
 
	def deserialize(self):
		with open('data_tuple.json', 'r') as file:
			data = json.load(file)
			list2tuple = tuple(data)
			return list2tuple
	
# tuple to bin serialization/deserialization
class SerializationBinTuple(SerializationInterface):
	def serialize(self, data):
		with open('data_tuple.bin', 'wb') as file:
			pickle.dump(data, file)
 
	def deserialize(self):
		with open('data_tuple.bin', 'rb') as file:
			data = pickle.load(file)
			return data


# set to json serialization/deserialization
class SerializationJsonSet(SerializationInterface):
	def serialize(self, data):
		set2list = list(data)
		with open('data_set.json', 'w') as file:
			json.dump(set2list, file)
 
	def deserialize(self):
		with open('data_set.json', 'r') as file:
			data = json.load(file)
			list2set = set(data)
			return list2set
	
# set to bin serialization/deserialization
class SerializationBinSet(SerializationInterface):
	def serialize(self, data):
		with open('data_set.bin', 'wb') as file:
			pickle.dump(data, file)
 
	def deserialize(self):
		with open('data_set.bin', 'rb') as file:
			data = pickle.load(file)
			return data




if __name__ == '__main__':
	my_list = [1, 2.4, True, 'string']
	sl = SerializationJsonList().serialize(my_list)
	dsl = SerializationJsonList().deserialize()
	assert my_list == dsl

	slb = SerializationBinList().serialize(my_list)
	dslb = SerializationBinList().deserialize()
	assert my_list == dslb


	my_dict = {'first': 1, 'second': 2, '3': 3}
	sd = SerializationJsonDict().serialize(my_dict)
	dsd = SerializationJsonDict().deserialize()
	assert my_dict == dsd

	sdb = SerializationBinDict().serialize(my_dict)
	dsdb = SerializationBinDict().deserialize()
	assert my_dict == dsdb


	my_tuple = (1, 2, 'string')
	st = SerializationJsonTuple().serialize(my_tuple)
	dst = SerializationJsonTuple().deserialize()
	assert my_tuple == dst

	stb = SerializationBinTuple().serialize(my_tuple)
	dstb = SerializationBinTuple().deserialize()
	assert my_tuple == dstb


	my_set = {1, 2, 'string'}
	ss = SerializationJsonSet().serialize(my_set)
	dss = SerializationJsonSet().deserialize()
	assert my_set == dss

	ssb = SerializationBinSet().serialize(my_set)
	dssb = SerializationBinSet().deserialize()
	assert my_set == dssb