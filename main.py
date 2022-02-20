import copy
import re
from pprint import pprint
import csv

from contact_utils import ContactUtils

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

contact_dictionary = {}
for contact in contacts_list[1:]:
    new_contact = ContactUtils.normalize(contact)
    contact_key = new_contact[0] + new_contact[1]
    if contact_key not in contact_dictionary:
        contact_dictionary[contact_key] = new_contact
    else:
        old_contact = contact_dictionary[contact_key]
        contact_dictionary[contact_key] = ContactUtils.merge(old_contact, contact)

with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(list(contact_dictionary.values()))
