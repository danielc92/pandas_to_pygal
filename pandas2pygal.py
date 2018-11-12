"""Import pygal for charting and numpy for aggregate functions."""
import pygal
import numpy

# HELPER FUNCTIONS


def return_data_tier1(data,
                      group_primary,
                      aggregate_by,
                      aggregate_type):
    """Return a dictionary for a one-tier chart."""
    # Aggregate the data conditionally, index set to 'group_primary'
    if aggregate_type == 'mean':
        data_new = data.groupby(group_primary).mean()
    elif aggregate_type == 'min':
        data_new = data.groupby(group_primary).min()
    elif aggregate_type == 'max':
        data_new = data.groupby(group_primary).max()
    else:
        data_new = data.groupby(group_primary).sum()

    # Convert into python dictionary and select subset by 'aggregate_by'
    dictionary = data_new.to_dict()[aggregate_by]

    return dictionary


def return_data_tier2(data,
                      group_primary,
                      group_secondary,
                      aggregate_by,
                      aggregate_type):
    """Return a dictionary for a two-tier chart."""
    # Determine aggregation method
    if aggregate_type == 'mean':
        func = numpy.mean
    elif aggregate_type == 'min':
        func = numpy.min
    elif aggregate_type == 'max':
        func = numpy.max
    else:
        func = numpy.sum

    # Create a pivot table by the two group variables
    pivotted = data.pivot_table(values=aggregate_by,
                                index=group_primary,
                                columns=group_secondary,
                                aggfunc=func)

    labels = list(pivotted.index)
    dictionary_data = pivotted.to_dict(orient='list')
    dictionary = {'data': dictionary_data, 'labels': labels}

    return dictionary

# CHARTING FUNCTIONS


def bar(data,
        group_primary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    """Return a pygal Bar chart from a pandas dataframe."""
    pyg = pygal.Bar()

    # Set custom style and config if exists
    if custom_config:
        pyg.config = custom_config

    if custom_style:
        pyg.style = custom_style

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def pie(data,
        group_primary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    """Return a pygal Pie chart from a pandas dataframe."""
    pyg = pygal.Pie()

    # Set custom style and config if exists
    if custom_config:
        pyg.config = custom_config

    if custom_style:
        pyg.style = custom_style

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def solidgauge(data,
               group_primary,
               aggregate_by,
               aggregate_type,
               custom_config=None,
               custom_style=None):
    """Return a pygal Solid Gauge chart from a pandas dataframe."""
    pyg = pygal.SolidGauge()

    # Set custom style and config if exists
    if custom_config:
        pyg.config = custom_config

    if custom_style:
        pyg.style = custom_style

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def line(data,
         group_primary,
         group_secondary,
         aggregate_by,
         aggregate_type,
         custom_config=None,
         custom_style=None):
    """Return a pygal Line chart from a pandas dataframe."""
    chart = pygal.Line()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return chart


def groupedbar(data,
               group_primary,
               group_secondary,
               aggregate_by,
               aggregate_type,
               custom_config=None,
               custom_style=None):
    """Return a pygal Grouped Bar chart from a pandas dataframe."""
    chart = pygal.Bar()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return chart


def dot(data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    """Return a pygal Dot chart from a pandas dataframe."""
    chart = pygal.Dot()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return chart


def stackedbar(data,
               group_primary,
               group_secondary,
               aggregate_by,
               aggregate_type,
               custom_config=None,
               custom_style=None):
    """Return a pygal Stacked Bar chart from a pandas dataframe."""
    chart = pygal.StackedBar()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return chart


def stackedline(data,
                group_primary,
                group_secondary,
                aggregate_by,
                aggregate_type,
                custom_config=None,
                custom_style=None):
    """Return a pygal Stacked Line chart from a pandas dataframe."""
    chart = pygal.StackedLine()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return


def radar(data,
          group_primary,
          group_secondary,
          aggregate_by,
          aggregate_type,
          custom_config=None,
          custom_style=None):
    """Return a pygal Radar chart from a pandas dataframe."""
    chart = pygal.Radar()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = return_data_tier2(data,
                                   group_primary,
                                   group_secondary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary['data'].items()]
    chart.x_labels = dictionary['labels']

    # Return chart object
    return chart


def scatter(data,
            x_values,
            y_values,
            group_primary,
            custom_config=None,
            custom_style=None):
    """Return a pygal Scatter chart from a pandas dataframe."""
    chart = pygal.XY()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary using helper function
    dictionary = {key: list(zip(
                  data[data[group_primary] == key][x_values],
                  data[data[group_primary] == key][y_values]))
                  for key in data[group_primary].unique()}

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary.items()]

    # Return chart object
    return chart
