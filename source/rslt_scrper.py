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

    lst =[]
    lst1 =[]
    for i in range (len(table1)):
        num =0 
        for row in table1[i].find_all('tr'):

            td = row.find_all('td')
            for j in td:
                lst.append(j.text.strip())   
            result['table'+str(num)] =lst 
            lst =[]
            num = num+1            
    return result

