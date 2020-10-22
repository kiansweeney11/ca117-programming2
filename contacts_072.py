#!/usr/bin/env python


class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return ("{} {} {}".format(self.name, self.phone, self.email))


class ContactList(object):

    def __init__(self, d={}):
        self.d = d

    def add_contact(self, other):
        self.d[other.name] = other

    def del_contact(self, other):
        if other in self.d:
            (self.d).pop(other)

    def get_contact():
        if other in self.d:
            return (self.d[other])
        else:
            None

    def __str__(self):
        return("{} {} {}".format(self.name, self.phone, self.email
         key=self.name))



from contacts_072 import Contact, ContactList
import sys

def main():
    cl = ContactList()
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)

    c = cl.get_contact('Jimmy')
    print(c)
    c = cl.get_contact('Mary')
    print(c)

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()
