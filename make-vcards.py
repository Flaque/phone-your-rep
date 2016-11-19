import vobject
import csv
import re

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

PARTY = {
    'R' : 'Republican',
    'D' : 'Democrat',
    'I' : 'Independent'
}

FOLDER = 'vcards'

def write(name, text):
    with open(FOLDER + '/' + name, 'w') as vCardFile:
        vCardFile.write(text)

def isEmail(text):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", text):
        return True
    else:
        return False

with open('senators.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next() #Pop off first row
    for row in reader:
        v_card = vobject.vCard()

        # Name
        first, last = row[INDICES['first_name']], row[INDICES['last_name']]

        v_card.add('n') # 'n' is "Name" in V_card land
        v_card.n.value = vobject.vcard.Name(family=last, given=first)

        v_card.add('fn') # 'fn' is "Full Name"
        v_card.fn.value = first + ' ' + last

        # Email / URL
        email = row[INDICES['email']]
        if isEmail(email):
            v_card.add('email')
            v_card.email.value = email
            v_card.email.type = 'INTERNET'
        else:
            v_card.add('url')
            v_card.url.value = email

        # Phone Number
        district_phone = row[INDICES['district_tel']]
        v_card.add('tel')
        v_card.tel.value = district_phone
        v_card.tel.type_param = 'District Office'

        # Party
        role = PARTY[row[INDICES['party']]]
        v_card.add('role')
        v_card.role.value = role


        # Write to a file
        text = v_card.serialize()
        write(first + '_' + last + '.vcf', text)
