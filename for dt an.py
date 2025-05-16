# print('welocme to BAUST due list:')
# first_name=input('enter your first name:')
# last_name=input('enter your last name:')
# your_id_please=input('enter your id please:')
# your_batch=input('enter your batch:')
# your_dep=input('which depertment you form:')
# your_phone=input('please enter your phone number:')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your January due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your february due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your March due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your April due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your May due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your June due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your July due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your Auguest due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your September due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your october due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your November due is 70,000 tk')
# print(f'hey,{first_name}{last_name},{your_id_please},{your_batch},{your_dep},{your_phone},your December due is 70,000 tk')
# print('''thhaks for visiting this program.
#       we glad to inform your due list.
#       have a good day..''')
#--------------------------chapter-2--------------------------------
# therre have 4 types of datatype----
#1.integer2.floating3.string5.boolien
# a=4#int
# b=6#int
# c=6.4#float
# name='harry'#str
# #----type---
# f=type(name)
# print(f)
# print(a+b)
#---------------calculator-------------------------
# print('---calculator---')
# a=int(input('enter the 1st num:'))
# b=int(input('enter the 2nd num:'))
# print('the 1st number is',a)
# print('the 2nd number is',b)
# print(a+b)
# print('---data type---')
# a=input('enter the value of a:')
# print(type(a))
# print('---true fals--')
# a=int(input('enter the value of a:'))
# b=int(input('enter the value of b:'))
# print('a is gretter than b is',a>b)
# print('--avg--')
# a=int(input('enter the value of a:'))
# b=int(input('enter the value of b:'))
# print('avg of those 2 numbers is',(a+b)/2)
# print('--squer--')
# a=int(input('enter the value of a:'))
# print('the value of squer of a is',a**2)
#------------------------chapter3-------------------------
# name='harry'
# print(name[0:3])
#-----------------for letter---------
# letter='''dear,<!name!>,
# you are selected!!,
# <!date!>,
# for more details.....call on: 01722079024'''
# print(letter.replace('<!name!>','Aysha Adiyat Prima').replace('<!date!>','1st november,2025'))
#---------list-----------------
# member=['ahnaf tahmid-220211001',
#         'aysha siddika-220211002',
#         'mishkat jahan moumi-220211003',
#         'mahiul islam moon-220211004']
# print(member)
#-------for uni-------------
# name=input('enter your name:')
# id=int(input('enter your id:'))
# dep=input('enter your depertment:')
# mob=int(input('enter your mobile number:'))
#-------------new well to do list-----
# fruit=[]
# f1=input('enter your fruit name:')
# fruit.append(f1)
# f2=input('enter your fruit name:')
# fruit.append(f2)
# f3=input('enter your fruit name:')
# fruit.append(f3)
# print(fruit)
#------sort the list----
# number=[33,64,12,2,48]
# number.sort()
# number.reverse()
# print(number)
#------dictionary-----
name_id={'ahnaf tahmid':220211045,
         'aysha siddika':220211002,
         'miskat jahan':220211003,
         'isarat radia':220211004,
         'rana babu':220211005,
         'fahim habib':220211006,
         'mahiul kabir moon':220211007,
         'jahana sinmin':220211008,
         'dilruba akter':220211009,}
name_id.update({'ahnaf tahmid':220211001})
name_cgpa={'ahnaf tahmid':3.98,
         'aysha siddika':4.00,
         'miskat jahan':2.44,
         'isarat radia':2.98,
         'rana babu':3.22,
         'fahim habib':3.21,
         'mahiul kabir moon':2.25,
         'jahana sinmin':3.09,
         'dilruba akter':3.02}
name_cgpa.update()
name_dep={'ahnaf tahmid':'BBA',
         'aysha siddika':'BBA',
         'miskat jahan':'BBA',
         'isarat radia':'BBA',
         'rana babu':'BBA',
         'fahim habib':'BBA',
         'mahiul kabir moon':'BBA',
         'jahana sinmin':"BBA",
         'dilruba akter':'BBA',}
name_dep.update()
print('your id:',name_id.get('0'))
print('your cgpa:',name_cgpa.get('0'))
print('your depertment:',name_dep.get('0'))
    