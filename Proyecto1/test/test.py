import unittest
import mpb22p1
from unittest import TestCase
from mpb22p1.src.mpb22.eda.tabular import TabularDatasetSummary
class MyFirstTest(TestCase):
    def test(self):
        t=TabularDatasetSummary("D:/Documentos/Licenciatura en Ciencia de Datos/6. Sexto Semestre/Modulado Predictivo/unemployment analysis.csv",["None","A"],None)
        d=t.histogram("2002")
        print(d)
if __name__ == '__main__':
    unittest.main()