class Parent():
    def __init__(self,last_name,eye_color):
        print("parent constructor called")
        self.last_name=last_name
        self.eye_color=eye_color
    def show_info(self,last_name,eye_color):
        print(self.last_name)
        print(self.eye_color)

        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("child constructor was called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys
        

billy_cyrus=Parent("broacha","green");
billy_cyrus.show_info(5,3)



miley_cyrus=Child("broacha","green",3)
miley_cyrus.show_info(10,3)

#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)

