
class Contact:
    """
    A class representing a contact with name, telephone, 
    email, and favorite status.

    Attributes:
        __name (str): The name of the contact.
        __telephone (str): The telephone number of the contact.
        __email (str): The email address of the contact.
        __favorite (bool): The favorite status of the contact.
        __data (dict): A dictionary containing contact information.

    """

    __instances = []

    def __init__(self, name, telephone, email, favorite) -> None:
        self.__name = name
        self.__telephone = telephone
        self.__email = email
        self.__favorite = favorite
        self.__data = {'name': self.__name,
                       'telephone': self.__telephone,
                       'email': self.__email,
                       'favorite': self.__favorite}
        Contact.__instances.append(self.__data)

    @classmethod
    def get_all_contacts(cls):
        for instance in cls.__instances:
            print(instance)

    @classmethod
    def get_all_favorite_contacts(cls):
        for instance in cls.__instances:
            if instance['favorite'] == True:
                print(instance)

    @classmethod
    def delete_contact(cls, email):
        """
        Deletes the contact instance.
        """
        for instance in cls.__instances:
            if instance['email'] == email:
                data = {
                    'name': instance['name'],
                    'telephone': instance['telephone'],
                    'email': instance['email'],
                    'favorite': instance['favorite']
                }
                Contact.__instances.remove(data)
        print("Contact deleted successfully.")

    @classmethod
    def find_contact_by_email(cls, email):
        for instance in cls.__instances:
            if instance['email'] == email:
                return instance

    @classmethod
    def update_name(cls, email, new_name):
        contact = cls.find_contact_by_email(email)
        contact['name'] = new_name
        print("Name updated successfully.")

    @classmethod
    def update_telephone(cls, email, new_telephone):
        contact = cls.find_contact_by_email(email)
        contact['telephone'] = new_telephone
        print("Telephone updated successfully.")

    @classmethod
    def update_email(cls, email, new_email):
        contact = cls.find_contact_by_email(email)
        contact['email'] = new_email
        print("Email updated successfully.")

    @classmethod
    def update_favorite(cls, email, new_favorite):
        contact = cls.find_contact_by_email(email)
        contact['favorite'] = new_favorite
        print("Favorite status updated successfully.")


contato1 = Contact('Sergio', '(11) 99999-9999', 'sergio@email.com', True)
contato2 = Contact('João', '(11) 99999-9999', 'joao@email.com', False)

Contact.get_all_favorite_contacts()
