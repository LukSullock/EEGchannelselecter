# -*- coding: utf-8 -*-
"""
EEG channel selector creating an XML file with selected channels.
Copyright (C) 2024  Luk Sullock Enzlin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
from xml.etree import ElementTree as ET
from PyQt6 import QtWidgets, QtCore, QtGui

#These values are default values and can be changed
channelnames=["Fp1", "Fp2", "F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2",
              "F7", "F8", "T7", "T8", "P7", "P8", "Fz", "Cz", "Pz"]
network="PsyAmp_0201"
ip="170.16.1.1"
com="COM5"
dfile="EEGchannels.xml"

#Class to define GUI
class Ui_MainWidget():
    def setupUi(self, MainWidget):
        #Set up GUI with components
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(640, 563)
#Main layout
        self.centralwidget = QtWidgets.QWidget(parent=MainWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
#Set central widget as such
        MainWidget.setCentralWidget(self.centralwidget)
#Checkboxes
        #All channel selectors in same variable for easier access
        self.CKBchannels=[QtWidgets.QCheckBox(parent=self.centralwidget) for ii in range(20)]
        for ii, _ in enumerate(self.CKBchannels):
            self.CKBchannels[ii].setObjectName(f"CKBchannel_{ii+1}")
            self.gridLayout.addWidget(self.CKBchannels[ii],ii, 2,1,1)
        self.CKBchannel_all = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.CKBchannel_all.setObjectName("CKBchannel_all")
        self.gridLayout.addWidget(self.CKBchannel_all, 20, 2, 1, 1)
#Line edits
        self.LEPsyAmp = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LEPsyAmp.setObjectName("LEPsyAmp")
        self.gridLayout.addWidget(self.LEPsyAmp, 0, 0, 1, 2)
        self.LEip = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LEip.setObjectName("LEip")
        self.gridLayout.addWidget(self.LEip, 1, 1, 1, 1)
        self.LEcom = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LEcom.setObjectName("LEcom")
        self.gridLayout.addWidget(self.LEcom, 2, 1, 1, 1)
        self.LEoutput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.LEoutput.setObjectName("LEoutput")
        self.gridLayout.addWidget(self.LEoutput, 3, 1, 1, 1)
#Labels
        self.LBLip = QtWidgets.QLabel(parent=self.centralwidget)
        self.LBLip.setObjectName("LBLip")
        self.gridLayout.addWidget(self.LBLip, 1, 0, 1, 1)
        self.LBLserial = QtWidgets.QLabel(parent=self.centralwidget)
        self.LBLserial.setObjectName("LBLserial")
        self.gridLayout.addWidget(self.LBLserial, 2, 0, 1, 1)
        self.LBLoutput = QtWidgets.QLabel(parent=self.centralwidget)
        self.LBLserial.setObjectName("LBLoutputl")
        self.gridLayout.addWidget(self.LBLoutput, 3, 0, 1, 1)
#Menubar
        self.menubar = QtWidgets.QMenuBar(parent=MainWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
#Set menubar as such
        MainWidget.setMenuBar(self.menubar)
#Actions within dropdown menu's
        self.actionOpen = QtGui.QAction(parent=MainWidget)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWidget)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWidget)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuMenu.menuAction())
#Spacers
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 21, 2, 1, 1)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget): #Function to set texts within widgets and short cuts
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "MainWidget"))
#Line edit default text
        self.LEPsyAmp.setText(_translate("MainWidget", network))
        self.LEip.setText(_translate("MainWidget", ip))
        self.LEcom.setText(_translate("MainWidget", com))
        self.LEoutput.setText(_translate("MainWidget", dfile))
#Label text
        self.LBLip.setText(_translate("MainWidget", "EEG box IP"))
        self.LBLserial.setText(_translate("MainWidget", "Serial port"))
        self.LBLoutput.setText(_translate("MainWidget", "Output file name"))
#Menu and action texts
        self.menuMenu.setTitle(_translate("MainWidget", "Menu"))
        self.actionOpen.setText(_translate("MainWidget", "Open"))
        self.actionOpen.setShortcut(_translate("MainWidget", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWidget", "Save"))
        self.actionSave.setShortcut(_translate("MainWidget", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWidget", "Save as"))
        self.actionSave_as.setShortcut(_translate("MainWidget", "Ctrl+Shift+S"))
#Checkbox texts
        self.CKBchannel_all.setText(_translate("MainWidget", "All channels"))
        self.CKBchannels[19].setText(_translate("MainWidget", "Markers"))
        self.CKBchannels[19].setChecked(True)
        for ii,_ in enumerate(self.CKBchannels[:-1]):
            self.CKBchannels[ii].setText(_translate("MainWidget", f"Channel {ii+1}"))

#Main class handling operations
class MainWindow(QtWidgets.QMainWindow, Ui_MainWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Call GUI class and set it up
        self.ui=Ui_MainWidget()
        self.ui.setupUi(self)
        #Set channel names and assign operation commands for buttons and actions
        _translate = QtCore.QCoreApplication.translate
        for channeln in range(19):
            self.ui.CKBchannels[channeln].setText(_translate("MainWindow",
                                             f"Channel {channelnames[channeln]} ({channeln+1})"))
        self.ui.CKBchannel_all.stateChanged.connect(self.check_all)
        self.ui.actionSave.triggered.connect(lambda: self.savefile(self.ui.LEoutput.text()))
        self.ui.actionSave_as.triggered.connect(lambda: self.savefile_as(self.ui.LEoutput.text()))
        self.ui.actionOpen.triggered.connect(lambda: self.openfile(filename=self.ui.LEoutput.text()))
        if len(sys.argv)>1:
            self.openfile(infile=sys.argv[1])
    #Function to check or uncheck all channels
    def check_all(self):
        state=self.ui.CKBchannel_all.isChecked()
        for channeln in range(20):
            self.ui.CKBchannels[channeln].setChecked(state)
    #Open file explorer to select a file to open
    def openfile(self,*, filename=None,infile=None):
        _translate = QtCore.QCoreApplication.translate
        #Open file explorer if no file was given as input
        if not infile:
            infile,_ = QtWidgets.QFileDialog.getOpenFileName(
                self,
                "Open File",
                f"{filename}",
                "XML files (*.xml);;All Files (*)",
            )
            #Check if a file has been selected
            if not infile:
                #Dialog box informing user that no file has been selected
                msgbox=QtWidgets.QMessageBox(parent=self.ui.centralwidget)
                msgbox.setText("No file selected")
                msgbox.exec()
                return
        #Get XML data
        tree=ET.parse(infile)
        root=tree.getroot()
        #Toggle all channel select on and off to turn all channels off
        self.ui.CKBchannel_all.setChecked(True)
        self.ui.CKBchannel_all.setChecked(False)
        #Turn on required channels
        for channel in root.iter('channel'):
            self.ui.CKBchannels[int(channel.attrib['n'])-1].setChecked(True)
        #Set network, ip, serialport, and file location as line edit texts
        self.ui.LEPsyAmp.setText(_translate("MainWindow", root[-1].find('network').text))
        self.ui.LEip.setText(_translate("MainWindow", root[-1].find('ip').text))
        self.ui.LEcom.setText(_translate("MainWindow", root[-1].find('serialport').text))
        self.ui.LEoutput.setText(_translate("MainWindow", infile))
    #Open file explorer to set a save location
    def savefile_as(self,outputfile):
        _translate = QtCore.QCoreApplication.translate
        #Open file explorer
        folder_path,_ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save File",
            f"{outputfile}",
            "XML files (*xml);;All Files (*)")
        #Check if a destination has been selected
        if folder_path:
            #Call save file function with destination
            self.savefile(folder_path)
            self.ui.LEoutput.setText(_translate("MainWindow", folder_path))
        else:
            #Dialog box informing user that no file has been selected
            msgbox=QtWidgets.QMessageBox(parent=self.ui.centralwidget)
            msgbox.setText("No file selected")
            msgbox.exec()
    #Function to save file at given location
    def savefile(self,output):
        #Check if there is atleast one channel selected
        anychecked=self.ui.CKBchannels[19].isChecked()
        if not anychecked:
            for channeln in range(19):
                if self.ui.CKBchannels[channeln].isChecked():
                    anychecked=True
                    break
            #If no channel has been selected, inform user and stop saving file
            if not anychecked:
                msgbox=QtWidgets.QMessageBox(parent=self.ui.centralwidget)
                msgbox.setText("Select at least 1 channel")
                msgbox.exec()
                return
        #Beginning text required for xml file
        xmltext='''
<vsrrp9>
    <sample_speed>500</sample_speed>

    <device>PsyPhy</device>
        	
    <filetype>matlab</filetype>
        	
    <channels>'''
        #Add text required for selected channels 
        for channeln in range(19):
            if self.ui.CKBchannels[channeln].isChecked():
                xmltext+=f'''
        <channel n="{channeln+1}">
			<chid>anin{channeln}</chid>
			<visible>yes</visible>
			<gain>6</gain>
			<color>0</color>
			<channel_mode>EEG</channel_mode>
			<lead_off>OFF</lead_off>
			<srb>SRB2</srb>
			<bias_ref>ON</bias_ref>
			<name>{channelnames[channeln]} ({channeln})</name>
			<lp_freq>70</lp_freq>
			<lp_order>4</lp_order>
			<lp_enable>YES</lp_enable>
			<hp_freq>0.1</hp_freq>
			<hp_order>2</hp_order>
			<hp_enable>YES</hp_enable>
			<notch>50.0</notch>
			<notch_enable>YES</notch_enable>
		</channel>
        '''
        #Text required for marker channel
        if self.ui.CKBchannels[19].isChecked():
            xmltext+='''
        <channel n="20">
            <chid>digin</chid>
            <visible>yes</visible>
            <gain>0</gain>
            <color>0x118800</color>
            <name>marker</name>
        </channel>'''
        #Closing text required for xml file
        xmltext+=f'''
    </channels>
		
	<experiment>
		<block n="1">
			<type>GET_DATA</type>
			<duration>86400</duration>
			<feedback>YES</feedback>
			<nr_channels>ALL</nr_channels>
			<name>test 1</name>
		</block>
	</experiment>
	
	<analysis>

		<createMATfile>YES</createMATfile>
		
	</analysis>
	
	<hardware>
		<network>{self.ui.LEPsyAmp.text()}</network>
		<ip>{self.ui.LEip.text()}</ip>
		<txpower>5</txpower>
		<impcheck_freq>2</impcheck_freq>
		<impcheck_current>1</impcheck_current>
		<parallelport>NONE</parallelport>
		<serialport>{self.ui.LEcom.text()}</serialport>
		<baudrate>19200</baudrate>
		<useoptical>NO</useoptical>
		<disablewirednetwork>YES</disablewirednetwork>
	</hardware>
	
</vsrrp9>'''
        #Turn plane text into xml data
        tree=ET.XML(xmltext)
        #Save file at the given location
        with open(output, "wb") as f:
            f.write(ET.tostring(tree, encoding='UTF-8', xml_declaration=True))
        #Inform user that file has been saved
        msgbox=QtWidgets.QMessageBox(parent=self.ui.centralwidget)
        msgbox.setText(f"XML file has been saved at {output}")
        msgbox.exec()
#Setup needed to create GUI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
