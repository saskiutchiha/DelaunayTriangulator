from PyQt5.QtCore import Qt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FCQTA
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton ,QHBoxLayout,QScrollArea,QTextEdit,QLabel,QGridLayout
from PyQt5.QtGui import QPixmap
from functools import partial
import matplotlib.tri as tri
import numpy as np
from triangilisation import *
# from triangilisation import triangilisation 
nextwin = None
class infodelauray(QWidget):
   def __init__(self):
      super().__init__()
      self.img = QPixmap('OIP.jpeg')
      self.img1 = QPixmap('OIPT.jpeg')

      internalwin = QWidget(self)
      
      self.labelinfo = QLabel(self)
      self.labelinf2 = QLabel(self)
      self.labelinfo3 = QLabel(self)
      hbox = QHBoxLayout()
      vbox = QVBoxLayout()
      self.labelinfo1 = QLabel(self)
      self.labelinfo1.setPixmap(self.img)
      self.labelinfo3.setPixmap(self.img1)

      self.labelinfo1.setStyleSheet("")
      self.labelinfo.setText("""Boris Triangulation is a prominent figure in the field of computational geometry,known for his significant
   contributions to mesh generation and triangulation techniques.His method, widely recognized for its efficiency and accuracy,
    addresses the challenge of dividing a geometric domain into non-overlapping triangles. This process is crucial for  
  various applications, including computer graphics, finite element analysis, and geographic information systems.Triangulation's approach
   is distinguished by its focus on optimizing the quality of the triangulated mesh. His method involves algorithmic techniques that ensure the 
  resulting triangles are well-shaped, avoiding elongated or degenerate configurations. This enhances the accuracy of simulations 
  and analyses performed on the mesh. One of the core aspects of Triangulation's method is its adaptability to different types of
domains, whether they are simple or complex. The algorithm can handle varying degrees of rregularity in the input data,
  i making it versatile for real-world applications.

Triangulation's work has been instrumental in advancing the field, providing robust solutions for efficiently generating high-quality  
  meshes. His method continues to influence modern computational geometry, highlighting the importance of precise and reliable 
  triangulation techniques in computational applications.
                                                                                
""" )
      self.labelinfo.setOpenExternalLinks(True)
      self.labelinfo.setStyleSheet("font-family:Georgia;font-size:16px")    
      self.next = QPushButton('next >')
      self.next.clicked.connect(self.nextwin)
      self.next.setStyleSheet("background-color:#9400d3 ;border-radius:10px")
      self.next.setFixedSize(70,50)
      hbox.addWidget(self.labelinfo1)
      hbox.addWidget(self.labelinfo3)

      # hbox.addWidget(self.labelinfo1)
      vbox.addLayout(hbox)
      vbox.addWidget(self.labelinfo)
      vbox.addWidget(self.next)
      internalwin.setLayout(vbox)
      internalwin.setStyleSheet("background-color:#dda0dd ;border-radius:10px")
      internalwin.move(15,25)
      internalwin.setFixedSize(950,700)
      self.setFixedSize(1000,750)

   def nextwin(self):
         global nextwin
         nextwin = mainwindow()
         nextwin.show()
        #  self.close()

class TriangleWin(FCQTA):
    def __init__(self, parent):
        fig,self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)
        self.ax.grid()
        
        
class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.list_hboxs_elements = []
        self.points = [(0,0)]
        self.vboxcontainer = QWidget()
        self.TW = TriangleWin(self)
        self.hbox1 = QHBoxLayout()
        self.scrol = QScrollArea()
        self.vbox1 = QVBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.but = QPushButton('+',self)
        
        self.but.setFixedSize(30,30)
        self.but.setStyleSheet("""QPushButton{border-radius: 15px; background-color:#9400d3 ; color : white;} 
                          QPushButton:hover{
                          color:#9400d3; background-color : white;
                          }""")
        self.text = QTextEdit()
        self.text.setFixedSize(100,30)
        self.text.textChanged.connect(partial(self.get_x,0))

        self.text1 = QTextEdit()
        self.text1.setFixedSize(100,30)
        self.text1.textChanged.connect(partial(self.get_y,0))

        self.but.clicked.connect(self.addbut)
        self.list_hboxs_elements.append((self.but,self.text,self.text1))
        self.hbox2.addWidget(self.but)
        self.hbox2.addWidget(self.text)
        self.hbox2.addWidget(self.text1)
        self.creatbut = QPushButton('creat',self)
        self.creatbut.setStyleSheet("background-color:#9400d3 ;border-radius:10px")
        self.creatbut.setFixedSize(70,50)

        self.creatbut.clicked.connect(self.triangilize)
        self.vbox1.addWidget(self.creatbut)
        self.vbox1.addLayout(self.hbox2)
        
        self.vboxcontainer.setLayout(self.vbox1)
        self.scrol.setWidget(self.vboxcontainer)
        self.scrol.setWidgetResizable(True)
        # self.scrol.setStyleSheet("border-radius:10px;border-width")
        self.scrol.setFixedWidth(300)

        self.hbox1.addWidget(self.scrol)
        
        self.hbox1.addWidget(self.TW)
        self.setLayout(self.hbox1)
        # self.setFixedSize(100,100)
    def addbut(self):
        but = QPushButton('+',self)
        but.setStyleSheet("""QPushButton{border-radius: 15px; background-color:#9400d3 ; color : white;} 
                          QPushButton:hover{
                          color:#9400d3; background-color : white;
                          }""")

        but.setFixedSize(30,30)
        hbox = QHBoxLayout()
        text = QTextEdit()
        text.setFixedSize(100,30)
        text1 = QTextEdit()
        
        text1.setFixedSize(100,30)
        
        hbox.addWidget(but)
        hbox.addWidget(text)
        hbox.addWidget(text1)

        but.clicked.connect(self.addbut)
        index = len(self.list_hboxs_elements) -1
        self.list_hboxs_elements[index][0].setText('-')
        
        self.list_hboxs_elements[index][0].clicked.disconnect()
        self.list_hboxs_elements[index][0].clicked.connect(partial(self.delet_but,index))
        text.textChanged.connect(partial(self.get_x,index+1))
        text1.textChanged.connect(partial(self.get_y,index+1))
        self.list_hboxs_elements.append((but,text,text1))
        self.points.append((0,0))

        
        self.vbox1.addLayout(hbox)
    def delet_but(self,index):
        self.list_hboxs_elements[index][0].hide()
        self.list_hboxs_elements[index][1].hide()
        self.list_hboxs_elements[index][2].hide()
        print(index)
        self.list_hboxs_elements = self.list_hboxs_elements[:index] + [None] + self.list_hboxs_elements[index+1:]
        self.points[index] = None
    def get_x(self,index):
      try :
        x = self.list_hboxs_elements[index][1].toPlainText()
        self.points[index] = (float(x),self.points[index][1])
      except:
          pass
    def get_y(self,index):
      try :
        y = self.list_hboxs_elements[index][2].toPlainText()
        self.points[index] = (self.points[index][0],float(y))
        print(self.points)
      except:
         pass
    def triangilize(self):
        self.TW.ax.cla()
        self.TW.ax.grid(True)
        points = [point for point in self.points if point != None]
        triangles = triangilisation(points)
        for tr in triangles:
         x = np.array([tr[0][0], tr[1][0], tr[2][0]])
         y = np.array([tr[0][1], tr[1][1], tr[2][1]])
         triangulation = tri.Triangulation(x, y)
         self.TW.ax.triplot(triangulation, '', label='')
         self.TW.ax.scatter([x for x,y in points],[y for x,y in points])
        
       
    
    

        
app = QApplication(sys.argv)

win = infodelauray()
win.show()
sys.exit(app.exec_())