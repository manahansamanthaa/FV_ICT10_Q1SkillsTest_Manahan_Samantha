from pyscript import display


title= "Order your Food!"
description= "Input order, name, address, and mobile number! :))"

display(title, target="webtitle")
display(description, target="desc1")


from pyscript import document, display


def generate(e): #we put e for event handling
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    mobile_number = document.getElementById("mobile_number").value

 #multiline
    profile = f"""
Profile: 
    Name    : {name}
    Address : {address}
    Mobile number  : {mobile_number}
    """

document.getElementById("message").innerText = profile





