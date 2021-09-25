import databse_tools
import general_tools

names = databse_tools.names_of_stocks()

url = 'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i='  # + id
count = 0
failed_list = []

for token in names.keys():
    try:
        general_tools.download(str(url+names[token]), str('database/transfer/' + token + '.aspx'))
        count += 1
        print(str(count) + " of " + str(len(names)))
    except:
        try:
            general_tools.download(str(url + token), str('database/transfer/' + token + '.aspx'))
            count += 1
            print(str(count) + " of " + str(len(names)))
        except:
            failed_list.append(token)
            print("failed")


print('failed list : ' + str(failed_list))

print('done')
