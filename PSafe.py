import requests
import sys
from PyQt4  import QtGui,QtCore
import csv
import json
import time
from comp import Ui_PSafe

class Psafe(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_PSafe()
        self.ui.setupUi(self)
        self.datype = {'Content-type': 'application/json'}
        self.session = requests.Session() #creates a session
        self.ui.get_button.clicked.connect(self.getz)
        self.ui.post_button.clicked.connect(self.postz)
        self.ui.put_button.clicked.connect(self.putz)
        self.ui.del_button.clicked.connect(self.deletz)
        self.ui.importbutton.clicked.connect(self.importz)
        self.ui.browse_tbutton.clicked.connect(self.Browse)
        self.ui.csv_button.clicked.connect(self.to_csv)

        self.ui.Build_tbutton.clicked.connect(self.build_header)

#creates url and key
    def build_header(self):
        self.serv_name = self.ui.Serv_lnedit.text()
        self.url = self.ui.url_linedit.text()

        if self.serv_name == "":
            self.build_err()


        else:
            self.url_data = 'https://' + self.serv_name + '/eEye.RetinaCS.Server/api/public/v3/' + self.url
            self.URL = 'https://' + self.serv_name + '/eEye.RetinaCS.Server/api/public/v3/Auth/SignAppin'
            self.auth_key = self.ui.auth_lineedit.text()

            if (self.auth_key == ""):
                self.no_key_info()
                self.auth_key = 'PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;' #default key

            else:
                self.key_added()


    #Creating data
    def postz(self):
        try:
            self.headers = {'Authorization': '{}'.format(self.auth_key)}
            url = self.url_data
            if (url == self.URL):
                self.session.headers.update(self.headers)
                response = self.session.post(url, verify=False)
                results = str(response) + "=> " + "\n" + str(response.text)
                self.ui.textBrowser.setText(results)
                self.dat = json.loads(str(response.text))



            else:
                self.datype = {'Content-type': 'application/json'}
                self.session.headers.update(self.headers)
                x = self.ui.data_linedit.text()
                data = self.get_data(x)
                self.session.post(self.URL, verify=False)

                response = self.session.post(url, data=data, headers=self.datype)
                results = str(response) + "=> " + "\n" + str(response.text)
                self.ui.textBrowser.setText(results)
                self.dat = json.loads(str(response.text))

        except Exception as mess:
            self.somerror(mess)





    #Retrieving data
    def getz(self):

        try:

            self.headers = {'Authorization': '{}'.format(self.auth_key)}
            url = self.url_data
            self.session.headers.update(self.headers)
            self.session.post(self.URL, verify=False)
            response = self.session.get(url, verify=False)
            results = str(response) + "=> " + "\n" + str(response.text)
            self.ui.textBrowser.setText(results)
            self.dat = json.loads(str(response.text))


        except Exception as mess:
            self.somerror(mess)


      #Updating data
    def putz(self):
        try:
            self.headers = {'Authorization': '{}'.format(self.auth_key)}
            url = self.url_data
            self.datype = {'Content-type': 'application/json'}
            self.session.headers.update(self.headers)
            x = self.ui.data_linedit.text()
            data = self.get_data(x)
            self.session.post(self.URL, verify=False)
            response = self.session.put(url, data=data, headers=self.datype)
            results = str(response) + "=> " + "\n" + str(response.text)
            self.dat = json.loads(str(response.text))


            self.ui.textBrowser.setText(results)
        except Exception as mess:
            mess=str(mess)
            self.somerror(mess)




    #deleting data
    def deletz(self):
        try:
            self.headers = {'Authorization': '{}'.format(self.auth_key)}
            self.session.headers.update(self.headers)
            url = self.url_data
            self.session.post(self.URL, verify=False)  # Sign in
            response = self.session.delete(url)
            results = str(response) + "=> " + "\n" + str(response.text)
            self.ui.textBrowser.setText(results)

        except Exception as mess:
            self.somerror(mess)



    #importing xml file for queue
    def importz(self):
        try:
            self.headers = {'Authorization': '{}'.format(self.auth_key)}
            self.session.headers.update(self.headers)
            url = self.url_data  # get the url
            pathfile = str(self.ui.pathlinedit.text())  # get the filepath
            file = open(pathfile, 'r+')
            filecontents = file.read()
            bar = [ord(item) for item in str(
                filecontents)]  # list of bytes from contents of file...body must be  WorkgroupID,1,FileName,PasswordSafe.xml,FileContents,bar
            x = self.ui.data_linedit.text()
            # Get the data from the user as a list
            data = self.get_impdata(x, bar)
            self.session.post(self.URL, verify=False)
            response = self.session.post(url, data=data, headers=self.datype)
            results = str(response) + "=> " + "\n" + str(response.text)
            self.ui.textBrowser.setText(results)
        except Exception as mess:
            self.somerror(mess)


    def get_data(self,x):
        words = x.split(',')  # list of words

        keys = list()  # creating a keys list
        vals = list()  # creating a list for values
        mlist = []  # final list
        lwords = (len(words)) - 1
        x = 0
        while x <= lwords:

            if ((x % 2) == 0):

                keys.append(words[x])

            else:
                if words[x].isdigit():  # checking for values that are digits
                    vals.append(int(words[x]))
                else:

                    vals.append(words[x])
            x += 1

        tuplist = tuple(vals)  # converting values list to tuple
        mlist.append(tuplist)  # adding values tuple to new list
        d = zip(keys, mlist[0])  # merging keys with tuple values
        dicdata = dict(d)  # convert to dictionary
        data = json.dumps(dicdata)  # convert dictionary to Json
        return data

    #converts the info from the user to json form
    def get_impdata(self,x,bar):
        words = x.split(',')  # list of words

        keys = list()  # creating a keys list
        vals = list()  # creating a list for values
        mlist = []  # final list
        lwords = (len(words)) - 1

       #The code in the while loop, basically gets keys and values
        x = 0
        while x <= lwords:

            if ((x % 2) == 0):

                keys.append(words[x])  # add keys if x is even

            else:
                if (words[x]).isdigit():  # checking for values that are digits
                    vals.append(int(words[x]))
                else:

                    vals.append(words[x])
            x += 1

        tuplist = tuple(vals)  # converting values list to tuple
        mlist.append(tuplist)  # adding values tuple to new list
        d = zip(keys, mlist[0])  # merging keys with values
        dicdata = dict(d) #converting to dictionary
        dicdata['Filecontents'] = bar
        data = json.dumps(dicdata)# convert dictionary to Json data
        return data


    #browses for the file to import
    def Browse(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Select a file')
        self.ui.pathlinedit.setText(fname)

    #displays message box for missing Url parameters
    def build_err(self):

        QtGui.QMessageBox.information(self,"Missing data","Url or Server Name probably missing!")

    #Returns an error message
    def somerror(self,mess):
        mess=str(mess)
        QtGui.QMessageBox.information(self, "Error", mess + " " + "." + " " + " Url and a Server Name fields are probably empty!" )

    #Informs, that authorization key will be used
    def no_key_info(self):
        mess="A default Authorization key value will be used, since none was provided!"
        QtGui.QMessageBox.information(self, "Info",mess)

    #Alerts that a key has been added
    def key_added(self):
        mess = "Key Added Successfully!"
        QtGui.QMessageBox.information(self, "Info", mess)

#new method
    def to_csv(self):

        try:
            dres = self.dat
            dicx = {}
            strtyp = str(type(dres))

            #sometimes the data returns as a string
            if strtyp == "<class 'list'>":
                my_dict = dres[0]

                keys = my_dict.keys()  # store json data dict keys

                for key in keys:
                    dicx[key] = my_dict[key]

                with open('data.csv', 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerow(dicx)
                QtGui.QMessageBox.information(self, "Info",
                                              "Excel file {} created".format(output_file))


            else:

                keys = dres.keys()  # store json data dict keys

                for key in keys:
                    dicx[key] = dres[key]

                with open('data.csv', 'w+') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerow(dicx)

                QtGui.QMessageBox.information(self, "Info",
                                              "Excel file {} created".format(output_file))
        except Exception as mess:
            mess=str(mess)
            QtGui.QMessageBox.information(self, "Info", mess+","+"No excel sheet was created because no data was returned!")





if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    splash_pix = QtGui.QPixmap('rb.png')
    splash = QtGui.QSplashScreen(splash_pix,QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    time.sleep(2.5)

    window = Psafe()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

