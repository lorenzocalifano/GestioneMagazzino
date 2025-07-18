from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject

def save_ui_file():
    ui_str = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>750</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Login - EVENTICA</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: #1E90FF;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="email_input">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>200</y>
      <width>271</width>
      <height>30</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: white; 
color: #1E90FF;
padding: 5px;
border-radius: 3px;</string>
    </property>
    <property name="placeholderText">
     <string>Email</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="password_input">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>240</y>
      <width>271</width>
      <height>30</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: white; 
color: #1E90FF;
padding: 5px;
border-radius: 3px;</string>
    </property>
    <property name="echoMode">
     <enum>QLineEdit::Password</enum>
    </property>
    <property name="placeholderText">
     <string>Password</string>
    </property>
   </widget>
   <widget class="QPushButton" name="login_button">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>290</y>
      <width>271</width>
      <height>40</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
   background-color: white;
   color: #1E90FF;
   font-weight: bold;
   border-radius: 5px;
   padding: 8px;
}
QPushButton:hover {
   background-color: #F0F0F0;
}</string>
    </property>
    <property name="text">
     <string>Login</string>
    </property>
   </widget>
   <widget class="QLabel" name="error_message">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>340</y>
      <width>271</width>
      <height>30</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white; 
font-weight: bold;
qproperty-alignment: AlignCenter;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="reset_password_button">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>380</y>
      <width>271</width>
      <height>40</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
   background-color: white;
   color: #1E90FF;
   font-weight: bold;
   border-radius: 5px;
   padding: 8px;
}
QPushButton:hover {
   background-color: #F0F0F0;
}</string>
    </property>
    <property name="text">
     <string>Password dimenticata?</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>70</y>
      <width>750</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Montserrat</family>
      <pointsize>30</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white; 
qproperty-alignment: AlignCenter;</string>
    </property>
    <property name="text">
     <string>EVENTICA</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>750</width>
     <height>42</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

    with open("loginWindow.ui", "w", encoding="utf-8") as f:
        f.write(ui_str)

if __name__ == "__main__":
    save_ui_file()
    print("File loginWindow.ui generato con successo!")