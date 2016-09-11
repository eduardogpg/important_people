class AdvancedMessage(object):
	messages = []

	class Message():
		def __init__(self, message = '', type_message ='', identifier=''):
			self.message = message
			self.type_message = type_message
			self.identifier = identifier
			self.create_pre_idetifier()

		def create_pre_idetifier(self):
			self.pre_idetifier = "alert {}".format(self.identifier)

	@classmethod
	def add(cls, message ='', type_message ='', identifier = ''):
		new_message = cls.Message(message, type_message, identifier)
		cls.messages.append(new_message)

	@classmethod
	def get_messages(cls):
		return cls.messages