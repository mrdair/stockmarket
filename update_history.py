import databse_tools
import general_tools

names = databse_tools.names_of_stocks()

url = 'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i='  # + id
count = 0
failed_list = []

for token in names.keys():
    try:
        general_tools.download(str(url+names[token]), str('database/history/' + token + '.csv'))
        count += 1
        print(str(count) + " of " + str(len(names)))
    except:
        try:
            general_tools.download(str(url + token), str('database/history/' + token + '.csv'))
            count += 1
            print(str(count) + " of " + str(len(names)))
        except:
            failed_list.append(token)
            print("failed")


print('failed list : ' + str(failed_list))

print('done')
