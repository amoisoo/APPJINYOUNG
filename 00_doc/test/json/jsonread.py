

import json




getDATA = json.load( open( 'data.json', encoding='utf-8' ) )


print(getDATA['id'] )
print(getDATA['address'] )

for i in getDATA['address']:
    print(i , ' : ', getDATA['address'][i])
