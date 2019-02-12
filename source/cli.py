import click
import keyring
import getpass
from source.rslt_scrper import rslt
from source.scrapper import attempt
from tabulate import tabulate

@click.command()
@click.option('-r', '--roll', prompt='Roll Number', help='Enter the Roll Number for ERP Login.')
def attendance(roll):
    """
    Get the credentials first
    """
    password = keyring.get_password('ERP', roll)
    if password == None:
        password = getpass.getpass("Password: ")
        ans = input("Do you want to store your password?(y/N)")
        if ans=='y':
            keyring.set_password('ERP', roll, password)
            
    response = attempt(roll, password)
    response_ = rslt(roll, password)
    # Fetch attendance from ERP and Pretty Print it on Terminal.
    num = int(input('Enter 0 for Result and 1 for Attendance:'))
    if num ==1:

        if not response:
            click.secho('Invalid Credentials, Login failed.', fg='red', bold=True)
        else:
            table = attendance_table(response)
            print(tabulate(table, headers=["Subject Name", "Attended", "Percentage"],
                    tablefmt="fancy_grid"))
    elif num ==0:
        if not response_:
            click.secho('Invalid Credentials, Login failed.', fg='red', bold=True)
        else:
            table = result_table(response_)
            print(tabulate(table, headers=["Subject Code", "Subject Name", "L-T-P","Credit","Grade"],
                    tablefmt="fancy_grid"))        

                

def attendance_table(response):
    result = list()
    for (code, data) in response.items():
        row = list()
        row.append(data['name'])
        row.append(data['attended'] + '/' + data['total'])
        row.append(data['percentage'])
        result.append(row)

    return result
def result_table(response_):
    result = list()
    for i in range(len(response_.keys())):
        result.append(response_["table"+str(i)])


    return result    


