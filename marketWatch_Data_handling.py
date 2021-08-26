import pandas as pd
import os
import matplotlib.pyplot as plt
################################################ End of Importing ################################


def keydata_handling(open_Data,dayRange_Data,week52Range_Data): # Key Data Conversion to Dataframe
    keydata_df = pd.DataFrame(columns=['Open', 'Day_Range','52_Weeks_Range'])
    keydata_df.loc[0] = [open_Data,dayRange_Data,week52Range_Data]
    print("Key Data:\n")
    print(keydata_df)


def overview_performance_data_handling(performance_table_row_data_list):
    preprocessed_list = []
    for items in performance_table_row_data_list:
        preprocessed_list += (items.splitlines())
    row_data = []
    column_data = []
    for item in range(0, len(preprocessed_list)):
        if item % 2 == 1:
            row_data.append(preprocessed_list[item])
        else:
            column_data.append(preprocessed_list[item])
    performance_df = pd.DataFrame(columns=column_data)
    data_to_append = row_data
    performance_df_length = len(performance_df)
    performance_df.loc[performance_df_length] = data_to_append
    print("\nPerformance Data:\n")
    print(performance_df)

def overview_performer_data_handling(performer_table_header_data_list,performer_name_list,
                                     performer_last_list, performer_change_list,performer_change_percent_list,reason):
    top_performer_df = ''
    bottom_performer_df = ''
    if reason == "Top Performer":
        top_performer_df = pd.DataFrame(list(zip(performer_name_list, performer_last_list, performer_change_list,
                                                 performer_change_percent_list)), columns=performer_table_header_data_list)
        print("\nTop Performer:\n")
        print(top_performer_df)

    if reason == "Bottom Performer":
        bottom_performer_df = pd.DataFrame(list(zip(performer_name_list, performer_last_list, performer_change_list,
                                                 performer_change_percent_list)), columns=performer_table_header_data_list)
        print("\nBottom Performer:\n")
        print(bottom_performer_df)

def historical_quotes_data_handling():
    main_path = os.getcwd()
    download_folder_name = 'marketWatch_Downloads'
    download_path = main_path + '\\' + download_folder_name
    download_list = os.listdir(download_path)
    csv_file_path = ''
    for item in download_list:
        if '.csv' in item:
            print("\nCSV File found!.Converting to dataframe\n")
            csv_file_path = str(os.path.join(download_path, item))
    historical_quotes_df = pd.read_csv(csv_file_path)

    print(historical_quotes_df)
    print('Plotting the data')
    try:  # For row data with comma and decimal point
        historical_quotes_df['Date'] = pd.to_datetime(historical_quotes_df['Date'])
        historical_quotes_df['Open'] = historical_quotes_df['Open'].str.replace(',', '').astype(float)
        historical_quotes_df['High'] = historical_quotes_df['High'].str.replace(',', '').astype(float)
        historical_quotes_df['Low'] = historical_quotes_df['Low'].str.replace(',', '').astype(float)
        historical_quotes_df['Close'] = historical_quotes_df['Close'].str.replace(',', '').astype(float)

    except:
        pass

    try:  # For row data with decimal point
        historical_quotes_df['Date'] = pd.to_datetime(historical_quotes_df['Date'])
        historical_quotes_df['Open'] = historical_quotes_df['Open'].astype(float)
        historical_quotes_df['High'] = historical_quotes_df['High'].astype(float)
        historical_quotes_df['Low'] = historical_quotes_df['Low'].astype(float)
        historical_quotes_df['Close'] = historical_quotes_df['Close'].astype(float)

    except:
        pass

    try:  # For row data with percentage and decimal point

        historical_quotes_df['Date'] = pd.to_datetime(historical_quotes_df['Date'])
        historical_quotes_df['Open'] = historical_quotes_df['Open'].str.replace('%', '').astype(float)
        historical_quotes_df['High'] = historical_quotes_df['High'].str.replace('%', '').astype(float)
        historical_quotes_df['Low'] = historical_quotes_df['Low'].str.replace('%', '').astype(float)
        historical_quotes_df['Close'] = historical_quotes_df['Close'].str.replace('%', '').astype(float)
        print("All the values except Date are in percentage. For plotting needed to remove that")

    except:
        pass

    historical_quotes_df[['Date', 'Open', 'High', 'Low', 'Close']].plot(x="Date", kind="bar")

    plt.show()



def future_contract_data_handling(recent_contracts_table_header_list,recent_contracts_table_contracts_name_list,recent_contracts_table_contracts_last_list,
                                      recent_contracts_table_contracts_change_list,recent_contracts_table_contracts_open_list,
                                      recent_contracts_table_contracts_high_list,recent_contracts_table_contracts_low_list,recent_contracts_table_contracts_date_list):
    # This is for contract data handling only happens in some cases like future contracts and futures
    recent_contracts_df = ''

    recent_contracts_df = pd.DataFrame(list(zip(recent_contracts_table_contracts_name_list, recent_contracts_table_contracts_last_list,recent_contracts_table_contracts_change_list,
                                                recent_contracts_table_contracts_open_list,recent_contracts_table_contracts_high_list,recent_contracts_table_contracts_low_list,
                                                recent_contracts_table_contracts_date_list)), columns=recent_contracts_table_header_list)

    print(recent_contracts_df)
