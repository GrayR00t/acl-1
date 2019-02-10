from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

def rslt(user, password):
    url = 'http://erp.iitbbs.ac.in'
    browser = RoboBrowser(history=False, parser='html.parser')
    response = browser.open(url)
    form = browser.get_form(action='login.php')
    form['email'].value = user
    form['password'].value = password
    browser.submit_form(form)

    if (browser.url != 'http://erp.iitbbs.ac.in/home.php'):
        return False

    attendance_link = 'http://erp.iitbbs.ac.in/Result/results.php'
    browser.open(attendance_link)

    soup = BeautifulSoup(browser.response.text, 'html.parser')
    content1 = soup.find('div', attrs={'class': 'inner2'})
    table0 = content1.find('table' ,attrs={'class':'marks_list'})
    table1 = table0.find_all('table')
    heading = table1[0].find_all('tr')





    result = dict()
    '''
    for row in heading: # Don't need headers
        td = row.find_all('td')
        code = td[0].text.strip()
        subject = td[1].text.strip()
        L_T_P = td[2].text.strip()
        credit= td[3].text.strip()
        Grade = td[4].text.strip()
        result['heading'] = {
            'Code' :code,
            'name' : subject,
            'L_T_P': L_T_P,
            'Credit': credit,
            'Grade': Grade
        }'''
    lst =[]
    lst1 =[]
    for i in range (len(table1)):
        num =0
        
        #print(len(table1[i].find_all('tr'))) 
        for row in table1[i].find_all('tr'):

            td = row.find_all('td')
            #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            #print(td)
            #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            #print(len(td))
            #lst =[]
            for j in td:
                #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                #print(i)
                #print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
                #print(j.text.strip())
                lst.append(j.text.strip())
            #lst.append(lst1)
            #print(lst)    
            result['table'+str(num)] =lst 
            lst =[]
            num = num+1            
    return result
#id1 = input('enter your roll no:')
#pass1 =input('enter password:')   

#print(rslt('17EE01033','' ))
