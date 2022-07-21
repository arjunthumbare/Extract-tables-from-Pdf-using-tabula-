import tabula
import os

tables = tabula.read_pdf(r"C:/Users/ARAJANTH/Downloads/World.pdf", pages="all")
print("those are table", tables,"\n")
folder_name = "C:/Users/ARAJANTH/Pictures/tables"
print(folder_name )

if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
print (tables )



#for table in enumerate(tables):
    #print('this is i ',i)
    #print("this is tablr ",table )
    #table.to_excel(os.path.join(folder_name, f"tablebbbb.xlsx"))
tabula.convert_into("C:/Users/ARAJANTH/Downloads/World.pdf", "C:/Users/ARAJANTH/Pictures/tables/output.csv", output_format="csv", pages="all")

    

