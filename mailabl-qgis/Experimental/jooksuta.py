# moodusta kinnistu ümber buffer ja kanna joonisele 
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\KinnistuBuffer.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\KinnistuBuffer.py', 'exec')
    exec(code, globals())

# vali kanalisatsiooni torud    
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\selecting_K.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\Selecting_K.py', 'exec')
    exec(code, globals())

# Vali survekanalisatsiooni torud
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\selecting_S.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\Selecting_S.py', 'exec')
    exec(code, globals())

#Eemalda ajutine kanalisatsiooni kiht
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\EemaldaAjutine.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Selecting\EemaldaAjutine.py', 'exec')
    exec(code, globals())

with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\PuhastaTöölaud.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\PuhastaTöölaud.py', 'exec')
    exec(code, globals())

with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\buffer.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\buffer.py', 'exec')
    exec(code, globals())

with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\intersect_v1.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\intersect_v1.py', 'exec')
    exec(code, globals())
    
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Liida.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Liida.py', 'exec')
    exec(code, globals())
    
with open(r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Ühenda.py') as f:
    code = compile(f.read(), r'C:\Users\Admin\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts\Ühenda.py', 'exec')
    exec(code, globals())