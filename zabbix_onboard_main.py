import zabbix_onboard_def
import csv
import json


h_group_name = 0
t_group_name = 1
u_group_name = 2

configs = zabbix_onboard_def.read_config("onboard.conf")
url = configs.get('url')
key = configs.get('key')
account_code = configs.get('account_code')
template = configs.get('template')
ro_template = configs.get('ro_template')
static = "Account/{}".format(account_code)



hidar=[]
uidar=[]
ridar=[]

##Create host groups

with open (template, mode='r', newline='', encoding='utf-8') as file:
     c_reader = csv.reader(file)
     headers = next(c_reader)
     for row in c_reader:
       if row[h_group_name].strip():
            h_group=row[h_group_name].replace("CODE", account_code)
            h_group_get = zabbix_onboard_def.get_h_group(url, key, h_group)
            if (len(h_group_get['result']) == 0):
                print ('Group' , h_group, 'not exists. Creating')
                zabbix_onboard_def.set_h_group(url, key, h_group)
            else:                
                print('Group ', h_group, 'exists. Aborting.')


##Create templates groups

with open (template, mode='r', newline='', encoding='utf-8') as file:
     c_reader = csv.reader(file)
     headers = next(c_reader)
     for row in c_reader:
       if row[t_group_name].strip():
            t_group=row[t_group_name].replace("CODE", account_code)
            t_group_get = zabbix_onboard_def.get_t_group(url, key, t_group)
            if (len(t_group_get['result']) == 0):
                print ('Group' , t_group, 'not exists. Creating')
                zabbix_onboard_def.set_t_group(url, key, t_group)
            else:                
                print('Group ', t_group, 'exists. Aborting.')
#            

#Creating user groups:

with open (template, mode='r', newline='', encoding='utf-8') as file:
     c_reader = csv.reader(file)
     headers = next(c_reader)
     for row in c_reader:
       if row[u_group_name].strip():
            u_group=row[u_group_name].replace("CODE", account_code)
            u_group_get = zabbix_onboard_def.get_u_group(url, key, u_group)
            if (len(u_group_get['result']) == 0):
                print ('Group' , u_group, 'not exists. Creating')
                zabbix_onboard_def.set_u_group(url, key, u_group)
            else:                
                print('User group ', u_group, 'exists. Aborting.')


#Get host groups IDs
with open (template, mode='r', newline='', encoding='utf-8') as file:
     c_reader = csv.reader(file)
     headers = next(c_reader)
     for row in c_reader:
      if row[h_group_name].strip():
           h_group=row[h_group_name].replace("CODE", account_code)
           hid_group_get = zabbix_onboard_def.get_h_group(url, key, h_group)
           hidar.append(hid_group_get['result'][0]['groupid'])

#Get user groups IDs
with open (template, mode = 'r', newline='', encoding='utf-8') as file:
    c_reader = csv.reader(file)
    headers = next(c_reader)
    for row in c_reader:
        if row[u_group_name].strip():
           u_group=row[u_group_name].replace("CODE", account_code)
           uid_group_get = zabbix_onboard_def.get_u_group(url, key, u_group)
           uidar.append(uid_group_get['result'][0]['usrgrpid'])


templategroupid = zabbix_onboard_def.get_t_group(url, key, static)

#Get RO template groups IDs
with open (ro_template, mode='r', newline='', encoding='utf-8') as file:
     c_reader = csv.reader(file)
     headers = next(c_reader, None)
     for row in c_reader:
        #print(row[0])
        if row[0].strip():
            s_group=row[0].replace("CODE", account_code)
            rid_group_get = zabbix_onboard_def.get_t_group(url, key, s_group)
            #print(rid_group_get['result'][0]['groupid'])
            ridar.append((rid_group_get['result'][0]['groupid'], "2"))



ridar.append((templategroupid['result'][0]['groupid'], "3")) 


##Update user groups:


hostgroupid = zabbix_onboard_def.get_h_group(url, key, static)
h_group_id = hostgroupid['result'][0]['groupid']

for i in range(len(uidar)):
    u_group_id = uidar[i]
    update_ro = zabbix_onboard_def.update_st_u_group(url, key, u_group_id, ridar)
    update_h = zabbix_onboard_def.update_h_u_group(url, key, u_group_id, h_group_id)
    #print(update_ro)

print ("Applying group permissions. Please wait... ")

#Propagate
zabbix_onboard_def.update_p_t_group(url, key, templategroupid['result'][0]['groupid'])
zabbix_onboard_def.update_p_h_group(url, key,hostgroupid['result'][0]['groupid'])

print("Done. Please check entries in Zabbix portal.")

##EOF