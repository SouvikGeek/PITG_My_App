from ldap3 import Server, Connection, ALL, MODIFY_REPLACE, MODIFY_ADD
import config
from services.all_func import current_time

# function to deactivate employee
def modify_ldap_entry_deactivation(effected_user):
    # Define the server
    s = Server(config.host, get_info=ALL) 

    # define the connection
    c = Connection(s, user=config.user, password=config.password)
    c.bind()
    currentTime = current_time()
    accountDeactivationreason='Account has been deactivated on :'+currentTime
    # perform the Modify operation
    c.modify('cn='+effected_user+','+config.search_base,
         {'description': [(MODIFY_ADD, [accountDeactivationreason])],
          'loginDisabled': [(MODIFY_REPLACE, ['True'])]})
    print(c.result)

    # close the connection
    c.unbind()
   
   
# function to activate employee    
def modify_ldap_entry_activation(effected_user):
    # Define the server
    s = Server(config.host, get_info=ALL) 

    # define the connection
    c = Connection(s, user=config.user, password=config.password)
    c.bind()
    currentTime = current_time()
    accountActivationreason='Account has been activated on :'+currentTime
    # perform the Modify operation
    c.modify('cn='+effected_user+','+config.search_base,
         {'description': [(MODIFY_ADD, [accountActivationreason])],
          'loginDisabled': [(MODIFY_REPLACE, ['False'])]})
    print(c.result)

    # close the connection
    c.unbind()    

# function to provide employee access to resource
def modify_ldap_group(effected_user,grpname, reason):
    # Define the server
    s = Server(config.host, get_info=ALL)

    # define the connection
    c = Connection(s, user=config.user, password=config.password)
    c.bind()
    currentTime = current_time()
    dnUser= 'cn='+effected_user+','+config.search_base
    resourceAccessReason='Access request raised on :'+currentTime
    fetch_reason = reason
    print(fetch_reason)
    # perform the Modify operation
    c.modify(grpname,
         {'equivalentToMe': [(MODIFY_ADD, [dnUser])],
          'member': [(MODIFY_ADD, [dnUser])]})
    print(c.result)

    # close the connection
    c.unbind()
    


# Function to update employee address or phone number
def update_address_or_phone(user_dn, new_phone_number, new_address):
    # Define the server
    s = Server(config.host, get_info=ALL)

    # Define the connection
    c = Connection(s, user=config.user, password=config.password)
    c.bind()

    # Define the attributes to update
    changes = {
        'telephoneNumber': [(MODIFY_REPLACE, [new_phone_number])],
        'l': [(MODIFY_REPLACE, [new_address])],
    }

    # Update the user's attributes
    c.modify(user_dn, changes)

    # Check the result
    if 'resultCode' in c.result and c.result['resultCode'] == 0:
        print(f"User {user_dn} updated successfully.")
    else:
        print(f"Error updating user {user_dn}: {c.result}")

    # Close the LDAP connection
    c.unbind()




# Usage example
# if __name__ == '__main__':
#     user_dn = 'cn=john_doe,ou=users,dc=example,dc=com'  # DN of the user you want to update
#     new_phone_number = '123-456-7890'
#     new_address = '123 Main St, City, Country'

#     update_ldap_user(user_dn, new_phone_number, new_address)


# if __name__ == 'main':
#     m = modify_ldap_group('user1','cn=pam-imanager-server-access,ou=groups,o=pitg')