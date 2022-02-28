import json
import pandas as pd

def lambda_handler(event, context):
    with open("event.json") as f:
        data = json.load(f)
    
    print(json.dumps(data, indent=5))   # make the indent=5 likewise to resolve the error.
    print("\n")
    
    
    df_for_values = pd.DataFrame.from_dict(data, orient = "columns")
    print(df_for_values)
    print("\n\n")
    
    split_jsonn_to_extract_data = json.loads(df_for_values.to_json(orient = "split", index = False))
    print(json.dumps(split_jsonn_to_extract_data, indent=5))
    print("\n")
    
    
    valueArr1 = []
    for i in split_jsonn_to_extract_data:
        if i == 'data':
            for j in split_jsonn_to_extract_data[i]:
                for k in j:
                    valueArr1.append(k)
    
    # print(valueArr1)
    # print("\n\n")
    
    valueArr2 = []
    for i in valueArr1:
        if i != None:
            valueArr2.append(i)
            
    print(valueArr2)
    print("\n\n")
    
    
    
    df_for_keys = pd.DataFrame.from_dict(data, orient = "index")
    print(df_for_keys)
    print("\n\n")
    
    # print(df.iloc[3].to_numpy())
    # print(dftt.index.to_numpy())
    keyArr = []
    for i in df_for_keys.index.to_numpy():
        keyArr.append(i)
    
    print(keyArr)
    print("\n")
    
    
    Dict = {}
    for keys in keyArr:
        for values in valueArr2:
            Dict[keys] = [values]
            valueArr2.remove(values)    # so that next time when keys iterate it can get updated with the next values in the valueArr2 ARRAY.
            break
    
    print(Dict)
    print("\n\n")
    
    
    print(json.dumps(Dict, indent=5))
    print("\n")
    
    df_of_new_Dict = pd.DataFrame.from_dict(Dict, orient = "columns")
    print(df_of_new_Dict)
    print("\n\n")

    
    
    #with open("test.csv", "w") as fout:
    
    res = df_of_new_Dict.to_csv(sep = ",", index = False)
    print(res)
    
    print("\n")
    
    return {
        'statusCode': 200,
        'body': 'Success !'
    }