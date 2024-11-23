### Main functions repository for the Forex Frenzy project
# forexfrenzy/functions.py

from django.apps import apps

def get_table_data(table_name, columns):
    """
    Retrieve specific columns from a specific table.

    :param table_name: Name of the table (model) to query.
    :param columns: List of columns to retrieve.
    :return: Queryset with the specified columns.
    """
    # Get the model class from the table name
    model = apps.get_model('forexfrenzy', table_name)

    # Query the database for the specified columns
    data = model.objects.values(*columns)

    return data