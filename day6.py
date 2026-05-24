contact = {'anna':2903847899,'godwin':4988766544,'varun':9876543451}
for key,values in contact.items():
    print(f'name: {key} , number: {values}')
a = input('enter the name:')
if a in contact:
    print(f"Number: {contact[a]}")
else:
    print("Contact not found")