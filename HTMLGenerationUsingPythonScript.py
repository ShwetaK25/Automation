
href_doc = r"./ABC.SP.800-171r1-20180220.pdf#page=25"
href_feature = r"./ABC.feature#text=shweta"
href_excel = r"./ABC_Requirements.xlsx#MY POLICY!C9"

str1 = '''
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <table border="1">
            <tr>
                <td>Policy document</td>
                <td>Excel</td>
                <td>Feature file</td>
            </tr>
            <tr>
               <td><a href = '''+href_doc+'''>doc</td>
               <td><a href = '''+href_feature+'''>Feature file</td>
               <td><a href = '''+href_excel+''' target="_blank">Excel file</td>
               
            </tr>

        </table>
    </body>
</html>
'''
hs = open(r"C:\Shweta\RA\myhtml.html", 'w')
hs.write(str1)
hs.close()
