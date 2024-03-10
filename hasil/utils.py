def get_unik_sapi(sapi):
    new_sapi = []

    for entry in sapi:
        sapi_id = entry['sapi_id']
        sapi_nama = entry['sapi__nama_sapi']

        if not any(d['sapi_id'] == sapi_id for d in new_sapi):
            new_sapi.append({'sapi_id':sapi_id,'nama_sapi':sapi_nama})
    
    return new_sapi

# balikannya json
def filter_by_kriteria(obj,parameters):
    for param in parameters:
        if(obj["kriteria_id"] == param["kriteria__id"]):
            if obj["nilai"] >= param["min"] and obj["nilai"] <= param["max"]:
                obj["param_id"] = param["id"]
                obj["nilai_id"] = param["nilai__id"]
            elif obj["nilai"] >= param["min"] and obj["nilai"] >= param["max"]:
                obj["param_id"] = param["id"]
                obj["nilai_id"] = param["nilai__id"]
            elif obj["nilai"] == param["min"] and obj["nilai"] <= param["max"]:
                obj["param_id"] = param["id"]
                obj["nilai_id"] = param["nilai__id"]    
    return obj

# tentukan nilai parameter berdasarkan id kriteria
# jalankan unit test per app
#  python3 manage.py test hasil.tests
def get_parameter_by_id(data_kriteria_sapi,data_parameter):
    new_param = []
    for obj in data_kriteria_sapi:
        param = filter_by_kriteria(obj,data_parameter)
        new_param.append(param)
    return new_param

# mengambil nilai bobot
def filter_nilai_by_id(data,data_nilai):
    for nilai in data_nilai:
        if(data["nilai_id"] == nilai["id"]):
            data["bobot"] = nilai["bobot"]
    
    return data

# fungsi unit cara min max
def define_max_min(kriteria,matriks):
    array_max_min = []
    for mat in matriks:
        if(kriteria["id"] == mat["kriteria_id"]):
            array_max_min.append(mat)
    
    # maxs = max(array_max_min, key=lambda x: x["bobot"])
    # print(maxs)
    json_kriteria = {}
    if(kriteria["atribut"] == "benefit"):
        json_kriteria["nilai"] = max(array_max_min, key=lambda x: x["bobot"])["bobot"]
        json_kriteria["status"] = "benefit"
    else:
        json_kriteria["nilai"] = min(array_max_min, key=lambda x: x["bobot"])["bobot"]
        json_kriteria["status"] = "cost"
    
    json_kriteria["nama_kriteria"] = kriteria["nama_kriteria"]
    json_kriteria["kriteria_id"] = kriteria["id"]

    return json_kriteria

# hitung max min
def count_max_min(mat,max_min_val):
    for val in max_min_val:
        if(mat["kriteria_id"] == val["kriteria_id"]):
            if(val["status"] == "benefit"):
                nilai = round(mat["bobot"] / val["nilai"],2)
            elif(val["status"] == "cost"):
                nilai = round(val["nilai"]/ mat["bobot"],2)
           
    
    return nilai
    

def normalisasi_count(keputusan,data_kriteria,data_nilai):
    # ambil nilai/bobot
    new_matriks = []
    for data in keputusan:
        filtered_nilai = filter_nilai_by_id(data,data_nilai)
        new_matriks.append(filtered_nilai)

    # mencari nilai max/min
    max_min_val = []
    for kriteria in data_kriteria:
        mapped_max_min = define_max_min(kriteria,new_matriks)
        max_min_val.append(mapped_max_min)

    # hitung nilai max_min dicocoki dengan kriteria_id
    for mat in new_matriks:
        count_val = count_max_min(mat,max_min_val)
        mat["nilai_norm"] = count_val
    
    return new_matriks


# mengkalikan nilai normalisasi dengan bobot
def kali_bobot(sapi,keputusan,kriteria):
    new_sapi = []
    # kelompokkan per sapi
    for dt_kep in keputusan:
        if(sapi["sapi_id"] == dt_kep["sapi_id"]):
            new_sapi.append(dt_kep)
    
    jumlah = 0
    # kalikan normalisasi dan bobot
    for sp in new_sapi:
        for kt in kriteria:
            if(sp["kriteria_id"] == kt["id"]):
                jumlah += float(sp["nilai_norm"])* float(kt["bobot_kriteria"])
    
    return {'sapi_id':sapi["sapi_id"],'nama_sapi':sapi["nama_sapi"],'nilai':jumlah}
   

# mencari ranking
def get_ranking(keputusan,data_kriteria):
    unique_sapi = get_unik_sapi(keputusan)
    new_rank = []
    
    for sapi in unique_sapi:
        hasil = kali_bobot(sapi,keputusan,data_kriteria)
        new_rank.append(hasil)

    return sorted(new_rank, key=lambda x: x["nilai"], reverse=True)

# membuat html to excel
def create_html_excel(data):
    # looping object label
    html = """<table>\n<tr>\n"""

    for key, value in data["custom_labels"].items():
      html += f'<th>{value}</th>\n'

    html += '<tr/>\n'


    # isikan nilai ke dalam baris
    for index, dt in enumerate(data["data"]):
        html += f'<tr>\n<td>{index+1}</td>\n<td>{dt["sapi__nama_sapi"]}</td>\n<td>{dt["nilai_norm"]}</td>\n</tr>\n'

    html += '</table>'
    return html
   
        
