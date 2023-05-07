import pandas as pd

trans_df = pd.read_csv('new_trans.csv')


def gen_totals(client_id):
    test_df = trans_df.copy()
    client_df = test_df.loc[test_df['id_cliente'] == client_id].copy()
    # client_df.loc[:, 'fecha_transaccion'] = pd.to_datetime(client_df['fecha_transaccion'])
    # client_df.loc[:, 'fecha_transaccion'] = client_df.loc[:, 'fecha_transaccion'].dt.month
    totals = client_df.groupby(['id_cliente', 'fecha_transaccion'])['monto_transaccion'].sum()
    totals_dict = {}
    for index, value in totals.items():
        totals_dict[index[1]] = value
    return totals_dict


def gen_histograms(client_id):
    test_new_df = trans_df.copy()
    client_new_df = test_new_df.loc[test_new_df['id_cliente'] == client_id].copy()
    # client_new_df.loc[:, 'fecha_transaccion'] = pd.to_datetime(client_new_df['fecha_transaccion'])
    # client_new_df.loc[:, 'fecha_transaccion'] = client_new_df.loc[:, 'fecha_transaccion'].dt.month
    histograms = client_new_df.groupby(['id_cliente', 'fecha_transaccion', 'mcc_nombre'])['monto_transaccion'].count()
    histograms_dict = {}
    for index, value in histograms.items():
        if not histograms_dict.get(index[1]):
            histograms_dict[index[1]] = {"mcc": [index[2]], "count": [value]}
        else:
            histograms_dict[index[1]]["mcc"].append(index[2])
            histograms_dict[index[1]]["count"].append(value)
    return histograms_dict


# def new_cv():
#     trans_df.loc[:, 'fecha_transaccion'] = pd.to_datetime(trans_df['fecha_transaccion'])
#     trans_df.loc[:, 'fecha_transaccion'] = trans_df.loc[:, 'fecha_transaccion'].dt.month
#     trans_df.to_csv('new_trans.csv', index=False)
#
#
# new_cv()