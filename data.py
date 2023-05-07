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


def gen_pies(client_id):
    test_df = trans_df.copy()
    client_df = test_df.loc[test_df['id_cliente'] == client_id].copy()
    client_df.groupby(['id_cliente', 'fecha_transaccion'])['monto_transaccion'].sum()
    porcentaje_list = []

    client_per_df = test_df.loc[test_df['id_cliente'] == client_id].copy()
    client_per_df.groupby(['id_cliente', 'fecha_transaccion', 'mcc_nombre'])['monto_transaccion'].count()

    client_new_df = test_df.loc[test_df['id_cliente'] == client_id].copy()

    total_ser = client_df.groupby(['id_cliente', 'fecha_transaccion'])['monto_transaccion'].sum()
    grouped_ser = client_new_df.groupby(['id_cliente', 'fecha_transaccion', 'mcc_nombre'])['monto_transaccion'].sum()
    grouped_df = grouped_ser.reset_index()
    grouped_df.head()

    for index, row in grouped_df.iterrows():
        porcentaje = (row['monto_transaccion'] / total_ser[client_id][row['fecha_transaccion']]) * 100
        porcentaje_list.append(porcentaje)

    data = {'porcentaje': porcentaje_list}
    porcentaje = pd.DataFrame(data)

    grouped_df['per'] = porcentaje

    pies_dict = {}
    for index, row in grouped_df.iterrows():
        if not pies_dict.get(row['fecha_transaccion']):
            pies_dict[row['fecha_transaccion']] = {"mcc": [row['mcc_nombre']], "count": [row['per']]}
        else:
            pies_dict[row['fecha_transaccion']]["mcc"].append(row['mcc_nombre'])
            pies_dict[row['fecha_transaccion']]["count"].append(row['per'])

    return pies_dict


def gen_savings(client_id):
    test_per_df = trans_df.copy()
    client_per_df = test_per_df.loc[test_per_df['id_cliente'] == client_id].copy()
    savings = client_per_df.groupby(['id_cliente', 'fecha_transaccion', 'mcc_nombre'])['monto_transaccion'].agg(['sum', 'count']).reset_index()

    savings_dict = {}
    for index, row in savings.iterrows():
        if not savings_dict.get(row['fecha_transaccion']):
            savings_dict[row['fecha_transaccion']] = {}
        savings_dict[row['fecha_transaccion']][row['mcc_nombre']] = {'monto': row['sum'], 'transaccion': row['count']}
    return savings_dict





# def new_cv():
#     trans_df.loc[:, 'fecha_transaccion'] = pd.to_datetime(trans_df['fecha_transaccion'])
#     trans_df.loc[:, 'fecha_transaccion'] = trans_df.loc[:, 'fecha_transaccion'].dt.month
#     trans_df.to_csv('new_trans.csv', index=False)
#
#
# new_cv()



