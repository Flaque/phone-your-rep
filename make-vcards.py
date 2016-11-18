import vobject
import csv

INDICES = {
    'state' : 0,
    'full' : 1,
    'last_name' : 2,
    'first_name' : 3,
    'party' : 4,
    'district_address_1' : 5,
    'district_address_2' : 6,
    'district_address_3' : 7,
    'district_tel' : 8,
    'dc_office_address' : 9,
    'dc_tel' : 10,
    'email' : 11,
    'website' : 12,
    'class' : 13,
    'bioguide_id' : 14,
    'photo' : 15
}

def write(name, text):
    with open(name, 'w') as vCardFile:
        vCardFile.write(text)

with open('senators.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        v_card = vobject.vCard()

        first, last = row[INDICES['first_name']], row[INDICES['last_name']]

        v_card.add('n') # 'n' is "Name" in V_card land
        v_card.n.value = vobject.vcard.Name(family=last, given=first)

        v_card.add('fn') # 'fn' is "Full Name"
        v_card.fn.value = first + ' ' + last

        v_card.add('email')
        v_card.email.value = row[INDICES['email']]
        v_card.email.type = 'INTERNET'

        # Write to a file
        text = v_card.serialize()
        write(first + '_' + last + '.csv', text)
