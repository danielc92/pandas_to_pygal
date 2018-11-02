import pygal

'''
Helper functions:
These functions will turn the pandas dataframe into a format suitable
for either 1 tier or 2 tier pygal charts.
1 tier - only one group by required (eg. pie chart)
2 tier - two group by required (eg. stacked bar chart)
To transmute pandas dataframes into dictionary formats for pygal
'''


def return_data_tier1(data, group_primary, aggregate_by, aggregate_type):

    if aggregate_type == 'mean':
        data_new = data.groupby(group_primary).mean()
    elif aggregate_type == 'min':
        data_new = data.groupby(group_primary).min()
    elif aggregate_type == 'max':
        data_new = data.groupby(group_primary).max()
    else:
        data_new = data.groupby(group_primary).sum()

    dictionary = data_new.to_dict()[aggregate_by]

    return dictionary


def return_data_tier2(data, group_primary, group_secondary, aggregate_by, aggregate_type):

    pivotted = data.pivot_table(values=aggregate_by,
                                 index=group_primary,
                                 columns=group_secondary)

    labels = list(pivotted.index)
    dictionary_data = pivotted.to_dict(orient='list')
    dictionary = {'data': dictionary_data, 'labels': labels}

    return dictionary


'''
Chart Functions
'''


def pandpyg_bar(
        data,
        group_primary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):

    pyg = pygal.Bar()

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def pandpyg_pie(
        data,
        group_primary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):

    pyg = pygal.Pie()

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def pandpyg_solidgauge(
        data,
        group_primary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):

    pyg = pygal.SolidGauge()

    # Transform dataframe into dictionary
    dictionary = return_data_tier1(data,
                                   group_primary,
                                   aggregate_by,
                                   aggregate_type)

    # Add data to pygal object
    [pyg.add(key, values) for key, values in dictionary.items()]

    # Return chart
    return pyg


def pandpyg_line(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.Line()

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


def pandpyg_groupedbar(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.Bar()

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


def pandpyg_dot(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.Dot()

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

def pandpyg_stackedbar(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.StackedBar()

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


def pandpyg_stackedline(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.StackedLine()

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


def pandpyg_radar(
        data,
        group_primary,
        group_secondary,
        aggregate_by,
        aggregate_type,
        custom_config=None,
        custom_style=None):
    
    # Create pygal chart object
    chart = pygal.Radar()

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

