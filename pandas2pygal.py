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


def return_one_tier_chart(data,
                          group_primary,
                          aggregate_by,
                          aggregate_type,
                          chart_type,
                          custom_config=None,
                          custom_style=None):

    """Return a 'one-tier' pygal chart from a pandas dataframe."""
    if chart_type == 'pie':
        chart = pygal.Pie()
    elif chart_type == 'solid gauge':
        chart = pygal.SolidGauge()
    elif chart_type == 'bar':
        chart = pygal.Bar()

    # Set custom style and config if exists
    if custom_config:
        chart.config = custom_config

    if custom_style:
        chart.style = custom_style

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [chart.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return chart


def return_two_tier_chart(data,
                          group_primary,
                          group_secondary,
                          aggregate_by,
                          aggregate_type,
                          chart_type,
                          custom_config=None,
                          custom_style=None):
    """Return a pygal Line chart from a pandas dataframe."""
    if chart_type == 'line':
        chart = pygal.Line()
    elif chart_type == 'dot':
        chart = pygal.Dot()
    elif chart_type == 'grouped bar':
        chart = pygal.Bar()
    elif chart_type == 'stacked bar':
        chart = pygal.StackedBar()
    elif chart_type == 'stacked line':
        chart = pygal.StackedLine()
    elif chart_type == 'radar':
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
