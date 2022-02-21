"""
from sample: soil_template_to_map.xlsx
Take soil data from excel and bring them into a dict/geojson like this:

{ "geometry":{"coordinates":[lat,long],"type":"Point"},
              "properties":{
                            "P":a,
                            "K":b,
                            "Mg":c,
                            "Ca":d,
                            "S":e,
                            "pH":f,
                            "CTC":g,
                            "V%":h,
                            "EC":i
                            "texture":j
                            },"type":"Feature"
}

"""
import openpyxl


# pass data from excel sheets to lists,

def tab_opener(your_excel_name):
    '''

    :param your_excel_name: file to be open
    :return: tab to be worked on
    '''

    analise = openpyxl.load_workbook(your_excel_name)
    name_tab = analise.sheetnames[0]
    tab_of_interest = analise[name_tab]

    return tab_of_interest


def tab_values_in_lists(tab_of_interest):
    """

    :param tab_of_interest: sheet with all the values
    :return: tabela = list of lists with each row's values
    comment: the set size of sheet is from cell a1 to cell zz100 (5200 values, should be enough for soil analysis)
    """
    tabela = []
    for row in tab_of_interest['a1:zz100']:  # search a big enough zone
        row_list = []  # list of column from each row
        for column in row:
            if column.value:  # takes off empty cell
                try:
                    row_list += [float(column.value)]  # add num value to row_list line by line, avoid numbers as str
                except ValueError:  # if the value is actually a str (like soil texture): stays like this
                    row_list += [column.value]
        if not row_list:  # if empty row: breaks = end of the tab
            break
        tabela += [row_list]
    return tabela


# set header to know what properties to put in dictionnary

def find_header(tab_list):
    """

    :param tab_list: list of lines of the document
    :return: properties to put in dictionary (analysis properties)
    """
    header = []
    for row_values_list in tab_list:
        for value in row_values_list:
            if value == 'Lat' or value == 'lat' or value == 'latitude' or value == 'Latitude':
                header = row_values_list
    return header


def clean_tab_list(tab_list_to_clean):
    """
       Takes off rows that are not analysis values
    """
    tab_cleaned = []
    for list1 in tab_list_to_clean:
        try:
            list1[0] = float(list1[0])
            tab_cleaned += [list1]
        except ValueError:
            list1 = []

    return tab_cleaned


# create dict compatible geojson form properties and raw data

def dict_geojson_creator(tab_values_of_analysis, header):
    '''

    :param tab_values_of_analysis: raw values corresponding to properties
    :param header: properties name
    :return: a list of dict {"geometry": {"coordinates": [lat, long], "type": "Point"},
                                   "properties": dico, "type": "Feature"
                                   }
    '''
    list_analysis_all_points = []
    for list_of_val in tab_values_of_analysis:
        lat = list_of_val[0]
        long = list_of_val[1]
        dico = {}
        for i in range(2, len(header)):
            dico[header[i]] = list_of_val[i]
        dict_analysis_one_point = {"geometry": {"coordinates": [lat, long], "type": "Point"},
                                   "properties": dico, "type": "Feature"
                                   }
        list_analysis_all_points.append(dict_analysis_one_point)

    return list_analysis_all_points


# excel_name = input('Analyse file path:')  # in this case :
excel_name = 'soil_template_to_map.xlsx'
tab_of_interest = tab_opener(excel_name)
tab_list = tab_values_in_lists(tab_of_interest)
header = find_header(tab_list)  # name of the properties in the tab (same line as lat, long)
tab_values_of_analysis = clean_tab_list(tab_list)  # raw datas (actual values)

# now we have header (properties on the file) and all the values (property index = value index).
# we must create a geojson ready file

print(dict_geojson_creator(tab_values_of_analysis, header))
