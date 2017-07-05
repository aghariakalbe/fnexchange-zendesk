import json
import requests
from fnexchange.core.plugins import AbstractPlugin


class ZendeskPlugin(AbstractPlugin):
	
	def create_ticket(self,payload):# Will create your ticket
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			response = requests.post(self.config.url+'tickets.json',auth=("aghariakalbe@gmail.com/token",self.config.api_key),json=(elements[0]))
			success=False
			if response.status_code == 201:
			  success= True 
			else:
			  success= False
			print "Status Code : " + str(response.status_code)
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	
	def update_ticket(self,payload):#Will update your tickets
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			ticket_id=str(elements[1]["ticket_id"])
			response = requests.put(self.config.url+'tickets/'+ticket_id+'.json',auth=("aghariakalbe@gmail.com/token",self.config.api_key),json=(elements[0]))

			if response.status_code == 200:
			   success= True
			else:
			   success= False
			print "Status Code : " + str(response.status_code)
			return response.content	
	
	def delete_ticket(self,payload):#Will delete ticket
			elements=payload["elements"]
			id=str(elements[0]["id"])
			response=requests.delete(self.config.url+'tickets/'+id+'.json', auth = ("aghariakalbe@gmail.com/token",self.config.api_key))
			if response.status_code==204:
			   success= True
			else:
			   success= False
			print "Status Code :" + str(response.status_code)
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}#/api/v2/tickets/{id}/mark_as_spam.json
	def spam_ticket(self,payload):#Will spam ticket and suspend requester
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			id=str(elements[0]["id"])
			response = requests.put(self.config.url+'tickets/'+id+'/mark_as_spam.json',auth=("aghariakalbe@gmail.com/token",self.config.api_key))
			if response.status_code == 200:
			   success= True
			else:
			   success= False
			print "Status Code : " + str(response.status_code)
			return 	{
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	def view_ticket(self,payload):#Working
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			ticket_id=str(elements[0]["ticket_id"])
			response=requests.get(self.config.url+'/'+ticket_id,auth= (self.config.api_key,'x'), headers=headers)
			if response.status_code == 200:
			  success= True
			else:
			  success = False
			print "Status Code : " + str(response.status_code)
			return response.content
	
	def create_contact(self,payload): #Working
			headers = { 'Content-Type' : 'application/json' } 
			elements=payload["elements"]
			contact_info=elements[0]["contact_info"]
			response = requests.post(self.config.url1,auth=(self.config.api_key,"x"), headers=headers,data = json.dumps(contact_info))
			if response.status_code==201:
				success= True
			else:
				success= False	
			print "Status Code :" + str(response.status_code)
			print response.content
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			},response.content
	
	def delete_contact(self,payload): #Working
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			domain=elements[0]["contact_id"]
			contact_id=elements[0]["contact_id"]
			response = requests.delete(self.config.url1+'/'+str(contact_id),auth=(self.config.api_key,"x"), headers=headers)
			if response.status_code==204:
				success= True
			else:
				success= False	
			print "Status Code :" + str(response.status_code)
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
			
	def update_contact(self,payload):#Put method is not allowed apparently, error 405--Couldnt update spam messages, see above,still not working
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			contact_id=str(elements[1]["contact_id"])
			response = requests.put(self.config.url1+'/'+contact_id, auth = (self.config.api_key,"x"), headers = headers, data = json.dumps(elements[0]["contact_info"]))

			if response.status_code == 200:
			   success= True
			else:
			   success= False
			print "Status Code : " + str(response.status_code)
			return response.content'''
