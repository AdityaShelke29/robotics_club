import RigolWFM.wfm as rigol

filename = 'wfm/DS2072A-1.wfm'
scope = 'DS2072A'

scope_data = rigol.Wfm.from_file(filename, scope)

description = scope_data.describe()
print(description)

s = scope_data.csv()

# just show the first few entries
rows = s.split('\n')
for i in range(5):
    print(rows[i])