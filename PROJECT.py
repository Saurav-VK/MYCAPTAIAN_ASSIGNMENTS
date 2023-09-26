import csv
def write_info(info_list):
    with open('Student_details.csv','a',newline='') as csv_file:
              writer= csv.writer(csv_file)
              if csv_file.tell()==0:
                  writer.writerow(["Name:", "Age", "Contact info", "E-mail ID"])
              writer.writerow(info_list)

if __name__ == '__main__':                                   
    Addinfo=True
    St_no=1
    while(Addinfo):
        Student_details=input("Enter the details of student #{} in the following order: [Name Age Contact_no E-mail]".format(St_no))
        print("Entered info = "+Student_details)
        Student_detail_list=Student_details.split(' ')
        print("Entered details is: "+str(Student_detail_list))
        print("\nThe entered details is:\nName:{}\nAge:{}\nContact:{}\nEmail:{}\n".format(Student_detail_list[0],Student_detail_list[1],Student_detail_list[2],Student_detail_list[3]))
        choice=input("Is the Entered details correct? Answer with a Y/N: ")
        if choice=='Y':
            write_info(Student_detail_list)
            continuity_check=input("Do you want to add the details of more students? Answer with a (Y/N): ")
            if continuity_check=='Y':
                Addinfo=True
                St_no=St_no+1
            elif continuity_check=='N':
                Addinfo=False
            else:
                print('Invalid choice!!')
        elif choice=='N':
            print('Please re-enter details!!')
       




              