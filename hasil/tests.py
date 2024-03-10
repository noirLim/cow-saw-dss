from decimal import Decimal
from django.test import TestCase
from .utils import *
import re

data_kriteria_sapi = [
    {'id': 1, 'nilai': 1300.0, 'sapi_id': 1, 'kriteria_id': 2, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'},
    {'id': 2, 'nilai': 200.0, 'sapi_id': 1, 'kriteria_id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'}, 
    {'id': 3, 'nilai': 60000000.0, 'sapi_id': 1, 'kriteria_id': 4, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'}, 
    {'id': 4, 'nilai': 34.0, 'sapi_id': 1, 'kriteria_id': 5, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'}, 
    {'id': 5, 'nilai': 4.0, 'sapi_id': 1, 'kriteria_id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'}, 
    {'id': 6, 'nilai': 800.0, 'sapi_id': 2, 'kriteria_id': 2, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
    {'id': 7, 'nilai': 150.0, 'sapi_id': 2, 'kriteria_id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
    {'id': 8, 'nilai': 40000000.0, 'sapi_id': 2, 'kriteria_id': 4, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
    {'id': 9, 'nilai': 21.0, 'sapi_id': 2, 'kriteria_id': 5, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
    {'id': 10, 'nilai': 4.0, 'sapi_id': 2, 'kriteria_id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
    {'id': 11, 'nilai': 900.0, 'sapi_id': 3, 'kriteria_id': 2, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
    {'id': 12, 'nilai': 160.0, 'sapi_id': 3, 'kriteria_id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
    {'id': 13, 'nilai': 50000000.0, 'sapi_id': 3, 'kriteria_id': 4, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
    {'id': 14, 'nilai': 25.0, 'sapi_id': 3, 'kriteria_id': 5, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
    {'id': 15, 'nilai': 3.0, 'sapi_id': 3, 'kriteria_id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
  ]

data_nilai = [
        {'id': 4, 'status': 'SR', 'bobot': 1}, 
        {'id': 5, 'status': 'R', 'bobot': 2}, 
        {'id': 6, 'status': 'C', 'bobot': 3}, 
        {'id': 7, 'status': 'T', 'bobot': 4}, 
        {'id': 8, 'status': 'ST', 'bobot': 5}
]

data_kriteria = [
        {'id': 2, 'nama_kriteria': 'Berat', 'bobot_kriteria': Decimal('0.20'),'atribut':"benefit"}, 
        {'id': 3, 'nama_kriteria': 'Tinggi', 'bobot_kriteria': Decimal('0.20'),'atribut':"benefit"}, 
        {'id': 4, 'nama_kriteria': 'Harga', 'bobot_kriteria': Decimal('0.25'),'atribut':"cost"}, 
        {'id': 5, 'nama_kriteria': 'Usia', 'bobot_kriteria': Decimal('0.25'),'atribut':"benefit"}, 
        {'id': 6, 'nama_kriteria': 'Daya Konsumsi Pakan', 'bobot_kriteria': Decimal('0.15'),'atribut':"benefit"}
]

data_parameter = [
    {'id': 2, 'nama': '0-300', 'min': 0.0, 'max': 300.0, 'kriteria__id': 2, 'kriteria__nama_kriteria': 'Berat', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 4}, 
    {'id': 3, 'nama': '301-600', 'min': 301.0, 'max': 600.0, 'kriteria__id': 2, 'kriteria__nama_kriteria': 'Berat', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 5}, 
    {'id': 4, 'nama': '601-900', 'min': 601.0, 'max': 900.0, 'kriteria__id': 2, 'kriteria__nama_kriteria': 'Berat', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 6}, 
    {'id': 5, 'nama': '901-1200', 'min': 901.0, 'max': 1200.0, 'kriteria__id': 2, 'kriteria__nama_kriteria': 'Berat', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 7}, 
    {'id': 6, 'nama': '1201-1500', 'min': 1201.0, 'max': 1500.0, 'kriteria__id': 2, 'kriteria__nama_kriteria': 'Berat', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 8},
    
    {'id': 7, 'nama': '0-50', 'min': 0.0, 'max': 50.0, 'kriteria__id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 4}, 
    {'id': 8, 'nama': '51-100', 'min': 51.0, 'max': 100.0, 'kriteria__id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 5}, 
    {'id': 9, 'nama': '101-150', 'min': 101.0, 'max': 150.0, 'kriteria__id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 6}, 
    {'id': 10, 'nama': '151-200', 'min': 151.0, 'max': 200.0, 'kriteria__id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 7}, 
    {'id': 11, 'nama': '201-250', 'min': 201.0, 'max': 250.0, 'kriteria__id': 3, 'kriteria__nama_kriteria': 'Tinggi', 'kriteria__bobot_kriteria': Decimal('0.20'), 'nilai__id': 8}, 

    {'id': 12, 'nama': '< 10000000', 'min': 0.0, 'max': 10000000.0, 'kriteria__id': 4, 'kriteria__nama_kriteria': 'Harga', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 4}, 
    {'id': 13, 'nama': '10000000-20000000', 'min': 10000000.0, 'max': 20000000.0, 'kriteria__id': 4, 'kriteria__nama_kriteria': 'Harga', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 5},
    {'id': 14, 'nama': '20000000-35000000', 'min': 20000000.0, 'max': 35000000.0, 'kriteria__id': 4, 'kriteria__nama_kriteria': 'Harga', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 6}, 
    {'id': 15, 'nama': '35000000-50000000', 'min': 35000000.0, 'max': 50000000.0, 'kriteria__id': 4, 'kriteria__nama_kriteria': 'Harga', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 7}, 
    {'id': 16, 'nama': '>5000000', 'min': 50000001.0, 'max': 50000000.0, 'kriteria__id': 4, 'kriteria__nama_kriteria': 'Harga', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 8}, 
   
    {'id': 17, 'nama': '0-7', 'min': 0.0, 'max': 7.0, 'kriteria__id': 5, 'kriteria__nama_kriteria': 'Usia', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 4}, 
    {'id': 18, 'nama': '8-12', 'min': 8.0, 'max': 12.0, 'kriteria__id': 5, 'kriteria__nama_kriteria': 'Usia', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 5}, 
    {'id': 19, 'nama': '13-20', 'min': 13.0, 'max': 20.0, 'kriteria__id': 5, 'kriteria__nama_kriteria': 'Usia', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 6}, 
    {'id': 20, 'nama': '21-28', 'min': 21.0, 'max': 28.0, 'kriteria__id': 5, 'kriteria__nama_kriteria': 'Usia', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 7}, 
    {'id': 21, 'nama': '29-36', 'min': 29.0, 'max': 36.0, 'kriteria__id': 5, 'kriteria__nama_kriteria': 'Usia', 'kriteria__bobot_kriteria': Decimal('0.25'), 'nilai__id': 8}, 
   
    {'id': 22, 'nama': '0.5', 'min': 0.5, 'max': 0.0, 'kriteria__id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'kriteria__bobot_kriteria': Decimal('0.15'), 'nilai__id': 4}, 
    {'id': 23, 'nama': '1', 'min': 1.0, 'max': 0.0, 'kriteria__id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'kriteria__bobot_kriteria': Decimal('0.15'), 'nilai__id': 5},
    {'id': 24, 'nama': '2', 'min': 2.0, 'max': 0.0, 'kriteria__id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'kriteria__bobot_kriteria': Decimal('0.15'), 'nilai__id': 6},
    {'id': 25, 'nama': '3', 'min': 3.0, 'max': 0.0, 'kriteria__id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'kriteria__bobot_kriteria': Decimal('0.15'), 'nilai__id': 7},
    {'id': 26, 'nama': '>4', 'min': 4.0, 'max': 4.0, 'kriteria__id': 6, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'kriteria__bobot_kriteria': Decimal('0.15'), 'nilai__id': 8}]

def remove_whitespace(text):
    # Remove all whitespace characters (\s) using regular expression
    return re.sub(r'\s+', '', text)

class HasilTestCase(TestCase):
    # depan harus tambahkan test supaya unitnya jalan
    def test_get_unique_sapi(self):
        expected = [
           {'sapi_id': 1, 'nama_sapi': 'Sapi A'},
           {'sapi_id': 2, 'nama_sapi': 'Sapi B'},
           {'sapi_id': 3, 'nama_sapi': 'Sapi C'},
        ]
        actual = get_unik_sapi(data_kriteria_sapi)

        self.assertEqual(actual,expected)
    
    def test_matrix_keputusan(self):
        expected =  [
        {'id': 1, 'nilai': 1300.0, 'sapi_id': 1, 'kriteria_id': 2,'param_id':6, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8},
        {'id': 2, 'nilai': 200.0, 'sapi_id': 1, 'kriteria_id': 3,'param_id':10,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':7}, 
        {'id': 3, 'nilai': 60000000.0, 'sapi_id': 1, 'kriteria_id': 4,'param_id':16,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
        {'id': 4, 'nilai': 34.0, 'sapi_id': 1, 'kriteria_id': 5,'param_id':21,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
        {'id': 5, 'nilai': 4.0, 'sapi_id': 1, 'kriteria_id': 6,'param_id':26,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
       
        {'id': 6, 'nilai': 800.0, 'sapi_id': 2, 'kriteria_id': 2,'param_id':4,  'kriteria__nama_kriteria': 'Berat', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':6}, 
        {'id': 7, 'nilai': 150.0, 'sapi_id': 2, 'kriteria_id': 3,'param_id':9,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':6}, 
        {'id': 8, 'nilai': 40000000.0, 'sapi_id': 2, 'kriteria_id': 4,'param_id':15,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':7}, 
        {'id': 9, 'nilai': 21.0, 'sapi_id': 2, 'kriteria_id': 5,'param_id':20,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':7}, 
        {'id': 10, 'nilai': 4.0, 'sapi_id': 2, 'kriteria_id': 6,'param_id':26,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':8}, 
        
        {'id': 11, 'nilai': 900.0, 'sapi_id': 3, 'kriteria_id': 2,'param_id':4,  'kriteria__nama_kriteria': 'Berat', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':6}, 
        {'id': 12, 'nilai': 160.0, 'sapi_id': 3, 'kriteria_id': 3,'param_id':10,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 13, 'nilai': 50000000.0, 'sapi_id': 3, 'kriteria_id': 4,'param_id':15,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 14, 'nilai': 25.0, 'sapi_id': 3, 'kriteria_id': 5,'param_id':20,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 15, 'nilai': 3.0, 'sapi_id': 3, 'kriteria_id': 6,'param_id':25,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        ]

        actual = get_parameter_by_id(data_kriteria_sapi,data_parameter)   
       
        self.assertEqual(actual,expected)

    def test_count_normalisasi(self):
        keputusan =  [
        {'id': 1, 'nilai': 1300.0, 'sapi_id': 1, 'kriteria_id': 2,'param_id':6, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8},
        {'id': 2, 'nilai': 200.0, 'sapi_id': 1, 'kriteria_id': 3,'param_id':10,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':7}, 
        {'id': 3, 'nilai': 60000000.0, 'sapi_id': 1, 'kriteria_id': 4,'param_id':16,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
        {'id': 4, 'nilai': 34.0, 'sapi_id': 1, 'kriteria_id': 5,'param_id':21,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
        {'id': 5, 'nilai': 4.0, 'sapi_id': 1, 'kriteria_id': 6,'param_id':26,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A','nilai_id':8}, 
       
        {'id': 6, 'nilai': 800.0, 'sapi_id': 2, 'kriteria_id': 2,'param_id':4,  'kriteria__nama_kriteria': 'Berat', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':6}, 
        {'id': 7, 'nilai': 150.0, 'sapi_id': 2, 'kriteria_id': 3,'param_id':9,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':6}, 
        {'id': 8, 'nilai': 40000000.0, 'sapi_id': 2, 'kriteria_id': 4,'param_id':15,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':7}, 
        {'id': 9, 'nilai': 21.0, 'sapi_id': 2, 'kriteria_id': 5,'param_id':20,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':7}, 
        {'id': 10, 'nilai': 4.0, 'sapi_id': 2, 'kriteria_id': 6,'param_id':26,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B','nilai_id':8}, 
        
        {'id': 11, 'nilai': 900.0, 'sapi_id': 3, 'kriteria_id': 2,'param_id':4,  'kriteria__nama_kriteria': 'Berat', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':6}, 
        {'id': 12, 'nilai': 160.0, 'sapi_id': 3, 'kriteria_id': 3,'param_id':10,  'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 13, 'nilai': 50000000.0, 'sapi_id': 3, 'kriteria_id': 4,'param_id':15,  'kriteria__nama_kriteria': 'Harga', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 14, 'nilai': 25.0, 'sapi_id': 3, 'kriteria_id': 5,'param_id':20,  'kriteria__nama_kriteria': 'Usia', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        {'id': 15, 'nilai': 3.0, 'sapi_id': 3, 'kriteria_id': 6,'param_id':25,  'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C','nilai_id':7}, 
        ]

        actual = normalisasi_count(keputusan,data_kriteria,data_nilai)
        expected = [
            {'id': 1, 'nilai': 1300.0, 'sapi_id': 1, 'kriteria_id': 2, 'param_id': 6, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            {'id': 2, 'nilai': 200.0, 'sapi_id': 1, 'kriteria_id': 3, 'param_id': 10, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 3, 'nilai': 60000000.0, 'sapi_id': 1, 'kriteria_id': 4, 'param_id': 16, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 0.8}, 
            {'id': 4, 'nilai': 34.0, 'sapi_id': 1, 'kriteria_id': 5, 'param_id': 21, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            {'id': 5, 'nilai': 4.0, 'sapi_id': 1, 'kriteria_id': 6, 'param_id': 26, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            
            {'id': 6, 'nilai': 800.0, 'sapi_id': 2, 'kriteria_id': 2, 'param_id': 4, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.6}, 
            {'id': 7, 'nilai': 150.0, 'sapi_id': 2, 'kriteria_id': 3, 'param_id': 9, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.75}, 
            {'id': 8, 'nilai': 40000000.0, 'sapi_id': 2, 'kriteria_id': 4, 'param_id': 15, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 9, 'nilai': 21.0, 'sapi_id': 2, 'kriteria_id': 5, 'param_id': 20, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}, 
            {'id': 10, 'nilai': 4.0, 'sapi_id': 2, 'kriteria_id': 6, 'param_id': 26, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            
            {'id': 11, 'nilai': 900.0, 'sapi_id': 3, 'kriteria_id': 2, 'param_id': 4, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.6}, 
            {'id': 12, 'nilai': 160.0, 'sapi_id': 3, 'kriteria_id': 3, 'param_id': 10, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 13, 'nilai': 50000000.0, 'sapi_id': 3, 'kriteria_id': 4, 'param_id': 15, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0},
            {'id': 14, 'nilai': 25.0, 'sapi_id': 3, 'kriteria_id': 5, 'param_id': 20, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}, 
            {'id': 15, 'nilai': 3.0, 'sapi_id': 3, 'kriteria_id': 6, 'param_id': 25, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}]

        self.assertEqual(actual,expected)

    def test_search_ranking(self):
        data = [
            {'id': 1, 'nilai': 1300.0, 'sapi_id': 1, 'kriteria_id': 2, 'param_id': 6, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            {'id': 2, 'nilai': 200.0, 'sapi_id': 1, 'kriteria_id': 3, 'param_id': 10, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 3, 'nilai': 60000000.0, 'sapi_id': 1, 'kriteria_id': 4, 'param_id': 16, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 0.8}, 
            {'id': 4, 'nilai': 34.0, 'sapi_id': 1, 'kriteria_id': 5, 'param_id': 21, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            {'id': 5, 'nilai': 4.0, 'sapi_id': 1, 'kriteria_id': 6, 'param_id': 26, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            
            {'id': 6, 'nilai': 800.0, 'sapi_id': 2, 'kriteria_id': 2, 'param_id': 4, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.6}, 
            {'id': 7, 'nilai': 150.0, 'sapi_id': 2, 'kriteria_id': 3, 'param_id': 9, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.75}, 
            {'id': 8, 'nilai': 40000000.0, 'sapi_id': 2, 'kriteria_id': 4, 'param_id': 15, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 9, 'nilai': 21.0, 'sapi_id': 2, 'kriteria_id': 5, 'param_id': 20, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}, 
            {'id': 10, 'nilai': 4.0, 'sapi_id': 2, 'kriteria_id': 6, 'param_id': 26, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B', 'nilai_id': 8, 'bobot': 5, 'nilai_norm': 1.0}, 
            
            {'id': 11, 'nilai': 900.0, 'sapi_id': 3, 'kriteria_id': 2, 'param_id': 4, 'kriteria__nama_kriteria': 'Berat', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 6, 'bobot': 3, 'nilai_norm': 0.6}, 
            {'id': 12, 'nilai': 160.0, 'sapi_id': 3, 'kriteria_id': 3, 'param_id': 10, 'kriteria__nama_kriteria': 'Tinggi', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0}, 
            {'id': 13, 'nilai': 50000000.0, 'sapi_id': 3, 'kriteria_id': 4, 'param_id': 15, 'kriteria__nama_kriteria': 'Harga', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 1.0},
            {'id': 14, 'nilai': 25.0, 'sapi_id': 3, 'kriteria_id': 5, 'param_id': 20, 'kriteria__nama_kriteria': 'Usia', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}, 
            {'id': 15, 'nilai': 3.0, 'sapi_id': 3, 'kriteria_id': 6, 'param_id': 25, 'kriteria__nama_kriteria': 'Daya Konsumsi Pakan', 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C', 'nilai_id': 7, 'bobot': 4, 'nilai_norm': 0.8}]
        
        actual = get_ranking(data,data_kriteria)
        expected = [
            {'sapi_id': 1, 'nama_sapi': 'Sapi A', 'nilai': 1.0}, 
            {'sapi_id': 3, 'nama_sapi': 'Sapi C', 'nilai': 0.89}, 
            {'sapi_id': 2, 'nama_sapi': 'Sapi B', 'nilai': 0.87}]
        self.assertEqual(actual,expected)

    def test_create_report_excel(self):
        self.maxDiff = None
        data = {'custom_labels': {
            'ranking': 'Ranking', 'nama_sapi': 'Nama Sapi', 'nilai': 'Nilai'}, 
            'data': [
                {'id': 7, 'nilai_norm': 0.9, 'sapi__id': 1, 'sapi__nama_sapi': 'Sapi A'}, 
                {'id': 8, 'nilai_norm': 0.7700000000000001, 'sapi__id': 3, 'sapi__nama_sapi': 'Sapi C'}, 
                {'id': 9, 'nilai_norm': 0.745, 'sapi__id': 2, 'sapi__nama_sapi': 'Sapi B'}, 
                {'id': 10, 'nilai_norm': 0.565, 'sapi__id': 4, 'sapi__nama_sapi': 'Sapi D'}, 
                {'id': 11, 'nilai_norm': 0.53, 'sapi__id': 5, 'sapi__nama_sapi': 'Sapi E'}
            ]
        }

        actual = create_html_excel(data)
        expected = """
        <table>
        <tr>
        <th>Ranking</th>
        <th>Nama Sapi</th>
        <th>Nilai</th>
        <tr/>
        <tr>
        <td>1</td>
        <td>Sapi A</td>
        <td>0.9</td>
        </tr>
        <tr>
        <td>2</td>
        <td>Sapi C</td>
        <td>0.7700000000000001</td>
        </tr>
        <tr>
        <td>3</td>
        <td>Sapi B</td>
        <td>0.745</td>
        </tr>
        <tr>
        <td>4</td>
        <td>Sapi D</td>
        <td>0.565</td>
        </tr>
        <tr>
        <td>5</td>
        <td>Sapi E</td>
        <td>0.53</td>
        </tr>
        </table>
        """
        self.assertEqual(remove_whitespace(actual),remove_whitespace(expected))
    

        
