import pandas as pd
test= pd.read_csv('C:\\Users\\FX505DT\\Desktop\\my1.csv')
#print(test)

if {'Open','Close'}.issubset(test.columns):
    test['Change'] = (test['Close'] - test['Open'])/test['Open']

print(test)

test.to_csv('C:\\Users\\FX505DT\\Desktop\\output.csv')