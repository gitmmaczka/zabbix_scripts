import requests as req
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def read_config(config_file):
    variables={}
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                variables[key.strip()] = value.strip()

    return variables

def set_u_group(api_url, api_key, ug_name):
    query = {
        "jsonrpc": "2.0",
        "method": "usergroup.create",
        "params": {
            "name": ug_name
        },
        "auth": api_key,
        "id": 1
    }
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def get_u_group(api_url, api_key, ug_name):
    query = {
        "jsonrpc": "2.0",
        "method": "usergroup.get",
        "params": {
            "output": "simple",
            "filter": {
                "name": [
                    ug_name
                ]
            }
        },
        "auth": api_key,
        "id": 1
        
    }
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def update_h_u_group(api_url, api_key, ugid, hgid_group):
    query = {
    "jsonrpc": "2.0",
    "method": "usergroup.update",
    "params": {
        "usrgrpid": ugid,
        "users_status": "0",
        "hostgroup_rights": [
            {
                "id": hgid_group,
                "permission": 3
            }
#            for hgid in hgid_group
        ]
    },
    "auth": api_key,
    "id": 1
}
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def update_t_u_group(api_url, api_key, ugid, tgid_group):
    query = {
    "jsonrpc": "2.0",
    "method": "usergroup.update",
    "params": {
        "usrgrpid": ugid,
        "users_status": "0",
        "templategroup_rights": [
            {
                "id": tgid_group,
                "permission": 3
            }
#            for tgid in tgid_group
        ]
    },
    "auth": api_key,
    "id": 1
}
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def get_h_group(api_url, api_key, hg_name):
    query = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                hg_name
            ]
        }
    },
    "auth": api_key,
    "id": 1
}
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()

def set_h_group(api_url, api_key, hg_name):
    query = {
    "jsonrpc": "2.0",
    "method": "hostgroup.create",
    "params": {
        "name": hg_name
    },
    "auth": api_key,
    "id": 1
}
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def get_t_group(api_url, api_key, tg_name):
    query = {
    "jsonrpc": "2.0",
    "method": "templategroup.get",
    "params": {
        "output": "extend",
        "filter": {
             "name": [
                 tg_name
             ]
        }
    },
    "auth": api_key,
    "id": 1
}
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def set_t_group(api_url, api_key, tgroup):
    query = {
    "jsonrpc": "2.0",
    "method": "templategroup.create",
    "params": {
        "name": tgroup
    },
    "auth": api_key,
    "id": 1
}


    response = req.post(api_url, json=query, verify=False)
    return response.json()


def update_p_t_group(api_url, api_key, tgid_group):
    query = {
        "jsonrpc": "2.0",
        "method": "templategroup.propagate",
        "params": {
            "groups": [
                {
                    "groupid": tgid_group
                    }
                    ],
                    "permissions": True
                    },
                    "auth": api_key,
                    "id": 1
                    }
        
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def update_p_h_group(api_url, api_key, tgid_group):
    query = {
        "jsonrpc": "2.0",
        "method": "hostgroup.propagate",
        "params": {
            "groups": [
                {
                    "groupid": tgid_group
                    }
                    ],
                    "permissions": True,
                    "tag_filters": True
                    },
                    "auth": api_key,
                    "id": 1
                    }
        
    
    response = req.post(api_url, json=query, verify=False)
    return response.json()


def update_st_u_group(api_url, api_key, ugid, sgid_group):
    query = {
    "jsonrpc": "2.0",
    "method": "usergroup.update",
    "params": {
        "usrgrpid": ugid,
        "users_status": "0",
        "templategroup_rights": [
            { "id": sgid, "permission": perm }
            for sgid, perm in sgid_group
        ]
    },
    "auth": api_key,
    "id": 1
}
    response = req.post(api_url, json=query, verify=False)
    return response.json()
