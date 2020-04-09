import google.cloud.bigquery


client = bigquery.Client(project=os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS'))


def get_table_schema(client: biquery.Client, project_id: str, dataset: str, table_name: str) -> bigquery.schema.SchemaFields:
    '''
    Fetch the SchemaFields of a BigQuery table
    '''
    ds_ref = client.dataset(dataset)
    tbl_ref = ds_ref.table(table_name)
    tbl = client.get_table(tbl_ref)
    return tbl.schema
