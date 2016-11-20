import vobject # pip install vobject
import usaddress # pip install usaddress
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


def getAddress(row):
    """ Gets a vobject Address object from a row in the dataset """
    street = row[INDICES['district_address_1']]
    line_2 = row[INDICES['district_address_2']]
    line_3 = row[INDICES['district_address_3']]

    unparsed_address = street + ' ' + line_2 + ' ' + line_3

    return vobject.vcard.Address(street=unparsed_address)


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
            v_card.url.type_param = 'Contact'

        # Phone Number
        # See http://stackoverflow.com/questions/13552836/creating-a-multiple-phone-vcard-using-vobject
        # For adding multiple telephone numbers
        district_phone = row[INDICES['district_tel']]
        tel = v_card.add('tel')
        tel.value = district_phone
        tel.type_param = 'District Office'

        dc_phone = row[INDICES['dc_tel']]
        tel = v_card.add('tel')
        tel.value = district_phone
        tel.type_param = 'DC Office'

        # Party
        note = PARTY[row[INDICES['party']]]
        v_card.add('note')
        v_card.note.value = note

        # Website
        website = row[INDICES['website']]
        url = v_card.add('url')
        url.value = website
        url.type_param = 'Website'

        # Addresses
        adr = v_card.add('adr')
        adr.value = getAddress(row)
        adr.type_param = 'District Office Address'

        # Write to a file
        text = v_card.serialize()
        write(first + '_' + last + '.vcf', text)
