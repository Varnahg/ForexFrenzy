### Main functions repository for the Forex Frenzy project
# forexfrenzy/functions.py

from django.apps import apps

def get_table_data(table_name, columns, id=None):
    """
    Retrieve specific columns from a specific table in the db2.sqlite3 database.

    :param table_name: Name of the table (model) to query.
    :param columns: List of columns to retrieve.
    :param id: Optional id or list of ids to filter the rows.
    :return: Queryset with the specified columns.
    """
    # Get the model class from the table name
    model = apps.get_model('forexfrenzy', table_name)

    # Query the database for the specified columns
    if id is not None:
        if isinstance(id, list):
            data = model.objects.using('default').filter(id__in=id).values(*columns)
        else:
            data = model.objects.using('default').filter(id=id).values(*columns)
    else:
        data = model.objects.using('default').values(*columns)

    return data