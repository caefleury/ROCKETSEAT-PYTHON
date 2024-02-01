
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

    Methods:
        __init__(name, telephone, email, favorite):
            Initializes a new Contact instance 
            with the given parameters.

        get_all_contacts():
            Prints information for all contacts.

        get_all_favorite_contacts():
            Prints information for all favorite contacts.

        update_name(name):
            Updates the name of the contact.

        update_telephone(telephone):
            Updates the telephone number of the contact.

        update_email(email):
            Updates the email address of the contact.

        update_favorite(favorite):
            Updates the favorite status of the contact.
    """

    __instances = []

    def __init__(self,name,telephone,email,favorite) -> None:
        self.__name = name
        self.__telephone = telephone
        self.__email = email
        self.__favorite = favorite
        self.__data = {'name' : self.__name, 
                       'telephone' : self.__telephone, 
                       'email' : self.__email, 
                       'favorite' : self.__favorite}
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

    def update_name(self, name):
        self.__name = name
        self.__data['name'] = self.__name
    
    def update_telephone(self, telephone):
        self.__telephone = telephone
        self.__data['telephone'] = self.__telephone
    
    def update_email(self, email):
        self.__email = email
        self.__data['email'] = self.__email
    
    def update_favorite(self, favorite):
        self.__favorite = favorite
        self.__data['favorite'] = self.__favorite
    
    @classmethod
    def delete_contact(cls,data):
        """
        Deletes the contact instance.
        """
        Contact.__instances.remove(data)
        print("Contact deleted successfully.")
    

contato1 = Contact('Sergio','(11) 99999-9999','sergio@email.com',True)
contato2 = Contact('João','(11) 99999-9999', 'joao@email.com',False)

Contact.get_all_favorite_contacts()

