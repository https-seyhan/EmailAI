import pypff #module
import os
os.chdir('/home/saul/emails')

# Email class
class readEmails:
    # Class attributes
    pst = pypff.file()
 
    def __init__(self):
        print("Emails")
 
    def getEmail(self, email):
        print("Get the content of the Email", email)
        self.pst.open(email)
        root = self.pst.get_root_folder()
   
        for folder in root.sub_folders:
            print("folder ", folder)
            self.__getMesageDetails(folder)
         
        folder = root.get_sub_folder(1)
        print(folder)
        count = folder.get_number_of_sub_items()
        print("Counts ", count)

        #self.__getMesageDetails(folder.get_sub_item(0))
        #self.__getMesageDetails(folder.sub_messages(0))
        self.pst.close()
 
    def __getMesageDetails(self, folder):
        print("Folder ", folder)
        print("Messages  ", folder.sub_messages)
        message_list = []
        for message in folder.sub_messages:
            print("Message ", message)
            message_dict = processMessage(message)
            message_list.append(message_dict)
        example = processMessage(out.msg)
        #print("Message List ", message_list)
        #subject = msg.subject
        #content = msg.plain_text_body.decode()
        #sender = msg.sender_name
        #header = msg.transport_headers
        #sent_time = msg.delivery_time      
#if __name__ == '__main__':
reademails = readEmails()
reademails.getEmail('DestinationPst.pst')
    

