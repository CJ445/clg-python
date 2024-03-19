from tkinter import *
# from PIL import ImageTk,Image
from tkinter import ttk
window = Tk()
window.geometry("600x300")
window.title("Registration Form")
window.config()


lable = Label(window,text = "Registration Form",font=("Cambria",25))
lable.place(x=10,y=10)


l1 = Label(window,text = "Full name",font=("Cambria",13))
l1.place(x=10,y=62)


l2 = Entry(window,width=60)
l2.place(x=140,y=62)


l3 = Label(window,text="Email",font=("Cambria",13))
l3.place(x=10,y=92)


l4 = Entry(window,width=60)
l4.place(x=140,y=92)


l5 = Label(window,text="Gender",font=("Cambria",13))
l5.place(x=10,y=122)


v=IntVar()
c=StringVar()


Radiobutton(window,text="Male",
            variable=v,
            value=1,
            font=("Cambria",13)).place(x=140,y=122)


Radiobutton(window,text="Female",
            variable=v,
            value=2,
            font=("Cambria",13)).place(x=209,y=122)


l6 =Label(window,text="Country",font=("Cambria",13))
l6.place(x=10,y=152)


countrychoosen =ttk.Combobox(window,width = 25,textvariable = c,state="readonly")
countrychoosen['values'] = ("Select your country",
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Democratic Republic of the Congo",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman",
    "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")

countrychoosen.place(x=140,y=153)
countrychoosen.set("Select your country")
l7 =Label(window,text="Programming",font=("Cambria",13))
l7.place(x=10,y=185)

a=IntVar()
b=IntVar()


Checkbutton(window,text="Java",
            variable=a,
            onvalue=1,
            offvalue=0,
            font=("Cambria",13)).place(x=140,y=187)


Checkbutton(window,text="Python",
            variable=b,
            onvalue=1,
            offvalue=0,
            font=("Cambria",13)).place(x=200,y=187)


l9 = Button(text="Submit",fg='white',bg="red")
l9.place(x=10,y=223)

window.mainloop()
